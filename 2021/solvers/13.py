from typing import List

from kellog import debug, error, info, warning


def solve(lines: list[str]) -> int:
	crabs = [int(c) for c in lines[0].split(",")]
	debug(f"Total number of crabs: {len(crabs)}")

	fuels = {}
	mn, mx = min(crabs), max(crabs)
	for p in range(mn, mx + 1):
		fuels[calc_fuel(crabs, p)] = p

	fuel = min(fuels.keys())
	pos = fuels[fuel]

	info(f"Common position: {pos}")
	info(f"Minimum fuel: {fuel}")

	return fuel


def calc_fuel(crabs: list[int], p: int) -> int:
	fuel = 0
	for c in crabs:
		f = abs(c - p)
		fuel += f

	return fuel
