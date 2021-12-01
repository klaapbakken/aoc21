import os

def read_input(path):
    with open(path, mode="r") as f:
        input = [x.rstrip(os.linesep) for x in f.readlines()]
    return input