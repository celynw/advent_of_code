from kellog import debug, info


def solve(lines: list[str]) -> int:
	debug(f"Number of commands: {len(lines)}")

	indices = {}
	for line in lines:
		for i, n in enumerate(line):
			indices[i] = indices.get(i, 0) + int(n)
	gamma_rate = []
	epsilon_rate = []
	for index in indices.values():
		gamma_rate.append(int(index > len(lines) - index))
		epsilon_rate.append(int(index < len(lines) - index))
	gamma_rate = int("".join(map(str, gamma_rate)), 2)
	epsilon_rate = int("".join(map(str, epsilon_rate)), 2)

	info(f"gamma_rate: {gamma_rate}")
	info(f"epsilon_rate: {epsilon_rate}")
	info(f"Power consumption: {gamma_rate * epsilon_rate}")

	return gamma_rate * epsilon_rate
