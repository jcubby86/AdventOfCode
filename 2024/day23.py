#!/usr/bin/env python3

from collections import defaultdict
import sys


def readData(fileName: str) -> list:
    with open(fileName, "r") as f:
        return [tuple(x.strip().split("-")) for x in f.readlines()]
    return []


def part1(data: list):
    adjList: dict[str, set[str]] = defaultdict(set)
    triplets: set[tuple] = set()

    for x, y in data:
        adjList[x].add(y)
        adjList[y].add(x)

    for c1 in adjList:
        for c2 in adjList[c1]:
            common = adjList[c1].intersection(adjList[c2])
            for c3 in common:
                triplets.add(tuple(sorted([c1, c2, c3])))

    total = 0
    for t in triplets:
        if any([x.startswith("t") for x in t]):
            total += 1

    return total


def part2(data: list):
    adjList: dict[str, set[str]] = defaultdict(set)
    groups: list[set] = []

    for x, y in data:
        adjList[x].add(y)
        adjList[y].add(x)

    for c1 in adjList:
        for group in groups[::-1]:
            common = adjList[c1].intersection(group)
            # print(c1, group, common)
            if len(common) == len(group):
                common.add(c1)
                groups.append(common)
        groups.append(set([c1]))

    maxSize = max(map(len, groups))
    bestGroup = list(filter(lambda x: len(x) == maxSize, groups))
    return ",".join(sorted(bestGroup[0]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
