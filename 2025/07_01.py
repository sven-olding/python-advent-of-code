from collections import deque

from common import get_puzzle_input

input = get_puzzle_input("07_input.txt")


def get_start_location(lines):
    for idx, value in enumerate(lines[0]):
        if value == "S":
            return (1, idx)


beam_locations = []


def is_valid_position(grid, position):
    row, col = position
    if row >= len(grid) or col >= len(grid[row]) or row < 0 or col < 0:
        return False
    return True


def simulate_beams(grid, start):
    beams = deque([start])
    visited = set()
    splits = 0

    while beams:
        row, col = beams.popleft()

        while True:
            next_pos = (row + 1, col)
            if not is_valid_position(grid, next_pos):
                break

            row, col = next_pos
            if (row, col) in visited:
                break
            visited.add((row, col))
            beam_locations.append((row, col))

            if grid[row][col] == "^":
                splits += 1

                left = (row, col - 1)
                right = (row, col + 1)

                if is_valid_position(grid, left):
                    beams.append(left)
                if is_valid_position(grid, right):
                    beams.append(right)

                break

    return splits


current_location = get_start_location(input)
beam_locations.append(current_location)

split_count = simulate_beams(input, current_location)

result = []
for row_idx, row in enumerate(input):
    result_row = []
    for col_idx, col in enumerate(row):
        if (row_idx, col_idx) in beam_locations:
            result_row.append("|")
        else:
            result_row.append(col)

    result.append(result_row)

for row in result:
    print(row)

print(f"Splitted {split_count} times")
