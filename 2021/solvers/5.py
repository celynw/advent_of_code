#!/usr/bin/env python3
from typing import List

from kellog import info, warning, error, debug

# ==================================================================================================
def solve(lines: List[str]):
	debug(f"Number of commands: {len(lines)}")

	indices = {}
	for line in lines:
		for i, n in enumerate(line):
			indices[i] = indices.get(i, 0) + int(n)
	gammaRate = []
	epsilonRate = []
	for index in indices.values():
		gammaRate.append(int(index > len(lines) - index))
		epsilonRate.append(int(index < len(lines) - index))
	gammaRate = int("".join(map(str, gammaRate)), 2)
	epsilonRate = int("".join(map(str, epsilonRate)), 2)

	info(f"gammaRate: {gammaRate}")
	info(f"epsilonRate: {epsilonRate}")
	info(f"Power consumption: {gammaRate * epsilonRate}")
