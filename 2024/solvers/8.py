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
	line_length = len(lines[0])
	text = "".join(lines)

	# Find overlapping patterns
	occurrences = 0
	for pattern in [
		f"(?=(M.M.{{{line_length - 2}}}A.{{{line_length - 2}}}S.S))",
		f"(?=(M.S.{{{line_length - 2}}}A.{{{line_length - 2}}}M.S))",
		f"(?=(S.M.{{{line_length - 2}}}A.{{{line_length - 2}}}S.M))",
		f"(?=(S.S.{{{line_length - 2}}}A.{{{line_length - 2}}}M.M))",
	]:
		candidates = list(re.finditer(pattern, text))
		# Drop those which are on the line boundaries
		candidates = [candidate for candidate in candidates if candidate.span()[0] % line_length < line_length - 2]
		occurrences += len(candidates)

	return occurrences
