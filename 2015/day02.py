#!/usr/bin/env python3

import sys


def readData(fileName: str) -> list:
    with open(fileName, "r") as f:
        return [[int(y) for y in x.strip().split("x")] for x in f.readlines()]
    return []


def part1(data: list):
    return sum(
        [
            (2 * l * w) + (2 * w * h) + (2 * h * l) + min([l * w, w * h, l * h])
            for l, w, h in data
        ]
    )


def part2(data: list):
    return sum(
        [
            min([(2 * l) + (2 * h), (2 * w) + (2 * h), (2 * l) + (2 * w)]) + (l * w * h)
            for l, w, h in data
        ]
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
