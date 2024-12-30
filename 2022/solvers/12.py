from rich import print


def solve(lines: list[str]) -> str:
	answers = []
	for line in lines:
		buffer = []
		for i, c in enumerate(line):
			buffer.append(c)
			if len(buffer) > 14:
				buffer.pop(0)
			if len(set(buffer)) == 14:
				break
		answers.append(i + 1)
	print(answers)

	return str(answers)[1:-1]
