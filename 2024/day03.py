#!/usr/bin/env python3

import re
import sys


def parseGroup(mul, x, y, do, dont):
    if mul != "":
        return ("mul", int(x), int(y))
    elif do != "":
        return ("do", 0, 0)
    elif dont != "":
        return ("don't", 0, 0)


def readData(fileName: str):
    with open(fileName, "r") as f:
        return list(
            map(
                lambda x: parseGroup(*x),
                re.findall(
                    "(mul)\\((\\d{1,3}),(\\d{1,3})\\)|(do)\\(\\)|(don't)\\(\\)",
                    f.read(),
                ),
            )
        )

    return []


def part1(data):
    return sum([int(x) * int(y) for type, x, y in data if type == "mul"])


def part2(data):
    enabled = True
    total = 0
    for type, x, y in data:
        if type == "do":
            enabled = True
        elif type == "don't":
            enabled = False
        elif type == "mul" and enabled:
            total += int(x) * int(y)
    return total


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
