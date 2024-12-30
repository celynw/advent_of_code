import numpy as np
from kellog import debug, info


def solve(lines: list[str]) -> int:
	numbers = [int(n) for n in lines.pop(0).split(",")]
	debug(f"Number of numbers: {len(numbers)}")

	cells = []
	for line in lines:
		if line:
			cells += [int(n) for n in line.split(" ") if n]
	cells = np.array(cells)
	cells = cells.reshape((-1, 5, 5))
	debug(f"Number of boards: {cells.shape[0]}")

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

	return score
