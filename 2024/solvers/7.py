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
	search_word = "XMAS"
	occurrences = 0

	# Horizontally
	for line in lines:
		occurrences += len(re.findall(search_word, line))
		occurrences += len(re.findall(search_word[::-1], line))

	# Vertically
	columns = ["".join([line[i] for line in lines]) for i in range(len(lines[0]))]
	for column in columns:
		occurrences += len(re.findall(search_word, column))
		occurrences += len(re.findall(search_word[::-1], column))

	# Diagonally (top-right / bottom-left)
	padded_lines = []
	for i, line in enumerate(lines):
		padded_lines.append(" " * i + line + " " * (len(lines) - i))

	columns = ["".join([line[i] for line in padded_lines]) for i in range(len(padded_lines[-1]))]
	for column in columns:
		occurrences += len(re.findall(search_word, column))
		occurrences += len(re.findall(search_word[::-1], column))

	# Diagonally (top-left / bottom-right)
	padded_lines = []
	for i, line in enumerate(lines[::-1]):
		padded_lines.append(" " * i + line + " " * (len(lines) - i))

	columns = ["".join([line[i] for line in padded_lines]) for i in range(len(padded_lines[-1]))]
	for column in columns:
		occurrences += len(re.findall(search_word, column))
		occurrences += len(re.findall(search_word[::-1], column))

	return occurrences
