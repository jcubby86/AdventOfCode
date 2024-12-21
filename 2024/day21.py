#!/usr/bin/env python3

from functools import cache
import sys

"""
numeric:
right before down
up before left

directional:
down before left
right before up
"""


def readData(fileName: str) -> list[str]:
    with open(fileName, "r") as f:
        return [x.strip() for x in f.readlines()]
    return []


DIRECTIONAL = {
    "A": {"A": [""], "^": ["<"], ">": ["v"], "v": ["<v", "v<"], "<": ["<v<", "v<<"]},
    "^": {"^": [""], "A": [">"], "v": ["v"], "<": ["v<"], ">": ["v>"]},
    "v": {"v": [""], "A": ["^>", ">^"], "^": ["^"], "<": ["<"], ">": [">"]},
    "<": {"<": [""], "A": [">>^", ">^>"], "^": [">^"], "v": [">"], ">": [">>"]},
    ">": {">": [""], "A": ["^"], "^": ["^<", "<^"], "v": ["<"], "<": ["<<"]},
}
NUMERIC = [" 0A", "123", "456", "789"]
NUMERIC_POS: dict[str, tuple[int, int]] = {}


@cache
def findNumericCoords():
    for r in range(len(NUMERIC)):
        for c in range(len(NUMERIC[r])):
            NUMERIC_POS[NUMERIC[r][c]] = (r, c)


@cache
def moveNumeric(r: int, c: int, goal: str) -> tuple[int, int, str]:
    findNumericCoords()
    gr, gc = NUMERIC_POS[goal]

    if c > gc and (gc != 0 or r != 0):  # left
        diff = c - gc
        r, c, s = moveNumeric(r, gc, goal)
        return r, c, ("<" * diff) + s
    elif r > gr:  # down
        diff = r - gr
        r, c, s = moveNumeric(gr, c, goal)
        return r, c, ("v" * diff) + s
    elif r < gr:  # up
        diff = gr - r
        r, c, s = moveNumeric(gr, c, goal)
        return r, c, ("^" * diff) + s
    elif c < gc:  # right
        diff = gc - c
        r, c, s = moveNumeric(r, gc, goal)
        return r, c, (">" * diff) + s
    else:
        return r, c, ""


@cache
def solveDirectional(chunk, depth, maxDepth):
    # print(chunk, depth)
    if depth == maxDepth:
        return len(chunk)

    total = 0
    for i, curr in enumerate(chunk):
        prev = "A" if i == 0 else chunk[i - 1]
        possibleMoves = DIRECTIONAL[prev][curr]
        total += min(
            [
                solveDirectional(move + "A", depth + 1, maxDepth)
                for move in possibleMoves
            ]
        )
    return total


def solve(data: list[str], maxDepth: int):
    complexity = 0
    for line in data:
        r, c = 0, 2
        puzzle = []
        for i in line:
            r, c, result = moveNumeric(r, c, i)
            puzzle.append(result + "A")

        total = 0
        for chunk in puzzle:
            total += solveDirectional(chunk, 0, maxDepth)

        # print(line, total, end="\n\n")
        complexity += int(line[:-1]) * total
    return complexity


def part1(data: list[str]):
    return solve(data, 2)


def part2(data: list[str]):
    return solve(data, 25)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
