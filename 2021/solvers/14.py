#!/usr/bin/env python3
from typing import List
import math

from kellog import info, warning, error, debug

def solve(lines: List[str]) -> int:
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


def calc_fuel(crabs: List[int], p: int) -> int:
	fuel = 0
	for c in crabs:
		d = abs(c - p)
		f = d * (d + 1) // 2
		fuel += f

	return fuel
