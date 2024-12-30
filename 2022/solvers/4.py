#!/usr/bin/env python3
from rich import print, inspect

def solve(lines: list[str]) -> int:
	mapping = {
		"X": "A",
		"Y": "B",
		"Z": "C",
	}
	possibilities = list(mapping.values())

	score = 0
	for line in lines:
		opponent, you = line.split(" ")

		match you:
			case "X": # lose
				you = possibilities[(possibilities.index(opponent) - 1) % len(possibilities)]
			case "Y": # draw
				you = opponent
			case "Z": # win
				you = possibilities[(possibilities.index(opponent) + 1) % len(possibilities)]

		# Score for what you played
		score += possibilities.index(you) + 1

		# Score for the result
		result = (possibilities.index(you) - possibilities.index(opponent)) % len(possibilities)
		match result:
			case _ if result == 0: # draw
				score += 3
			case _ if result == 1: # win
				score += 6
			# case _: # lose
	print(score)

	return score
