from kellog import debug, info


def solve(lines: list[str]) -> int:
	debug(f"Number of depth measurements: {len(lines)}")

	prev_window = None
	prev_depths = []
	increased = 0
	decreased = 0
	for line in lines:
		curr_depth = int(line)
		prev_depths.append(curr_depth)
		if len(prev_depths) < 3:
			continue
		if len(prev_depths) > 3:
			prev_depths.pop(0)
		curr_window = sum(prev_depths)
		if prev_window is None:
			prev_window = curr_window
			continue
		if curr_window > prev_window:
			increased += 1
		elif curr_window < prev_window:
			decreased += 1
		prev_window = curr_window

	info(f"Decreased: {decreased}")
	info(f"Increased: {increased}")

	return increased
