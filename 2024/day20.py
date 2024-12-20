#!/usr/bin/env python3

from collections import defaultdict
import heapq
import math
import sys


cheats = [(-2, 0), (2, 0), (0, -2), (0, 2), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def readData(fileName: str) -> list[str]:
    with open(fileName, "r") as f:
        return [x.strip() for x in f.readlines()]
    return []


def getTile(grid, goal) -> tuple[int, int]:
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == goal:
                return r, c
    return -1, -1


def adjacencies(grid, r, c) -> list[tuple[int, int]]:
    result = []
    if r > 0 and grid[r - 1][c] != "#":
        result.append((r - 1, c))
    if r < len(grid) - 1 and grid[r + 1][c] != "#":
        result.append((r + 1, c))
    if c > 0 and grid[r][c - 1] != "#":
        result.append((r, c - 1))
    if c < len(grid[0]) - 1 and grid[r][c + 1] != "#":
        result.append((r, c + 1))
    return result


def dijkstra(grid) -> dict:
    visited = set()
    heap: list = []
    distances: dict[tuple, int | float] = defaultdict(lambda: math.inf)

    start = getTile(grid, "S")
    end = getTile(grid, "E")

    distances[start] = 0
    heapq.heappush(heap, (0, start))
    while len(heap) > 0:
        dist, current = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        for neighbor in adjacencies(grid, *current):
            tentative_distance = distances[current] + 1
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
            heapq.heappush(heap, (distances[neighbor], neighbor))

    return distances


def part1(grid: list[str]):
    result = 0

    distances = dijkstra(grid)

    for node in distances:
        for cheat in cheats:
            next = (node[0] + cheat[0], node[1] + cheat[1])
            if next in distances:
                difference = (distances[node] - distances[next]) - 2
                if difference >= 100:
                    result += 1
    return result


def part2(grid: list[str], maxDistance):
    result = 0

    distances = dijkstra(grid)
    # I got lucky that these keys happened to already be sorted by distance(ascending)
    nodes = list(distances.keys())

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            node1, node2 = nodes[i], nodes[j]
            dist = abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])
            diff = (distances[node2] - distances[node1]) - dist

            if dist > 0 and dist <= maxDistance and diff >= 100:
                result += 1

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    # print("part 1:", part2(data, 2))
    print("part 2:", part2(data, 20))
