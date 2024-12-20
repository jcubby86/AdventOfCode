#!/usr/bin/env python3

from collections import defaultdict
import sys
from functools import cache


def readData(fileName: str):
    with open(fileName, "r") as f:
        lines = [x.strip() for x in f.readlines()]
        return set(lines[0].split(", ")), lines[2:]
    return []


@cache
def checkPattern(pattern: str) -> int:
    if len(pattern) == 0:
        return 1
    total = 0
    for t in toweldict[pattern[0]]:
        if pattern.startswith(t):
            total += checkPattern(pattern.removeprefix(t))
    return total


def part1() -> int:
    return len([p for p in patterns if checkPattern(p) > 0])


def part2() -> int:
    return sum(checkPattern(p) for p in patterns)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    (
        towels,
        patterns,
    ) = readData(sys.argv[1])
    toweldict = defaultdict(list)
    for t in towels:
        toweldict[t[0]].append(t)

    print("part 1:", part1())
    print("part 2:", part2())
