#!/usr/bin/env python3
import re


def solve(lines: list[str]) -> int:
	"""Print and return the solution. Called by ../solve.py."""
	part_numbers = []
	for l, line in enumerate(lines):
		for m in re.finditer(r"\d+", line):
			span_l, span_r = m.span()
			span_l = max(0, span_l - 1)
			span_r = min(len(line) - 1, span_r + 1)
			if (
				# Check above
				(l > 0 and re.search(r"[^.\d]", lines[l - 1][span_l:span_r]))
				# Check below
				or (l < len(lines) - 1 and re.search(r"[^.\d]", lines[l + 1][span_l:span_r]))
				# Check left
				or line[span_l : m.span()[0]] not in ["", "."]
				# Check right
				or line[m.span()[1] : span_r] not in ["", "."]
			):
				part_numbers.append(int(m.group()))

	print(sum(part_numbers))

	return sum(part_numbers)
