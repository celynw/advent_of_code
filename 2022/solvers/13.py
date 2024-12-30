from rich import print

sizes = []


def solve(lines: list[str]) -> int:
	_tree, size = explore(lines)
	if size < 100000:
		sizes.append(size)
	print(sum(sizes))

	return sum(sizes)


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
			tree[directory] = explore(lines)
			if tree[directory][1] < 100000:
				sizes.append(tree[directory][1])
			size += tree[directory][1]  # Accumulate contained size
		elif line.startswith("$ ls"):
			size = 0
			while len(lines) > 0:
				line = lines.pop(0)
				if line.startswith("$"):
					lines.insert(0, line)  # Put line back on top
					break
				if line.startswith("dir "):
					pass
				else:
					size += int(line.split(" ")[0])

	return tree, size
