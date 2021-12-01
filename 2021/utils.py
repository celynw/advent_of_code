#!/usr/bin/env python3
from pathlib import Path

# ==================================================================================================
def get_puzzle_path(path: Path, index: str):
	return path.parent.parent / "puzzle_input" / f"{index}.txt"

# ==================================================================================================
def read_puzzle_input(path: Path):
	path = get_puzzle_path(path, path.stem)
	with open(path, "r") as file:
		return file.read().splitlines()
