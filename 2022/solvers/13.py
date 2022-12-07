#!/usr/bin/env python3
from rich import print, inspect

answers = []

# ==================================================================================================
def solve(lines: list[str]) -> int:
	tree, size = explore(lines)
	print(sum(answers))
	if size < 100000:
		answers.append(size)

	return sum(answers)


# ==================================================================================================
def explore(lines: list[str]) -> tuple[dict, int]:
	tree = {}
	size = 0
	while len(lines) > 0:
		line = lines.pop(0)
		if line.startswith("$ cd"):
			directory = line[5:]
			print(f"Exploring {directory}")
			if directory == "..":
				return tree, size
			else:
				tree[directory] = explore(lines)
				if tree[directory][1] < 100000:
					answers.append(tree[directory][1])
				size += tree[directory][1] # Accumulate contained size
		elif line.startswith("$ ls"):
			size = 0
			while len(lines) > 0:
				line = lines.pop(0)
				if line.startswith("$"):
					lines.insert(0, line) # Put line back on top
					break
				elif line.startswith("dir "):
					pass
				else:
					size += int(line.split(" ")[0])

	return tree, size
