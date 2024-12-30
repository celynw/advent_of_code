#!/usr/bin/env python3
import argparse
import importlib
from pathlib import Path
from typing import cast

from colorama import Fore


def main(args: argparse.Namespace) -> None:
	try:
		solver = importlib.import_module(f"{args.year}.solvers.{args.puzzle}")
	except ModuleNotFoundError as e:
		msg = f"Solver {args.year}.solvers.{args.puzzle} not found"
		raise ModuleNotFoundError(msg) from e

	lines = read_input(Path(cast(str, solver.__file__)), test=args.test)
	result = solver.solve(lines)

	if args.test:
		with (Path(__file__).parent / str(args.year) / "examples" / "answers.txt").open() as file:
			answers = file.read().splitlines()
		try:
			answer = int(answers[args.puzzle - 1])
		except ValueError:
			answer = answers[args.puzzle - 1]
		status = f"{Fore.GREEN}[PASS]{Fore.RESET}" if answer == result else f"{Fore.RED}[FAIL]{Fore.RESET}"
		print(f"{status} {answer} vs. {result}")


def get_puzzle_path(path: Path, index: str, *, test: bool = False):
	parent = "examples" if test else "puzzle_input"

	return path.parent.parent / parent / f"{index}.txt"


def read_input(path: Path, *, test: bool = False):
	path = get_puzzle_path(path, path.stem, test=test)
	with path.open() as file:
		return file.read().splitlines()


def _parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument("year", type=int, help="Year of puzzle")
	parser.add_argument("puzzle", type=int, help="Puzzle number (2 per day)")
	parser.add_argument("--test", "-t", action="store_true", help="Run with the test input and test against the answer")

	return parser.parse_args()


if __name__ == "__main__":
	main(_parse_args())
