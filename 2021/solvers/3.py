#!/usr/bin/env python3
from pathlib import Path

from kellog import info, warning, error, debug

import utils

# ==================================================================================================
def solve():
	lines = utils.read_puzzle_input(Path(__file__))
	debug(f"Number of commands: {len(lines)}")

	distance = 0
	depth = 0
	for line in lines:
		direction, amount = line.split(" ")
		if direction == "forward":
			distance += int(amount)
		elif direction == "down":
			depth += int(amount)
		elif direction == "up":
			depth -= int(amount)

	info(f"Final distance: {distance}")
	info(f"Final depth: {depth}")
	info(f"Multiplied: {distance * depth}")


# ==================================================================================================
if __name__ == "__main__":
	solve()
