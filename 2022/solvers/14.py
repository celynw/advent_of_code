#!/usr/bin/env python3
from rich import print, inspect

sizes = []

# ==================================================================================================
def solve(lines: list[str]) -> int:
	tree, size = explore(lines)
	sizes.append(size)
	total = 70000000
	allowed = total - 30000000
	assert size > allowed

	for answer in sorted(sizes):
		if answer > size - allowed:
			print(answer)
			return answer

	raise ValueError(f"Didn't find a suitable directory")


# ==================================================================================================
def explore(lines: list[str]) -> tuple[dict, int]:
	tree = {}
	size = 0
	while len(lines) > 0:
		line = lines.pop(0)
		if line.startswith("$ cd"):
			directory = line[5:]
			if directory == "..":
				return tree, size
			else:
				tree[directory] = explore(lines)
				sizes.append(tree[directory][1])
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
