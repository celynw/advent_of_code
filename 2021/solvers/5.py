#!/usr/bin/env python3
from pathlib import Path

from kellog import info, warning, error, debug

import utils

# ==================================================================================================
def solve():
	lines = utils.read_puzzle_input(Path(__file__))
	debug(f"Number of commands: {len(lines)}")

	indices = {}
	for line in lines:
		for i, n in enumerate(line):
			indices[i] = indices.get(i, 0) + int(n)
	gammaRate = []
	epsilonRate = []
	for k, v in indices.items():
		gammaRate.append(int(v > len(lines) - v))
		epsilonRate.append(int(v < len(lines) - v))
	gammaRate = int("".join(map(str, gammaRate)), 2)
	epsilonRate = int("".join(map(str, epsilonRate)), 2)

	info(f"gammaRate: {gammaRate}")
	info(f"epsilonRate: {epsilonRate}")
	info(f"Power consumption: {gammaRate * epsilonRate}")


# ==================================================================================================
if __name__ == "__main__":
	solve()
