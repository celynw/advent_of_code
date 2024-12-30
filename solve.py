#!/usr/bin/env python3
import importlib
from pathlib import Path
from typing import Annotated, cast

import typer
from colorama import Fore


def _main(
	year: Annotated[int, typer.Argument(help="Year of puzzle")],
	puzzle: Annotated[int, typer.Argument(help="Puzzle number (2 per day)")],
	*,
	test: Annotated[
		bool,
		typer.Option("--test", "-t", help="Run with the test input and test against the answer"),
	] = False,
) -> None:
	try:
		solver = importlib.import_module(f"{year}.solvers.{puzzle}")
	except ModuleNotFoundError as e:
		msg = f"Solver {year}.solvers.{puzzle} not found"
		raise ModuleNotFoundError(msg) from e

	lines = read_input(Path(cast(str, solver.__file__)), test=test)
	result = solver.solve(lines)

	if test:
		with (Path(__file__).parent / str(year) / "examples" / "answers.txt").open() as file:
			answers = file.read().splitlines()
		try:
			answer = int(answers[puzzle - 1])
		except ValueError:
			answer = answers[puzzle - 1]
		status = f"{Fore.GREEN}[PASS]{Fore.RESET}" if answer == result else f"{Fore.RED}[FAIL]{Fore.RESET}"
		print(f"{status} {answer} vs. {result}")
	else:
		print(result)


def read_input(path: Path, *, test: bool = False):
	parent = "examples" if test else "puzzle_input"
	path = path.parent.parent / parent / f"{path.stem}.txt"

	with path.open() as file:
		return file.read().splitlines()


if __name__ == "__main__":
	typer.run(_main)
