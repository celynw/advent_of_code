#!/usr/bin/env python3
from pathlib import Path

import numpy as np
from kellog import info, warning, error, debug

import utils

# ==================================================================================================
def solve():
	lines = utils.read_puzzle_input(Path(__file__))
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
		xStep = 1 if vent[2] >= vent[0] else -1
		yStep = 1 if vent[3] >= vent[1] else -1
		horizontal = vent[0] == vent[2]
		vertical = vent[1] == vent[3]
		vent[2] += xStep
		vent[3] += yStep
		if horizontal or vertical:
			bed[vent[1]:vent[3]:yStep, vent[0]:vent[2]:xStep] += 1
		else:
			for x, y in zip(range(vent[0], vent[2], xStep), range(vent[1], vent[3], yStep)):
				bed[y, x] += 1

	info(f"Number of dangerous vents: {len(bed[bed > 1])}")
