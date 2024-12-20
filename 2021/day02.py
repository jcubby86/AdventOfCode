#!/usr/bin/env python3

import sys


def readData(fileName: str):
    with open(fileName, "r") as f:
        lines = [x.split() for x in f.readlines()]
        pairs = [(x, int(y)) for x, y in lines]
        return pairs
    return []


def part1(data):
    pos = 0
    depth = 0
    for x, y in data:
        if x == "forward":
            pos += y
        if x == "up":
            depth -= y
        if x == "down":
            depth += y
    print(pos * depth)


def part2(data):
    pos = 0
    aim = 0
    depth = 0
    for x, y in data:
        if x == "forward":
            pos += y
            depth += aim * y
        if x == "up":
            aim -= y
        if x == "down":
            aim += y
    print(pos * depth)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
