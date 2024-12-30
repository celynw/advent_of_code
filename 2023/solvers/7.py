def solve(lines: list[str]) -> int:
	"""Print and return the solution. Called by ../../solve.py."""
	scores = []
	for line in lines:
		winning, have = ([int(x) for x in item.split()] for item in line.split(": ")[1].split(" | "))

		score = 0
		for h in have:
			if h in winning:
				score = score * 2 if score else 1
		scores.append(score)

	print(sum(scores))

	return sum(scores)
