#!/usr/bin/env python3

import sys


def readData(fileName: str) -> list[list[str]]:
    with open(fileName, "r") as f:
        return [x.split("\n") for x in f.read().split("\n\n")]
    return []


def parseKey(key):
    heights = []

    for i in range(len(key[0])):
        for j in range(1, 7):
            if key[j][i] == "#":
                heights.append(6 - j)
                break
    return heights


def parseLock(key):
    heights = []

    for i in range(len(key[0])):
        for j in range(1, 7):
            if key[j][i] == ".":
                heights.append(j - 1)
                break
    return heights


def checkPair(key, lock):
    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False
    return True


def part1(data):
    keys = []
    locks = []

    for o in data:
        if o[0][0] == ".":
            keys.append(parseKey(o))
        else:
            locks.append(parseLock(o))

    total = 0

    for key in keys:
        for lock in locks:
            if checkPair(key, lock):
                total += 1

    return total


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
