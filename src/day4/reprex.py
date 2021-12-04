import sys
import os
import numpy as np

input_path = os.path.abspath("inputs/day4/puzzle1.txt")
with open(input_path, mode="r") as f:
    input_data = [x.rstrip(os.linesep) for x in f.readlines()]


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
    next(input_)  # Skipping the empty line after the numbers
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


def play_bingo(numbers, boards, position):
    previous_winners = set()
    marks = np.ones(boards.shape, dtype=int)
    played_numbers = []
    for number in numbers:
        played_numbers.append(number)
        marks = marks * ~(boards == number)
        colwise_sum = np.sum(marks, axis=1)
        rowwise_sum = np.sum(marks, axis=2)
        winning_board_numbers = np.where(
            np.any(~colwise_sum.astype("bool"), axis=1)
            | np.any(~rowwise_sum.astype("bool"), axis=1)
        )[0]
        new_winners = set(winning_board_numbers) - previous_winners
        previous_winners = set(winning_board_numbers)
        if len(winning_board_numbers) == position:
            return np.array(list(new_winners)), marks, played_numbers


numbers, boards = process_bingo_input(input_data)

# Part One
w_board, w_marks, w_played_numbers = play_bingo(numbers, boards, 1)
p1_output = (
    np.sum(boards[w_board, :, :] * w_marks[w_board, :, :]) * w_played_numbers[-1]
)

# Part Two
l_board, l_marks, l_played_numbers = play_bingo(numbers, boards, boards.shape[0])
p2_output = (
    np.sum(boards[l_board, :, :] * l_marks[l_board, :, :]) * l_played_numbers[-1]
)

print(p1_output, p2_output)
