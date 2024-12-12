#!/usr/bin/env python3

from collections import defaultdict
from fractions import Fraction

def readInput(fileName: str) -> list[str]:
    with open(fileName, "r") as f:
        return [x.strip() for x in f.readlines()]

    return []

def reduced(r: int, c: int):
    f =  Fraction(r, c)
    return f.numerator, f.denominator

def checkPair1(r1: int, c1: int, r2: int, c2: int, height: int, width: int) -> set:
    antinodes = set()
    dr, dc = reduced(r2 - r1, c2 - c1)
    r, c = r1, c1

    # print({'r1': r1, 'c1': c1, 'r2': r2, 'c2': c2, 'dr': dr, 'dc': dc})
    while r >= 0 and c >= 0 and r < height and c < width: 
        r -= dr
        c -= dc
    while True:
        r += dr
        c += dc
        if not(r >= 0 and c >= 0 and r < height and c < width): break
        if (r == r1 and c == c1) or (r == r2 and c == c2): 
            continue
        d1 = (r1 - r, c1 - c)
        d2 = (r2 - r, c2 - c)
        # print(r, c, d1, d2)
        if (d1[0] * 2 == d2[0] and d1[1] * 2 == d2[1]) or (d1[0] == d2[0]*2 and d1[1] == d2[1]*2):
            antinodes.add((r, c))

    return antinodes

def checkFreq1(pairs: list[tuple[int, int]], height, width) -> set[tuple[int, int]]:
    antinodes = set()

    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):
            r1, c1 = pairs[i]
            r2, c2 = pairs[j]
            antinodes.update(checkPair1(r1, c1, r2, c2, height, width))

    return antinodes

def mapOut1(input: list[str]) -> set[tuple[int, int]]:
    antennas: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)
    antinodes: set[tuple[int, int]] = set()
    height = len(input)
    width = len(input[0])

    for r in range(len(input)):
        for c in range(len(input[r])):
            freq = input[r][c]
            if freq != ".":
                antennas[freq].append((r,c))

    # print(antennas)
    for freq in antennas:
        antinodes.update(checkFreq1(antennas[freq], height, width))

    return antinodes


def part1(input: list[str]):
    result = mapOut1(input)
    # print(sorted(list(result)))
    return len(result)

def checkPair2(r1: int, c1: int, r2: int, c2: int, height: int, width: int) -> set:
    antinodes = set()
    dr, dc = reduced(r2 - r1, c2 - c1)
    r, c = r1, c1

    # print({'r1': r1, 'c1': c1, 'r2': r2, 'c2': c2, 'dr': dr, 'dc': dc})
    while r >= 0 and c >= 0 and r < height and c < width: 
        r -= dr
        c -= dc
    while True:
        r += dr
        c += dc
        if not(r >= 0 and c >= 0 and r < height and c < width): break
        antinodes.add((r, c))

    return antinodes

def checkFreq2(pairs: list[tuple[int, int]], height, width) -> set[tuple[int, int]]:
    antinodes = set()

    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):
            r1, c1 = pairs[i]
            r2, c2 = pairs[j]
            antinodes.update(checkPair2(r1, c1, r2, c2, height, width))

    return antinodes

def mapOut2(input: list[str]) -> set[tuple[int, int]]:
    antennas: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)
    antinodes: set[tuple[int, int]] = set()
    height = len(input)
    width = len(input[0])

    for r in range(len(input)):
        for c in range(len(input[r])):
            freq = input[r][c]
            if freq != ".":
                antennas[freq].append((r,c))

    # print(antennas)
    for freq in antennas:
        antinodes.update(checkFreq2(antennas[freq], height, width))

    return antinodes


def part2(input: list[str]):
    result = mapOut2(input)
    # print(sorted(list(result)))
    return len(result)


if __name__ == "__main__":
    input = readInput("day08.txt")

    print("part 1:", part1(input))
    print("part 2:", part2(input))
