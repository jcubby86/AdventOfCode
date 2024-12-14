#!/usr/bin/env python3

import sys

import re
from fractions import Fraction


def readInput(fileName: str) -> list[list[int]]:
    with open(fileName, "r") as f:
        lines = [x for x in f.readlines()]
        return [
            list(map(int, re.findall("\\d+", "".join(lines[i : i + 3]))))
            for i in range(0, len(lines), 4)
        ]
    return []


def checkClaw(ax, ay, bx, by, px, py):
    af = Fraction((px * by) - (py * bx), (ax * by) - (ay * bx))
    bf = Fraction(px - (ax * af.numerator), bx)

    if af.denominator != 1 or bf.denominator != 1:
        return 0

    return (af.numerator * 3) + bf.numerator


def part1(input: list[list[int]]):
    return sum([checkClaw(*claw) for claw in input])


def part2(input: list[list[int]]):
    return sum(
        [
            checkClaw(ax, ay, bx, by, px + 10000000000000, py + 10000000000000)
            for ax, ay, bx, by, px, py in input
        ]
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        exit(1)

    input = readInput(sys.argv[1])

    print("part 1:", part1(input))
    print("part 2:", part2(input))
