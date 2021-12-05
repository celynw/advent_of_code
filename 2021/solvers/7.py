#!/usr/bin/env python3
from typing import List

import numpy as np
from kellog import info, warning, error, debug

# ==================================================================================================
def solve(lines: List[str]):
	numbers = [int(n) for n in lines.pop(0).split(",")]

	cells = []
	for line in lines:
		if line != "":
			cells += [int(n) for n in line.split(" ") if n != ""]
	cells = np.array(cells)
	cells = cells.reshape((-1, 5, 5))

	score = None
	for number in numbers:
		if score is not None:
			break

		cells[cells == number] = -1

		for board in cells:
			if -5 in board.sum(axis=0) or -5 in board.sum(axis=1):
				score = board[board != -1].sum() * number
				break

	info(f"Score: {score}")
