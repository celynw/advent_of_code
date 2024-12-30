from kellog import debug, info


def solve(lines: list[str]) -> int:
	debug(f"Number of commands: {len(lines)}")

	distance = 0
	aim = 0
	depth = 0
	for line in lines:
		direction, amount = line.split(" ")
		if direction == "forward":
			distance += int(amount)
			depth += aim * int(amount)
		elif direction == "down":
			aim += int(amount)
		elif direction == "up":
			aim -= int(amount)

	info(f"Final distance: {distance}")
	info(f"Final depth: {depth}")
	info(f"Multiplied: {distance * depth}")

	return distance * depth
