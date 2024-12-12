#!/usr/bin/env python3

import math
import sys


def readInput(fileName: str) -> list[int]:
    with open(fileName, "r") as f:
        return list(map(int, f.read().strip().split(" ")))
    return []


def rules(number):

    if number == 0:
        return [1]

    string = str(number)
    if len(string) % 2 == 0:
        left = string[: len(string) // 2]
        right = string[len(string) // 2 :]

        return [int(left), int(right)]

    return [number * 2024]


def part1(input: list[int], count: int):
    arr = [x for x in input]
    for i in range(count):
        res = []
        for num in arr:
            for x in rules(num):
                res.append(x)
        arr = res

    return len(arr)


def part2(input: list[int], count: int):

    def calc(x, l):
        s = str(x)
        if l == 0:
            return 1
        if x in mem[l]:
            return mem[l][x]
        if x == 0:
            mem[l][x] = calc(1, l - 1)
        elif len(s) % 2 == 0:
            mid = len(s) // 2
            mem[l][x] = calc(int(s[:mid]), l - 1) + calc(int(s[mid:]), l - 1)
        else:
            mem[l][x] = calc(x * 2024, l - 1)
        return mem[l][x]

    mem = [{} for i in range(count + 1)]

    return sum([calc(x, count) for x in input])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing arg")
        exit(1)

    input = readInput(sys.argv[1])

    print("part 1:", part1(input, 25))
    print("part 2:", part2(input, 75))
