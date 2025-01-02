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
	# For this one, it's one block of memory, despite being on multiple lines
	text = "".join(lines)

	disabled = text.split("don't()")
	enabled = disabled.pop(0)
	for match in disabled:
		enabled += "".join(match.split("do()")[1:])

	matches = re.findall(r"(mul\(([0-9]+),([0-9]+)\))", enabled)

	return sum(int(a) * int(b) for _, a, b in matches)
