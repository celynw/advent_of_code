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


# ==================================================================================================
def parse_args():
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument("puzzle", type=int, help="Puzzle number (2 per day)")

	return parser.parse_args()


# ==================================================================================================
if __name__ == "__main__":
	main(parse_args())
