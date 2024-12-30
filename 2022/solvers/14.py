from rich import print

sizes = []


def solve(lines: list[str]) -> int:
	_tree, size = explore(lines)
	sizes.append(size)
	total = 70000000
	allowed = total - 30000000
	assert size > allowed

	for answer in sorted(sizes):
		if answer > size - allowed:
			print(answer)
			return answer

	raise ValueError("Didn't find a suitable directory")


def explore(lines: list[str]) -> tuple[dict, int]:
	tree = {}
	size = 0
	while len(lines) > 0:
		line = lines.pop(0)
		if line.startswith("$ cd"):
			directory = line[5:]
			if directory == "..":
				return tree, size
			tree[directory] = explore(lines)
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
