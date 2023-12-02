#!/usr/bin/env python3
import colored_traceback.auto  # noqa: F401


# ======================================================================================================================
def solve(lines: list[str]) -> int:
	"""Print and return the solution. Called by ../solve.py."""
	calibration_values = []
	for line in lines:
		digits = [n for n in line if n.isdigit()]
		calibration_values.append(int(f"{digits[0]}{digits[-1]}"))

	print(sum(calibration_values))  # noqa: T201

	return sum(calibration_values)
