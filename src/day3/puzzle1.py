import sys
import os
sys.path.append(os.path.abspath("."))
from utils import read_input
import numpy as np

INPUT_PATH = os.path.abspath("inputs/day3/puzzle1.txt")
input_data = read_input(INPUT_PATH)


N = len(input_data)
bit_array = np.stack([np.array(list(x), dtype=int) for x in input_data])
most_ones = np.sum(bit_array, axis=0) > N/2
gamma = most_ones.astype("int")
epsilon = (~most_ones).astype("int")
gamma_rate = int("".join([str(x) for x in gamma]), base=2)
epsilon_rate = int("".join([str(x) for x in epsilon]), base=2)

output = epsilon_rate * gamma_rate

print(output) 
