import sys
import os
sys.path.append(os.path.abspath("."))
from utils import read_input

import pandas as pd

INPUT_PATH = os.path.abspath("inputs/day2/puzzle1.txt")
input_data = read_input(INPUT_PATH)

rows = [x.split(" ") for x in input_data]

movement_table = (
    pd.DataFrame
    .from_records(rows, columns=["instruction", "steps"])
    .assign(
        steps = lambda x: x.steps.astype(float), 
        aim = lambda x: (x.instruction == "down") * x.steps - (x.instruction == "up") * x.steps
    )
    .assign(
        aim = lambda x: x.aim.cumsum(),
        position = lambda x: ((x.instruction == "forward") * x.steps).cumsum(),
        depth = lambda x: ((x.instruction == "forward") * x.aim * x.steps).cumsum()
    )
    .iloc[-1,:]
)

output = int(movement_table.position * movement_table.depth)

print(output)
