import sys
import os
sys.path.append(os.path.abspath("."))
from utils import read_input

import pandas as pd

INPUT_PATH = os.path.abspath("inputs/day1/puzzle1.txt")
input_data = read_input(INPUT_PATH)
input_data = list(map(int, input_data))

output = (
    pd.DataFrame(
        {
            "out": input_data
        }
    )
    .assign(
        in_ = lambda x: x["out"].shift(3),
    )
    .pipe(
        lambda x: x["out"] > x["in_"]
    )
    .sum()
)

print(output)
