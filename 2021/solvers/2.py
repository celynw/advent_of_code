#!/usr/bin/env python3
from typing import List

from kellog import info, warning, error, debug

# ==================================================================================================
def solve(lines: List[str]) -> int:
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

	info(f"Decreased: {decreased}")
	info(f"Increased: {increased}")

	return increased
