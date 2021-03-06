#!/usr/bin/env python3
from typing import List

import numpy as np
from kellog import info, warning, error, debug

# ==================================================================================================
def solve(lines: List[str]) -> int:
	debug(f"Total number of vents: {len(lines)}")

	vents = []
	for line in lines:
		vents.append([int(n) for n in line.replace(" -> ", ",").split(",")])
	vents = np.array(vents)
	maxX = np.max(vents[:, [0, 2]])
	maxY = np.max(vents[:, [1, 3]])
	bed = np.zeros((maxY + 1, maxX + 1), dtype=np.int16)
	debug(f"Bed size: {bed.shape}")

	for vent in vents:
		if vent[0] == vent[2] or vent[1] == vent[3]:
			xStep = 1 if vent[2] >= vent[0] else -1
			yStep = 1 if vent[3] >= vent[1] else -1
			vent[2] += xStep
			vent[3] += yStep
			bed[vent[1]:vent[3]:yStep, vent[0]:vent[2]:xStep] += 1

	info(f"Number of dangerous vents: {len(bed[bed > 1])}")

	return len(bed[bed > 1])
