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
            "1": input_data[:-2],
            "2" : input_data[1:-1],
            "3" : input_data[2:],
        },
    )
    .transpose()
    .sum(axis=0)
    .to_frame()
    .rename(columns={0: "next"})
    .assign(now = lambda x: x.next.shift(1))
    .dropna()
    .assign(increase = lambda x: x.next > x.now)
    .increase
    .sum()
)

print(output)
