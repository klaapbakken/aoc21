import sys
import os
sys.path.append(os.path.abspath("."))
from utils import read_input
import numpy as np

def oxygen_rating_step(position, index):
    valid_numbers = position[index]
    # Keep ones if ones are the most common
    keep_ones = np.sum(valid_numbers) >= len(valid_numbers) / 2
    ones_index = position == 1
    if keep_ones:
        return index * ones_index
    else:
        return index * ~ones_index

def c02_scrubber_rating_step(position, index):
    valid_numbers = position[index]
    # Keep ones if ones are the least common
    keep_ones = np.sum(valid_numbers) < len(valid_numbers) / 2
    ones_index = position == 1
    if keep_ones:
        return index * ones_index
    else:
        return index * ~ones_index

def find_oxygen_rating(bit_array):
    index = np.ones((bit_array.shape[0],), dtype=bool)
    for i in range(bit_array.shape[1]):
        index = oxygen_rating_step(bit_array[:, i], index)
        if np.sum(index) == 1:
            return int(
                "".join((str(x) for x in np.squeeze(bit_array[index, :]))),
                base=2
            )
    return None

def find_c02_scrubber_rating(bit_array):
    index = np.ones((bit_array.shape[0],), dtype=bool)
    for i in range(bit_array.shape[1]):
        index = c02_scrubber_rating_step(bit_array[:, i], index)
        if np.sum(index) == 1:
            return int(
                "".join((str(x) for x in np.squeeze(bit_array[index, :]))),
                base=2
            )
    return None

INPUT_PATH = os.path.abspath("inputs/day3/puzzle1.txt")
input_data = read_input(INPUT_PATH)

bit_array = np.stack([np.array(list(x), dtype=int) for x in input_data])

output = find_oxygen_rating(bit_array) * find_c02_scrubber_rating(bit_array)

print(output) 
