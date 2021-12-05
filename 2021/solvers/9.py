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
		if vent[0] == vent[2] or vent[1] == vent[3]:
			xMin, xMax = sorted((vent[0], vent[2]))
			yMin, yMax = sorted((vent[1], vent[3]))
			bed[yMin:yMax + 1, xMin:xMax + 1] += 1

	info(f"Number of dangerous vents: {len(bed[bed > 1])}")
