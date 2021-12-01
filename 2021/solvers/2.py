#!/usr/bin/env python3
from pathlib import Path

from kellog import info, warning, error, debug

import utils

# ==================================================================================================
def solve():
	lines = utils.read_puzzle_input(Path(__file__))
	debug(f"Number of depth measurements: {len(lines)}")

	prevWindow = None
	prevDepths = []
	increased = 0
	decreased = 0
	for line in lines:
		currDepth = int(line)
		prevDepths.append(currDepth)
		if len(prevDepths) < 3:
			continue
		if len(prevDepths) > 3:
			prevDepths.pop(0)
		currWindow = sum(prevDepths)
		if prevWindow is None:
			prevWindow = currWindow
			continue
		if currWindow > prevWindow:
			increased += 1
		elif currWindow < prevWindow:
			decreased += 1
		prevWindow = currWindow

	info(f"increased: {increased}")
	info(f"decreased: {decreased}")


# ==================================================================================================
if __name__ == "__main__":
	solve()
