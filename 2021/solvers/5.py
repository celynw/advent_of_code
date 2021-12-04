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
	for index in indices.values():
		gammaRate.append(int(index > len(lines) - index))
		epsilonRate.append(int(index < len(lines) - index))
	gammaRate = int("".join(map(str, gammaRate)), 2)
	epsilonRate = int("".join(map(str, epsilonRate)), 2)

	info(f"gammaRate: {gammaRate}")
	info(f"epsilonRate: {epsilonRate}")
	info(f"Power consumption: {gammaRate * epsilonRate}")
