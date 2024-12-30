#!/usr/bin/env python3
import re


def solve(lines: list[str]) -> int:  # noqa: C901
	"""Print and return the solution. Called by ../solve.py."""
	parts = []
	gears = []
	for l, line in enumerate(lines):
		for m in re.finditer(r"\d+", line):
			span_l, span_r = m.span()
			span_l = max(0, span_l - 1)
			span_r = min(len(line), span_r + 1)

			if (
				# Check above
				(l > 0 and "*" in lines[l - 1][span_l:span_r])
				# Check below
				or (l < len(lines) - 1 and "*" in lines[l + 1][span_l:span_r])
				# Check left
				or (line[span_l : m.span()[0]] == "*")
				# Check right
				or (line[m.span()[1] : span_r] == "*")
			):
				parts.append((m.group(), (span_l, span_r), l))
		gears.extend((m.span()[0], l) for m in re.finditer(r"\*", line))

	ratios = []
	for gear_x, gear_y in gears:
		# Above and below
		candidates = []
		for name, (span_l, span_r), part_y in parts:
			if span_l <= gear_x < span_r and gear_y in [part_y - 1, part_y + 1]:
				candidates.append(int(name))
		if len(candidates) == 2:  # noqa: PLR2004
			ratios.append(candidates[0] * candidates[1])
			continue

		# Left and right
		candidates = []
		for name, (span_l, span_r), part_y in parts:
			if gear_x in [span_l, span_r - 1] and gear_y in [part_y - 1, part_y, part_y + 1]:
				candidates.append(int(name))
		if len(candidates) == 2:  # noqa: PLR2004
			ratios.append(candidates[0] * candidates[1])

	print(sum(ratios))  # noqa: T201

	return sum(ratios)
