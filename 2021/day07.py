#!/usr/bin/env python3

import sys
import math


def readData(fileName: str):
    with open(fileName, "r") as f:
        return [int(x) for x in f.readlines()[0].strip().split(",")]
    return []


def part2(data):
    avg = round(sum(data) / len(data))
    best = math.inf
    changed = True
    start = avg
    while changed:
        changed = False
        cost = 0
        for i in data:
            cost += sum([j + 1 for j in range(abs(i - start))])
        if cost < best:
            best = cost
            changed = True
            start -= 1
    changed = True
    start = avg
    while changed:
        changed = False
        cost = 0
        for i in data:
            cost += sum([j + 1 for j in range(abs(i - start))])
        if cost < best:
            best = cost
            changed = True
            start += 1
    print(best)


def part1(data):
    avg = round(sum(data) / len(data))
    best = math.inf
    changed = True
    start = avg
    while changed:
        changed = False
        cost = 0
        for i in data:
            cost += abs(i - start)
        if cost < best:
            best = cost
            changed = True
            start -= 1
    changed = True
    start = avg
    while changed:
        changed = False
        cost = 0
        for i in data:
            cost += abs(i - start)
        if cost < best:
            best = cost
            changed = True
            start += 1
    print(best)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
