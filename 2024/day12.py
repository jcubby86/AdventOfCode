#!/usr/bin/env python3

from collections import defaultdict
import sys
from typing import Any


def readData(fileName: str) -> list[str]:
    with open(fileName, "r") as f:
        return [x.strip() for x in f.readlines()]
    return []


def part1(data: list[str]):
    regions: list[list[Any]] = []
    plotToRegion: dict[tuple[int, int], int] = {}

    def mergeRegions(i, j):
        # print('merging',i, regions[i],j, regions[j])
        regions[i][1] += regions[j][1]
        regions[i][2] += regions[j][2]

        for p in plotToRegion:
            if plotToRegion[p] == j:
                plotToRegion[p] = i
        regions[j] = ["", 0, 0]

    def matchRegion(r, c):
        sidesMatched = 0
        regionsMatched = []
        if r > 0 and data[r][c] == data[r - 1][c]:
            sidesMatched += 1
            regionsMatched.append(plotToRegion[(r - 1, c)])
        if c > 0 and data[r][c] == data[r][c - 1]:
            sidesMatched += 1
            regionsMatched.append(plotToRegion[(r, c - 1)])

        if len(regionsMatched) == 0:
            return 0, None

        if len(set(regionsMatched)) > 1:
            mergeRegions(regionsMatched[0], regionsMatched[1])

        return sidesMatched, regionsMatched[0]

    for r in range(len(data)):
        for c in range(len(data[r])):
            sidesMatched, region = matchRegion(r, c)
            if sidesMatched > 0:
                plotToRegion[(r, c)] = region
                regions[region][1] += 1
                if sidesMatched == 1:
                    regions[region][2] += 2
            else:
                regions.append([data[r][c], 1, 4])
                plotToRegion[(r, c)] = len(regions) - 1

    # for region in regions:
    #   print(*region)
    # for p in plotToRegion:
    #   print(p, plotToRegion[p])
    return sum([a * p for t, a, p in regions])


def part2(data: list[str]):
    regions: list[list[Any]] = []
    plotToRegion: dict[tuple[int, int], int] = {}

    def mergeRegions(i, j):
        # print('merging',i, regions[i],j, regions[j])
        regions[i][1] += regions[j][1]
        regions[i][2] += regions[j][2]

        for p in plotToRegion:
            if plotToRegion[p] == j:
                plotToRegion[p] = i
        regions[j] = ["", 0, 0]

    def matchRegion(r, c):
        sidesMatched = []
        regionsMatched = []
        if r > 0 and data[r][c] == data[r - 1][c]:
            sidesMatched.append("t")
            regionsMatched.append(plotToRegion[(r - 1, c)])
        if c > 0 and data[r][c] == data[r][c - 1]:
            sidesMatched.append("l")
            regionsMatched.append(plotToRegion[(r, c - 1)])
        if c > 0 and r > 0 and data[r][c] == data[r - 1][c - 1]:
            sidesMatched.append("lc")
        if c < len(data[0]) - 1 and r > 0 and data[r][c] == data[r - 1][c + 1]:
            sidesMatched.append("rc")

        if len(regionsMatched) == 0:
            return sidesMatched, None

        if len(set(regionsMatched)) > 1:
            mergeRegions(regionsMatched[0], regionsMatched[1])

        return sidesMatched, regionsMatched[0]

    for r in range(len(data)):
        for c in range(len(data[r])):
            sidesMatched, region = matchRegion(r, c)
            if region is not None:
                plotToRegion[(r, c)] = region
                regions[region][1] += 1

                if sidesMatched == ["t", "l"] or sidesMatched == ["t", "l", "lc"]:
                    regions[region][2] -= 2
                elif (
                    sidesMatched == ["t", "lc"]
                    or sidesMatched == ["l", "lc"]
                    or sidesMatched == ["t", "rc"]
                ):
                    regions[region][2] += 2
                elif sidesMatched == ["t", "lc", "rc"]:
                    regions[region][2] += 4
                elif sidesMatched == ["l", "lc", "rc"]:
                    regions[region][2] += 2
                # else:
                #   print('unmatched', sidesMatched)
            else:
                regions.append([data[r][c], 1, 4])
                plotToRegion[(r, c)] = len(regions) - 1

    # for region in regions:
    #   print(*region)
    # for p in plotToRegion:
    #   print(p, plotToRegion[p])
    return sum([a * p for t, a, p in regions])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
