#!/usr/bin/env python3

import sys
from collections import defaultdict
import heapq


def readData(fileName: str):
    with open(fileName, "r") as f:
        return [tuple(map(int, x.split(","))) for x in f.readlines()]
    return []


def part1(size, fallen, bytePositions):
    fallen = set([b for b in bytePositions[: fallen + 1]])
    # print(fallen)
    adjList = defaultdict(list)
    for r in range(size):
        for c in range(size):
            if r > 0 and (r - 1, c) not in fallen:
                adjList[(r, c)].append((r - 1, c))
            if r < size - 1 and (r + 1, c) not in fallen:
                adjList[(r, c)].append((r + 1, c))
            if c > 0 and (r, c - 1) not in fallen:
                adjList[(r, c)].append((r, c - 1))
            if c < size - 1 and (r, c + 1) not in fallen:
                adjList[(r, c)].append((r, c + 1))

    distances = defaultdict(lambda: size**size)
    distances[(0, 0)] = 0
    visited = set()
    heap = []

    heapq.heappush(heap, (0, (0, 0)))
    while len(heap) > 0:
        dist, current = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        for neighbor in adjList[current]:
            tentative_distance = distances[current] + 1
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
            heapq.heappush(heap, (distances[neighbor], neighbor))

    return distances[(size - 1, size - 1)]


def part2(size, fallen, bytePositions):
    for i in range(fallen, len(bytePositions)):
        result = part1(size, i, bytePositions)
        # print(result)
        if result >= size**size:
            return bytePositions[i]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(71, 1024, data))
    print("part 2:", part2(71, 1024, data))
