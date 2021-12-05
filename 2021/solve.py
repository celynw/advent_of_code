#!/usr/bin/env python3
import argparse
import importlib
from pathlib import Path

import utils

# ==================================================================================================
def main(args: argparse.Namespace):
	solver = importlib.import_module(f"solvers.{args.puzzle}")
	lines = utils.read_input(Path(solver.__file__), args.test)
	result = solver.solve(lines)

	if args.test:
		with open(Path(__file__).parent / "examples" / "answers.txt", "r") as file:
			answers = file.read().splitlines()
		status = "[PASS]" if int(answers[args.puzzle - 1]) == result else "[FAIL]"
		print(f"{status} {int(answers[args.puzzle - 1])} vs. {result}")


# ==================================================================================================
def parse_args():
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument("puzzle", type=int, help="Puzzle number (2 per day)")
	parser.add_argument("--test", "-t", action="store_true", help="Run with the test input and test against the answer")

	return parser.parse_args()


# ==================================================================================================
if __name__ == "__main__":
	main(parse_args())
