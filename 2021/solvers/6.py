from kellog import debug, info


def solve(lines: list[str]) -> int:
	debug(f"Number of commands: {len(lines)}")

	oxygen_rating = lines
	co2_rating = lines
	for pos in range(len(lines[0])):
		if len(oxygen_rating) > 1:
			common = int(get_common([int(l[pos]) for l in oxygen_rating]))
			oxygen_rating = [line for line in oxygen_rating if line[pos] == str(common)]
		if len(co2_rating) > 1:
			common = int(get_common([int(l[pos]) for l in co2_rating]))
			co2_rating = [line for line in co2_rating if line[pos] != str(common)]
	oxygen_rating = int("".join(map(str, oxygen_rating)), 2)
	co2_rating = int("".join(map(str, co2_rating)), 2)

	info(f"oxygen_rating: {oxygen_rating}")
	info(f"co2_rating: {co2_rating}")
	info(f"Life Support Rating: {oxygen_rating * co2_rating}")

	return oxygen_rating * co2_rating


def get_common(values: list[int]) -> int:
	assert len(values) > 0

	return int(sum(values) >= len(values) - sum(values))
