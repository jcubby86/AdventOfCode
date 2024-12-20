#!/usr/bin/env python3

import sys
import re


def readData(fileName: str) -> list[list[int]]:
    with open(fileName, "r") as f:
        return [list(map(int, re.findall("-?\\d+", x))) for x in f.readlines()]
    return []


def part1(data: list[list[int]]):
    width, height = 101, 103
    robots = [
        ((x + (vx * 100)) % width, (y + (vy * 100)) % height) for x, y, vx, vy in data
    ]

    quads = [0, 0, 0, 0]
    for r in robots:
        if r[0] < width // 2:
            if r[1] < height // 2:
                quads[0] += 1
            elif r[1] != height // 2:
                quads[1] += 1
        elif r[0] != width // 2:
            if r[1] < height // 2:
                quads[2] += 1
            elif r[1] != height // 2:
                quads[3] += 1

    # print(quads)
    result = 1
    for q in quads:
        result *= q
    return result


def part2(data: list[list[int]]):
    width, height = 101, 103

    for i in range(0, 1000000):
        robots = [
            ((x + (vx * i)) % width, (y + (vy * i)) % height) for x, y, vx, vy in data
        ]

        d: dict[tuple[int, int], int] = {}
        for r in robots:
            if r in d:
                d[r] += 1
            else:
                d[r] = 1

        if (max(d.values())) == 1:
            # for c in range(width):
            #   for r in range(height):
            #     if (r, c) in robots:
            #       print('*', end='')
            #     else:
            #       print('.', end = '')
            #   print()
            return i


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
