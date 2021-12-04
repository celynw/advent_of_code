#!/usr/bin/env python3
from pathlib import Path

import numpy as np
from kellog import info, warning, error, debug

import utils

# ==================================================================================================
def solve() -> int:
	lines = utils.read_puzzle_input(Path(__file__))
	numbers = [int(n) for n in lines.pop(0).split(",")]

	cells = []
	for line in lines:
		if line != "":
			cells += [int(n) for n in line.split(" ") if n != ""]
	cells = np.array(cells)
	cells = cells.reshape((-1, 5, 5))

	score = None
	remove = []
	for number in numbers:
		if score is not None:
			break

		cells[cells == number] = -1

		for i, board in enumerate(cells):
			if -5 in board.sum(axis=0) or -5 in board.sum(axis=1):
				remove.append(i)

		if cells.shape[0] > 1:
			cells = np.delete(cells, remove, axis=0)
		elif len(remove) > 0:
			break
		remove = []

	board = cells.squeeze(0)
	score = board[board != -1].sum() * number
	info(f"Score: {score}")
