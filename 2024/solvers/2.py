def solve(lines: list[str]) -> int:
	"""
	Print and return the solution. Called by ../../solve.py.

	Parameters
	----------
	lines
		Puzzle input, as a list of line strings

	Returns
	-------
		Puzzle solution
	"""
	pairs = [line.split("   ") for line in lines]
	lefts, rights = zip(*pairs, strict=False)

	return sum(int(item) * rights.count(item) for item in lefts)
