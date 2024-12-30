#!/usr/bin/env python3

digitmap = {s: i for i, s in enumerate("zero one two three four five six seven eight nine".split())}
N_DIGITS = 2


def solve(lines: list[str]) -> int:
	"""Print and return the solution. Called by ../solve.py."""
	calibration_values = []
	for line in lines:
		calibration_value = ""

		# From the start of the line, iteratively convert words to digits to find the first digit
		done_line = ""
		for c in line:
			done_line = _convert_words_to_digits(done_line + c)
			digits = [n for n in done_line if n.isdigit()]
			if len(digits):
				calibration_value += digits[0]
				break

		# From the end of the line, iteratively convert words to digits to find the last digit
		done_line = ""
		for c in line[::-1]:
			done_line = _convert_words_to_digits(c + done_line)
			digits = [n for n in done_line if n.isdigit()]
			if len(digits):
				calibration_value += digits[0]
				break

		if len(calibration_value) != N_DIGITS:
			msg = f"Found {len(calibration_value)} digits in line, expected {N_DIGITS}: {line}"
			raise ValueError(msg)

		calibration_values.append(int(calibration_value))

	print(sum(calibration_values))  # noqa: T201

	return sum(calibration_values)



def _convert_words_to_digits(string: str) -> str:
	"""Replace all words in a string with their digit equivalent."""
	for word, digit in digitmap.items():
		string = string.replace(word, str(digit))

	return string
