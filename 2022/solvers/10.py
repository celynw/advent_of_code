from rich import print


def solve(lines: list[str]) -> str:
	stacks = []
	for line in lines:
		if len(stacks) == 0:  # 1: Initialise stacks
			stacks = [[] for _ in range((len(line) + 1) // 4)]
		if len(line) == 0 or line[1] == "1":  # 4: Skip newline
			continue
		if line.startswith("move"):  # 5: Follow instructions
			num, origin, dest = int(line.split(" ")[1]), int(line.split(" ")[3]), int(line.split(" ")[5])
			stacks[dest - 1] = stacks[origin - 1][:num] + stacks[dest - 1]
			del stacks[origin - 1][:num]
		else:  # 2: Populate stacks
			crates = [line[n] for n in range(1, len(line), 4)]
			for stack, crate in zip(stacks, crates, strict=False):
				if crate != " ":
					stack.append(crate)
	tops = [s[0] for s in stacks if len(s) > 0]
	print("".join(tops))

	return "".join(tops)
