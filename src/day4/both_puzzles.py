import sys
import os
sys.path.append(os.path.abspath("."))
from utils import read_input
import numpy as np

INPUT_PATH = os.path.abspath("inputs/day4/puzzle1.txt")
input_data = read_input(INPUT_PATH)

def process_row(line):
    digits = []
    for digit in line:
        if len(digits) == 2:
            yield int("".join(digits).lstrip())
            digits = []
        else:
            digits.append(digit)
    yield int("".join(digits).lstrip())

def process_bingo_input(input_data):
    input_ = iter(input_data)
    numbers = [int(x) for x in next(input_).split(",")]
    
    mode = "read"
    boards = []
    current_board = []
    next(input_) # Skipping the empty line after the numbers
    for line in input_:
        if not len(line):
            mode = "save"
        if mode == "read":
            current_board.append(np.array(list(process_row(line))))
        elif mode == "save":
            boards.append(np.stack(current_board))
            current_board = []
            mode = "read"
    boards.append(np.stack(current_board))
    return np.array(numbers), np.stack(boards)

def win_bingo(numbers, boards):
    marks = np.ones(boards.shape, dtype=int)
    played_numbers = []
    for number in numbers:
        played_numbers.append(number)
        marks = marks * ~(boards == number)
        colwise_sum = np.sum(marks, axis=1)
        rowwise_sum = np.sum(marks, axis=2)
        winning_board_number = np.where(
            np.any(~colwise_sum.astype("bool"), axis=1) |
            np.any(~rowwise_sum.astype("bool"), axis=1)
        )[0]
        if len(winning_board_number) > 0:
            return winning_board_number, marks, played_numbers
        
def lose_bingo(numbers, boards):
    marks = np.ones(boards.shape, dtype=int)
    played_numbers = []
    previous_winners = set()
    for number in numbers:
        played_numbers.append(number)
        marks = marks * ~(boards == number)
        colwise_sum = np.sum(marks, axis=1)
        rowwise_sum = np.sum(marks, axis=2)
        winning_board_number = np.where(
            np.any(~colwise_sum.astype("bool"), axis=1) |
            np.any(~rowwise_sum.astype("bool"), axis=1)
        )[0]
        new_winners = set(winning_board_number) - previous_winners
        previous_winners = set(winning_board_number)
        if len(winning_board_number) == boards.shape[0]:
            return np.array(list(new_winners)), marks, played_numbers

numbers, boards = process_bingo_input(input_data)

w_board, w_marks, w_played_numbers  = win_bingo(numbers, boards)
l_board, l_marks, l_played_numbers  = lose_bingo(numbers, boards)

puzzle1_output = np.sum(boards[w_board, :, :] * w_marks[w_board, :, :]) * w_played_numbers[-1]
puzzle2_output = np.sum(boards[l_board, :, :] * l_marks[l_board, :, :]) * l_played_numbers[-1]

print(puzzle1_output, puzzle2_output)
