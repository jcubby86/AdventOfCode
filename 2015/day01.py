#!/usr/bin/env python3

import sys


def readData(fileName: str) -> str:
    with open(fileName, "r") as f:
        return f.read().strip()
    return ''


def part1(data: str):
    f = 0
    for c in data:
        if c =='(':
            f += 1
        elif c == ')':
            f -= 1
    return f


def part2(data: str):
    f = 0
    for i, c in enumerate(data):
        if c =='(':
            f += 1
        elif c == ')':
            f -= 1
        if f == -1:
            return i + 1
    return f


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
