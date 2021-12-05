#!/usr/bin/env python3
from typing import List

from kellog import info, warning, error, debug

# ==================================================================================================
def solve(lines: List[str]) -> int:
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

	return increased
