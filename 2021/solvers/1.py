#!/usr/bin/env python3
from pathlib import Path

from kellog import info, warning, error, debug

import utils

# ==================================================================================================
def solve():
	lines = utils.read_puzzle_input(Path(__file__))
	debug(f"Number of depth measurements: {len(lines)}")

	prevDepth = None
	increased = 0
	decreased = 0
	for line in lines:
		currDepth = int(line)
		if prevDepth is None:
			prevDepth = currDepth
			continue
		if currDepth > prevDepth:
			increased += 1
		elif currDepth < prevDepth:
			decreased += 1
		prevDepth = currDepth

	info(f"increased: {increased}")
	info(f"decreased: {decreased}")
