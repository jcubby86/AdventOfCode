#!/usr/bin/env python3

import sys


def readData(fileName: str) -> str:
    with open(fileName, "r") as f:
        return f.read().strip()
    return ''

def uniqueMoves(data):
    x, y = 0, 0
    visited = set([(x, y)])

    for c in data:
        if c == ">":
            x += 1
        elif c == "<":
            x -= 1
        elif c == "^":
            y += 1
        elif c == "v":
            y -= 1
        visited.add((x, y))

    return visited


def part1(data: str):
    return len(uniqueMoves(data))


def part2(data: str):
    return len(uniqueMoves(data[0::2]).union(uniqueMoves(data[1::2])))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
