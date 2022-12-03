#!/usr/bin/env python3
from pathlib import Path

# ==================================================================================================
def get_puzzle_path(path: Path, index: str, test: bool = False):
	parent = "examples" if test else "puzzle_input"

	return path.parent.parent / parent / f"{index}.txt"


# ==================================================================================================
def read_input(path: Path, test: bool = False):
	path = get_puzzle_path(path, path.stem, test)
	with open(path, "r") as file:
		return file.read().splitlines()
