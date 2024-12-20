#!/usr/bin/env python3

import sys


def readData(fileName: str):
    with open(fileName, "r") as f:
        data = [x.strip() for x in f.readlines()]
        m = [0]
        lines = [
            [[findMax(int(z), m) for z in y.split(",")] for y in x.split(" -> ")]
            for x in data
        ]

        return lines, m[0]
    return []


def findMax(z, m):
    if z > m[0]:
        m[0] = z
    return z


def printGrid(grid):
    points = 0
    for row in grid:
        for val in row:
            print("." if val == 0 else val, end="")
            if val >= 2:
                points += 1
        print()
    return points


def part1(data):
    lines = data[0]
    m = data[1]
    grid = [[0 for i in range(m + 1)] for j in range(m + 1)]
    for line in lines:
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]
        if x1 == x2:
            diff = 1 if y2 >= y1 else -1
            for y in range(y1, y2 + diff, diff):
                grid[y][x1] += 1
        elif y1 == y2:
            diff = 1 if x2 >= x1 else -1
            for x in range(x1, x2 + diff, diff):
                grid[y1][x] += 1
        else:
            diffx = 1 if x2 >= x1 else -1
            diffy = 1 if y2 >= y1 else -1
            x = x1
            y = y1
            while x != x2 + diffx:
                grid[y][x] += 1
                x += diffx
                y += diffy

    print(printGrid(grid))


def part2(data):
    pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
