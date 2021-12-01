#!/usr/bin/env python3
from pathlib import Path

# ==================================================================================================
def get_puzzle_path(path: Path):
	return path.parent.parent / "puzzle_input" / "1.txt"

# ==================================================================================================
def read_puzzle_input(path: Path):
	path = get_puzzle_path(path)
	with open(path, "r") as file:
		return file.read().splitlines()
