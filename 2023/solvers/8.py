def solve(lines: list[str]) -> int:
	"""Print and return the solution. Called by ../solve.py."""
	won = {}
	total = 0
	for l, line in enumerate(lines):
		winning, have = ([int(x) for x in item.split()] for item in line.split(": ")[1].split(" | "))

		score = 0
		for h in have:
			if h in winning:
				score += 1

		if score:
			won[l] = [l + r + 1 for r in range(score)]
		else:
			total += 1  # This card

	for w in won:
		total += accumulate_cards(won, w)

	print(total)

	return total


def accumulate_cards(won: dict[int, list[int]], index: int, indent: str = "") -> int:
	"""Recurse and count the total number of won cards."""
	connected = won.get(index, [])
	total = 1  # This card

	for c in connected:
		total += accumulate_cards(won, c, indent + "  ")

	return total
