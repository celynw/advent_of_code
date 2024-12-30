#!/usr/bin/env python3
from rich import print, inspect

def solve(lines: list[str]) -> int:
	all_calories = []
	calories = 0
	for line in lines:
		if line == "":
			all_calories.append(calories)
			calories = 0
		else:
			calories += int(line)
	all_calories.append(calories)

	all_calories = sorted(all_calories)
	top_calories = sum(all_calories[-3:])
	print(top_calories)

	return top_calories
