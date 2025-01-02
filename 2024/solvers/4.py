def check_safety(levels: list[int]) -> bool:
	"""
	Check if the levels are safe.

	Parameters
	----------
	levels
		List of levels

	Returns
	-------
		True if the levels are safe, False otherwise
	"""
	safe = True
	increasing = levels[-1] - levels[0] > 0
	for i in range(len(levels) - 1):
		difference = int(levels[i + 1]) - int(levels[i])
		if not increasing:
			difference *= -1
		if 1 <= difference <= 3:
			continue
		safe = False
		break

	return safe


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
		levels = [int(l) for l in report.split(" ")]
		safe = check_safety(levels)
		if safe:
			num_safe += 1
		else:
			# Try removing one level
			for i in range(len(levels)):
				levels_copy = levels.copy()
				levels_copy.pop(i)
				safe = check_safety(levels_copy)
				if safe:
					num_safe += 1
					break

	return num_safe
