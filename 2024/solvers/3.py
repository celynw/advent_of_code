def solve(reports: list[str]) -> int:
	"""
	Print and return the solution. Called by ../../solve.py.

	Parameters
	----------
	reports
		Puzzle input, as a list of line strings

	Returns
	-------
		Puzzle solution
	"""
	num_safe = 0
	for report in reports:
		safe = True
		levels = [int(l) for l in report.split(" ")]
		increasing = levels[-1] - levels[0] > 0
		for i in range(len(levels) - 1):
			difference = int(levels[i + 1]) - int(levels[i])
			if not increasing:
				difference *= -1
			if 1 <= difference <= 3:
				continue
			safe = False
			break
		if safe:
			num_safe += 1

	return num_safe
