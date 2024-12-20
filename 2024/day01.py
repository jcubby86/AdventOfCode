#!/usr/bin/env python3

from collections import Counter


def readData(fileName: str):
    with open(fileName, "r") as f:
        return list(zip(*[list(map(int, x.strip().split())) for x in f.readlines()]))

    return []


def part1(lists):
    return sum([abs(x - y) for x, y in list(zip(*map(sorted, lists)))])


def part2(lists):
    counter = Counter(lists[1])
    return sum(l * counter[l] for l in lists[0])


if __name__ == "__main__":
    data = readData("data.txt")

    print("part 1:", part1(data))
    print("part 2:", part2(data))
