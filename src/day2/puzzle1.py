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
    .from_records(rows, columns=["direction", "steps"])
    .assign(steps = lambda x: x.steps.astype(float))
    .groupby("direction")
    .agg("sum")
)

output = int(
    (movement_table.loc["down", "steps"] - movement_table.loc["up", "steps"]) 
    * movement_table.loc["forward", "steps"]
)

print(output)
