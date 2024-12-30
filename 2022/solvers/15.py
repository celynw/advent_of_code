from rich import print


def solve(lines: list[str]) -> int:
	forest = []
	for line in lines:
		forest.append([int(n) for n in line])

	indices = set()
	for y, row in enumerate(forest):
		highest = -1
		for x, tree in enumerate(row):  # Left to right
			if tree > highest:
				indices.add((x, y))
				highest = tree
		highest = -1
		for x, tree in reversed(list(enumerate(row))):  # Right to left
			if tree > highest:
				indices.add((x, y))
				highest = tree
	for x, col in enumerate(map(list, zip(*forest, strict=False))):
		highest = -1
		for y, tree in enumerate(col):  # Top to bottom
			if tree > highest:
				indices.add((x, y))
				highest = tree
		highest = -1
		for y, tree in reversed(list(enumerate(col))):  # Bottom to top
			if tree > highest:
				indices.add((x, y))
				highest = tree

	print(len(indices))

	return len(indices)
