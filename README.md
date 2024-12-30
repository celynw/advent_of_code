# My solutions for [Advent of Code](https://adventofcode.com/)

![GitHub repo file count (file extension)](https://img.shields.io/github/directory-file-count/celynw/advent_of_code/2021%2Fsolvers?type=file&extension=py&label=2021%20progress)\
![GitHub repo file count (file extension)](https://img.shields.io/github/directory-file-count/celynw/advent_of_code/2022%2Fsolvers?type=file&extension=py&label=2022%20progress)\
![GitHub repo file count (file extension)](https://img.shields.io/github/directory-file-count/celynw/advent_of_code/2023%2Fsolvers?type=file&extension=py&label=2023%20progress)\
![GitHub repo file count (file extension)](https://img.shields.io/github/directory-file-count/celynw/advent_of_code/2024%2Fsolvers?type=file&extension=py&label=2024%20progress)

## Setup

```bash
uv venv -p 3.13
source .venv/bin/activate
uv pip install .
```

## Usage

```bash
./solve.py YEAR PUZZLE
```

where `YEAR` is `2021` onwards, and `PUZZLE` goes from `0` to `50`.

```text
$ ./2021/solve.py --help
usage: solve.py [-h] [--test] year puzzle

positional arguments:
  year        Year of puzzle
  puzzle      Puzzle number (2 per day)

optional arguments:
  -h, --help  show this help message and exit
  --test, -t  Run with the test input and test against the answer (default: False)
```
