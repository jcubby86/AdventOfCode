#!/usr/bin/env python3

import collections

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def readData(fileName: str) -> list[list[str]]:
    with open(fileName, "r") as f:
        return [list(x.strip()) for x in f.readlines()]
    return []


def move(pos, currentDir) -> tuple[int, int]:
    r, c = pos
    direction = dirs[currentDir]
    return r + direction[0], c + direction[1]


def turn(currentDir):
    return (currentDir + 1) % len(dirs)


def traverse(data, startPos) -> tuple:
    visited: dict[tuple[int, int], set[int]] = collections.defaultdict(set)
    pos: tuple[int, int] = startPos
    currentDir = 0

    while getLocation(data, pos) is not None and not (
        pos in visited and currentDir in visited[pos]
    ):
        visited[pos].add(currentDir)
        next = move(pos, currentDir)
        if getLocation(data, next) == "#":
            currentDir = turn(currentDir)
        else:
            pos = next
    return visited.keys(), getLocation(data, pos) is not None


def getLocation(data: list[list[str]], pos: tuple[int, int]) -> None | str:
    r, c = pos
    if r < 0 or r >= len(data) or c < 0 or c >= len(data[r]):
        return None
    else:
        return data[r][c]


def part1(data):
    width = len(data[0])
    startPos = [x for xs in data for x in xs].index("^")
    visited, _ = traverse(data, (startPos // width, startPos % width))
    return len(visited)


def part2(data):
    width = len(data[0])
    startIndex = [x for xs in data for x in xs].index("^")
    startPos = (startIndex // width, startIndex % width)
    visited, _ = traverse(data, startPos)

    count = 0
    for candidate in filter(lambda x: x != startPos, visited):
        r, c = candidate
        data[r][c] = "#"
        if traverse(data, startPos)[1]:
            count += 1
        data[r][c] = "."
    return count


if __name__ == "__main__":
    print("part 1:", part1(readData("data.txt")))
    print("part 2:", part2(readData("data.txt")))
