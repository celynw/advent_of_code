#!/usr/bin/env python3
from rich import print, inspect

# ==================================================================================================
def solve(lines: list[str]) -> int:
	redundant = 0
	for line in lines:
		section1, section2 = line.split(",")
		low1, high1 = [int(n) for n in section1.split("-")]
		low2, high2 = [int(n) for n in section2.split("-")]
		combined_len = len(set(range(low1, high1 + 1)) & set(range(low2, high2 + 1)))
		if combined_len in [high1 - low1 + 1, high2 - low2 + 1]:
			redundant += 1

	print(redundant)

	return redundant
