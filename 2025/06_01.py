import operator
from functools import reduce
from pathlib import Path

HERE = Path(__file__).parent
input_file = HERE / "06_input.txt"

with input_file.open() as f:
    lines = f.read().splitlines()

rows = [line.split() for line in lines]
columns = list(zip(*rows))  # zip with * (unpacking) transposes the rows to cols

results = []
for column in columns:
    operand = column[-1]
    numbers = [int(i) for i in column[:-1]]

    results.append(reduce(operator.mul if operand == "*" else operator.add, numbers))

print(f"Sum: {sum(results)}")
