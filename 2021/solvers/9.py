import numpy as np
from kellog import debug, info


def solve(lines: list[str]) -> int:
	debug(f"Total number of vents: {len(lines)}")

	vents = []
	for line in lines:
		vents.append([int(n) for n in line.replace(" -> ", ",").split(",")])
	vents = np.array(vents)
	max_x = np.max(vents[:, [0, 2]])
	max_y = np.max(vents[:, [1, 3]])
	bed = np.zeros((max_y + 1, max_x + 1), dtype=np.int16)
	debug(f"Bed size: {bed.shape}")

	for vent in vents:
		if vent[0] == vent[2] or vent[1] == vent[3]:
			x_step = 1 if vent[2] >= vent[0] else -1
			y_step = 1 if vent[3] >= vent[1] else -1
			vent[2] += x_step
			vent[3] += y_step
			bed[vent[1] : vent[3] : y_step, vent[0] : vent[2] : x_step] += 1

	info(f"Number of dangerous vents: {len(bed[bed > 1])}")

	return len(bed[bed > 1])
