from rich import print


def solve(lines: list[str]) -> int:
	all_calories = []
	calories = 0
	for line in lines:
		if not line:
			all_calories.append(calories)
			calories = 0
		else:
			calories += int(line)
	all_calories.append(calories)

	max_calories = max(all_calories)
	print(max_calories)

	return max_calories
