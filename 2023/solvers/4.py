#!/usr/bin/env python3
import operator
from functools import reduce


def solve(lines: list[str]) -> int:
	"""Print and return the solution. Called by ../solve.py."""
	powers = []
	for line in lines:
		_, results = line.split(": ")

		fewest = {
			"red": 0,
			"green": 0,
			"blue": 0,
		}

		sets = results.split("; ")
		for _set in sets:
			cube_colours = _set.split(", ")
			pairs = [tuple(cube_colour.split(" ")) for cube_colour in cube_colours]
			for pair in pairs:
				fewest[pair[1]] = max(fewest[pair[1]], int(pair[0]))
		powers.append(reduce(operator.mul, fewest.values(), 1))

	print(sum(powers))  # noqa: T201

	return sum(powers)
