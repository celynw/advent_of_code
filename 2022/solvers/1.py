#!/usr/bin/env python3
from rich import print, inspect

# ==================================================================================================
def solve(lines: list[str]) -> int:
	all_calories = []
	calories = 0
	for line in lines:
		if line == "":
			all_calories.append(calories)
			calories = 0
		else:
			calories += int(line)

	max_calories = max(all_calories)
	print(max_calories)

	return max_calories
