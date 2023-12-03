#!/usr/bin/env python3
import math

from rich import print, inspect

# ==================================================================================================
def solve(lines: list[str]) -> int:
	forest = []
	for line in lines:
		forest.append([int(n) for n in line])

	scores = [score(x, y, forest) for y in range(len(forest)) for x in range(y)]

	print(max(scores))

	return max(scores)


# ==================================================================================================
def score(tree_x: int, tree_y: int, forest: list[list[int]]) -> int:
	tree_height = forest[tree_y][tree_x]
	all_seen = []

	# Left
	seen = 0
	for x in range(tree_x - 1, -1, -1):
		seen += 1
		if forest[tree_y][x] >= tree_height:
			break
	all_seen.append(seen)

	# Right
	seen = 0
	for x in range(tree_x + 1, len(forest[0]), 1):
		seen += 1
		if forest[tree_y][x] >= tree_height:
			break
	all_seen.append(seen)

	# Up
	seen = 0
	for y in range(tree_y - 1, -1, -1):
		seen += 1
		if forest[y][tree_x] >= tree_height:
			break
	all_seen.append(seen)

	# Down
	seen = 0
	for y in range(tree_y + 1, len(forest), 1):
		seen += 1
		if forest[y][tree_x] >= tree_height:
			break
	all_seen.append(seen)


	return math.prod(all_seen)
