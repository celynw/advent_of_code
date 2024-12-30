from kellog import debug, info


def solve(lines: list[str]) -> int:
	debug(f"Number of depth measurements: {len(lines)}")

	prev_depth = None
	increased = 0
	decreased = 0
	for line in lines:
		curr_depth = int(line)
		if prev_depth is None:
			prev_depth = curr_depth
			continue
		if curr_depth > prev_depth:
			increased += 1
		elif curr_depth < prev_depth:
			decreased += 1
		prev_depth = curr_depth

	info(f"Decreased: {decreased}")
	info(f"Increased: {increased}")

	return increased
