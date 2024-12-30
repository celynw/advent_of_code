def solve(lines: list[str]) -> int:
	"""Print and return the solution. Called by ../solve.py."""
	targets = [int(s) for s in lines.pop(0).split(" ")[1:]]
	maps = parse(lines)

	for mapping in maps.values():
		for s, seed in enumerate(targets):
			for l in mapping:
				dest_start, src_start, length = l
				if seed in range(src_start, src_start + length + 1):
					targets[s] = dest_start + (seed - src_start)
					break
				targets[s] = seed

	print(min(targets))

	return min(targets)


def parse(lines: list[str]) -> dict[str, list[list[int]]]:
	"""Extract maps from input lines."""
	maps = {}
	name = ""
	these_maps = []
	for line in lines:
		if not line:
			continue

		if ":" in line:
			if name:
				maps[name] = these_maps
			name, _ = line.split(" ")
			these_maps = []
		else:
			these_maps.append([int(n) for n in line.split(" ")])

	if name not in maps:
		maps[name] = these_maps

	return maps
