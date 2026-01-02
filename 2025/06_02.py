import operator
from functools import reduce
from pathlib import Path

HERE = Path(__file__).parent
input_file = HERE / "06_input.txt"

with input_file.open() as f:
    lines = f.read().splitlines()

# lines = """123 328  51 64
# 45 64  387 23
#  6 98  215 314
# *   +   *   +   """.splitlines()


width = max(len(line) for line in lines)
grid = [line.ljust(width) for line in lines]
columns = list(zip(*grid))

total_grand_sum = 0
current_problem_numbers = []
current_operator = None


def calculate_result(numbers, op):
    if op == "*":
        return reduce(operator.mul, numbers)
    return sum(numbers)


for col in reversed(columns):
    col_str = "".join(col)

    if col_str.strip() == "":
        if current_problem_numbers:
            total_grand_sum += calculate_result(
                current_problem_numbers, current_operator
            )
            current_problem_numbers = []
            current_operator = None
            continue

    digits_part = "".join(col[:-1]).strip()
    op_part = col[-1].strip()

    if digits_part:
        current_problem_numbers.append(int(digits_part))

    if op_part in ("+", "*"):
        current_operator = op_part

if current_problem_numbers:
    total_grand_sum += calculate_result(current_problem_numbers, current_operator)

print(total_grand_sum)
