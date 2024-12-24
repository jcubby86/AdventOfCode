#!/usr/bin/env python3

from functools import cache
import sys
from collections import deque


def readData(fileName: str) -> tuple[list, list]:
    with open(fileName, "r") as f:
        v, r = f.read().split("\n\n")
        values = [x.split(": ") for x in v.split("\n")]
        rules = [x.split() for x in r.split("\n")]
        return values, rules

    return []


def executeRules(values, rules):
    while len(rules) > 0:
        r = rules.popleft()
        if r[0] not in values or r[2] not in values:
            rules.append(r)
            continue

        if r[1] == "AND":
            values[r[4]] = values[r[0]] & values[r[2]]
        elif r[1] == "OR":
            values[r[4]] = values[r[0]] | values[r[2]]
        elif r[1] == "XOR":
            values[r[4]] = values[r[0]] ^ values[r[2]]


def getIntValue(values: dict, prefix: str) -> int:
    f = sorted(
        [(k, v) for k, v in values.items() if k[0] == prefix],
        key=lambda x: int(x[0][1:]),
    )
    return int("".join([str(x[1]) for x in f[::-1]]), 2)


def getBitValues(value: int) -> str:
    return f"{value:050b}"


def part1(initialValues: list, rules: list) -> int:
    values = {k: int(v) for k, v in initialValues} 
    executeRules(values, deque(rules))
    return getIntValue(values, "z")


def part2(initialValues: list, rules: list):
    ruleDict = {x[4]: x for x in rules}
    values = {k: int(v) for k, v in initialValues} 

    @cache
    def getDependencies(key: str) -> set[str]:
        d: set[str] = set()
        if key not in ruleDict:
            return d

        rule = ruleDict[key]
        d.add(rule[0])
        d.update(getDependencies(rule[0]))
        d.add(rule[2])
        d.update(getDependencies(rule[2]))

        return d
    
    def executeRule(key: str):
        r = ruleDict[key]

        if r[0] not in values:
            executeRule(r[0])
        if r[2] not in values:
            executeRule(r[2])
        if r[1] == "AND":
            values[r[4]] = values[r[0]] & values[r[2]]
        elif r[1] == "OR":
            values[r[4]] = values[r[0]] | values[r[2]]
        elif r[1] == "XOR":
            values[r[4]] = values[r[0]] ^ values[r[2]]
    


    x = getIntValue(values, "x")
    y = getIntValue(values, "y")
    expected = getBitValues(x + y)

    for i in range(50):
        key = f"z{i:02d}"
        e = int(expected[-i - 1])
        if key not in ruleDict:
            break
        executeRule(key)
        if e != values[key]:
            print(f"key: {key}, expected: {e}, actual: {values[key]}")
            print(getDependencies(key).difference(getDependencies(f"z{(i-1):02d}")))
    # from here it's a manual process, but this helps narrow down the wires that could be crossed.
    # make sure that z00 is the XOR of (x00 XOR y00) and the wire that's "carrying" the 1 from before


    return expected


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    values, rules = readData(sys.argv[1])

    print("part 1:", part1(values, rules))
    print("part 2:", part2(values, rules))
