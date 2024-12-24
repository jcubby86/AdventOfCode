#!/usr/bin/env python3

import sys
import re
from collections import deque

def readData(fileName: str) -> tuple:
    with open(fileName, "r") as f:
        values, rules = f.read().split("\n\n")
        
        return [tuple(x.split(": ")) for x in values.split("\n")], deque([x.split() for x in rules.split("\n")])
    return []


def part1(values: list[tuple], rules: deque[tuple]) -> int:
    lookup = {}

    for k, v in values:
        lookup[k] = int(v)

    while len(rules) > 0:
        r = rules.popleft()
        if r[0] not in lookup or r[2] not in lookup:
            rules.append(r)
            continue

        if r[1] == 'AND':
            lookup[r[4]] = lookup[r[0]] & lookup[r[2]]
        elif r[1] == 'OR':
            lookup[r[4]] = lookup[r[0]] | lookup[r[2]]
        elif r[1] == 'XOR':
            lookup[r[4]] = lookup[r[0]] ^ lookup[r[2]]

    f = sorted([(k, v) for k, v in lookup.items() if k[0] == 'z'], key=lambda x: int(x[0][1:]))

    return int(''.join([str(x[1]) for x in f[::-1]]), 2)


def part2(data):
    pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(*data))
    print("part 2:", part2(data))
