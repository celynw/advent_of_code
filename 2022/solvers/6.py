from rich import print


def solve(lines: list[str]) -> int:
	priority = 0
	group = []
	for line in lines:
		group.append(line)
		if len(group) == 3:
			badge = list(set(group[0]) & set(group[1]) & set(group[2]))[0]

			if badge == badge.lower():
				priority += ord(badge) - ord("a") + 1
			elif badge == badge.upper():
				priority += ord(badge) - ord("A") + 27
			group = []
	print(priority)

	return priority
