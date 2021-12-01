import sys
import os
sys.path.append(os.path.abspath("."))
from utils import read_input

INPUT_PATH = os.path.abspath("inputs/day1/puzzle1.txt")

input_data = read_input(INPUT_PATH)

now = map(float, input_data[:-1])
next = map(float, input_data[1:])

output = sum([int(y > x) for x, y in zip(now, next)])

print(output)
