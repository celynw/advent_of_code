#!/usr/bin/env python3
from pathlib import Path
from typing import List

from kellog import info, warning, error, debug

import utils

# ==================================================================================================
def solve():
	lines = utils.read_puzzle_input(Path(__file__))
	debug(f"Number of commands: {len(lines)}")

	oxygenRating = lines
	co2Rating = lines
	for pos in range(len(lines[0])):
		if len(oxygenRating) > 1:
			common = int(get_common([int(l[pos]) for l in oxygenRating]))
			oxygenRating = [line for line in oxygenRating if line[pos] == str(common)]
		if len(co2Rating) > 1:
			common = int(get_common([int(l[pos]) for l in co2Rating]))
			co2Rating = [line for line in co2Rating if not line[pos] == str(common)]
	oxygenRating = int("".join(map(str, oxygenRating)), 2)
	co2Rating = int("".join(map(str, co2Rating)), 2)

	info(f"oxygenRating: {oxygenRating}")
	info(f"co2Rating: {co2Rating}")
	info(f"Life Support Rating: {oxygenRating * co2Rating}")


# ==================================================================================================
def get_common(values: List[int]) -> int:
	assert len(values) > 0

	return int(sum(values) >= len(values) - sum(values))


# ==================================================================================================
if __name__ == "__main__":
	solve()
