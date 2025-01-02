import re


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
	total = 0
	for line in lines:
		matches = re.findall(r"(mul\(([0-9]+),([0-9]+)\))", line)
		total += sum(int(a) * int(b) for _, a, b in matches)

	return total
