#!/usr/bin/env python3
from typing import List

from kellog import info, warning, error, debug

# ==================================================================================================
def solve(lines: List[str]) -> int:
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

	return distance * depth
