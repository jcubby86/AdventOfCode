#!/usr/bin/env python3

import sys

vowels = set("aeiou")
disallowed = set(["ab", "cd", "pq", "xy"])


def readData(fileName: str) -> list[str]:
    with open(fileName, "r") as f:
        return [x.strip() for x in f.readlines()]
    return []


def part1(data: list[str]):
    def checkNice(s):
        vowelCount = 0
        requiredSubstring = False

        for i, c in enumerate(s):
            if c in vowels:
                vowelCount += 1
            if i > 0:
                if s[i - 1 : i + 1] in disallowed:
                    return False
                if s[i - 1] == c:
                    requiredSubstring = True
        return vowelCount > 2 and requiredSubstring

    return len(list(filter(checkNice, data)))


def part2(data: list[str]):
    def checkNice(s):
        rule1 = False
        rule2 = False

        rule1Candidates = {}

        for i, c in enumerate(s):
            if i > 0:
                sub2 = s[i - 1 : i + 1]
                if sub2 in rule1Candidates and i >= rule1Candidates[sub2] + 2:
                    rule1 = True
                elif sub2 not in rule1Candidates:
                    rule1Candidates[sub2] = i
            if i > 1 and s[i - 2] == c:
                rule2 = True
        return rule1 and rule2

    return len(list(filter(checkNice, data)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
