#!/usr/bin/env python3

from typing import Callable
from itertools import product


def readData(fileName: str) -> list[tuple[int, list[int]]]:
    with open(fileName, "r") as f:
        return [
            (int(k), list(map(int, v.split(" "))))
            for k, v in [y.strip().split(": ") for y in f.readlines()]
        ]
    return []


def check1(operators, target: int, numbers: list[int]) -> bool:
    for ops in product(operators, repeat=(len(numbers) - 1)):
        result = numbers[0]
        for i in range(len(ops)):
            if ops[i] == "+":
                result += numbers[i + 1]
            elif ops[i] == "*":
                result *= numbers[i + 1]
            elif ops[i] == "||":
                result = int(str(result) + str(numbers[i + 1]))
        if result == target:
            return True
    return False


def part1(data: list[tuple[int, list[int]]]) -> int:
    return sum(
        [target for target, numbers in data if check1(["+", "*"], target, numbers)]
    )


def part2(data):
    return sum(
        [
            target
            for target, numbers in data
            if check1(["+", "*", "||"], target, numbers)
        ]
    )


if __name__ == "__main__":
    data = readData("data.txt")
    print(len(data))

    print("part 1:", part1(data))
    print("part 2:", part2(data))
