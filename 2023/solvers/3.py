query = {
	"red": 12,
	"green": 13,
	"blue": 14,
}


def solve(lines: list[str]) -> int:
	"""Print and return the solution. Called by ../../solve.py."""
	possible_ids = []
	for line in lines:
		game, results = line.split(": ")

		game_id = int(game[5:])

		possible = True
		sets = results.split("; ")
		for _set in sets:
			cube_colours = _set.split(", ")
			pairs = [tuple(cube_colour.split(" ")) for cube_colour in cube_colours]
			if not all(int(pair[0]) <= query[pair[1]] for pair in pairs):
				possible = False
				break
		if possible:
			possible_ids.append(game_id)

	print(sum(possible_ids))

	return sum(possible_ids)
