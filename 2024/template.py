#!/usr/bin/env python3

import sys


def readData(fileName: str) -> list[str]:
    with open(fileName, "r") as f:
        return [x.strip() for x in f.readlines()]
    return []


def part1(data: list[str]):
    return data


def part2(data: list[str]):
    pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
