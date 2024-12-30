#!/usr/bin/env python3
from rich import print, inspect

def solve(lines: list[str]) -> int:
	priority = 0
	for line in lines:
		num_items = len(line) // 2
		first, second = line[:num_items], line[num_items:]
		assert len(first) == len(second)

		# Find common item
		common_item = list(set(first).intersection(second))[0]

		# Work out priority
		if common_item == common_item.lower():
			priority += ord(common_item) - ord("a") + 1
		elif common_item == common_item.upper():
			priority += ord(common_item) - ord("A") + 27

	print(priority)

	return priority
