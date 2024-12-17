#!/usr/bin/env python3

import sys
from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def getStartTile(input) -> tuple[int, int]:
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "S":
                return r, c
    return -1, -1


def readInput(fileName: str) -> list[str]:
    with open(fileName, "r") as f:
        return [x.strip() for x in f.readlines()]
    return []


def part2(input: list[str]):
    r, c = getStartTile(input)

    toVisit: deque[tuple[int, int, int, int, list[tuple[int, int]]]] = deque()
    visited: dict[tuple[int, int, int], int] = {}
    solutions: list[int] = []
    solutionPaths: list[list[tuple[int, int]]] = []

    toVisit.append((r, c, 0, 0, []))
    while len(toVisit) > 0:
        r, c, dir, dist, path = toVisit.popleft()
        np = path + [(r, c)]

        if input[r][c] == "E":
            solutions.append(dist)
            solutionPaths.append(np)
            continue
        if input[r][c] == "#":
            continue
        if (r, c, dir) in visited and dist > visited[(r, c, dir)]:
            continue
        if len(solutions) > 0 and dist > min(solutions):
            continue

        visited[(r, c, dir)] = dist

        straight = dirs[dir]
        toVisit.append((r + straight[0], c + straight[1], dir, dist + 1, np))
        toVisit.append((r, c, (dir - 1) % len(dirs), dist + 1000, path))
        toVisit.append((r, c, (dir + 1) % len(dirs), dist + 1000, path))

    best = min(solutions)
    bestSeats = set()

    for i in range(len(solutions)):
        if solutions[i] == best:
            bestSeats.update(solutionPaths[i])

    return best, len(bestSeats)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        exit(1)

    input = readInput(sys.argv[1])
    best, bestSeats = part2(input)

    print("part 1:", best)
    print("part 2:", bestSeats)
