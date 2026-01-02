from pathlib import Path


def get_puzzle_input(filename: str):
    HERE = Path(__file__).parent
    input_file = HERE / filename
    with input_file.open() as f:
        return f.read().splitlines()
