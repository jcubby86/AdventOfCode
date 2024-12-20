#!/usr/bin/env python3

import sys


def readData(fileName: str) -> list[str]:
    with open(fileName, "r") as f:
        return [x.strip() for x in f.readlines()]
    return []


def tokenize(s):
    tokens = []
    for c in s:
        if c == "[" or c == "]" or c == ",":
            tokens.append(c)
        else:
            tokens.append(int(c))
    return tokens


def reduceTokens(tokens):
    depth = 0
    for i in range(len(tokens)):
        if tokens[i] == "[":
            depth += 1
        elif tokens[i] == "]":
            depth -= 1
        elif depth == 5:
            left = tokens[i]
            right = tokens[i + 2]
            for j in range(i - 1, -1, -1):
                if isNum(tokens[j]):
                    tokens[j] += left
                    break
            for j in range(i + 3, len(tokens)):
                if isNum(tokens[j]):
                    tokens[j] += right
                    break
            for j in range(5):
                tokens.pop(i - 1)
            tokens.insert(i - 1, 0)
            return True
    depth = 0
    for i in range(len(tokens)):
        if tokens[i] == "[":
            depth += 1
        elif tokens[i] == "]":
            depth -= 1
        elif isNum(tokens[i]) and tokens[i] >= 10:
            num = tokens[i]
            tokens.pop(i)
            tokens.insert(i, "]")
            tokens.insert(i, (num + 1) // 2)
            tokens.insert(i, ",")
            tokens.insert(i, num // 2)
            tokens.insert(i, "[")
            return True
    return False


def isNum(c):
    return c != "[" and c != "]" and c != ","


def printTokens(tokens):
    for token in tokens:
        print(token, end="")
    print()


def magnitude(tokens):
    if isNum(tokens[0]):
        return tokens.pop(0)
    if tokens[0] == "[":
        tokens.pop(0)
        left = 3 * magnitude(tokens)
        tokens.pop(0)
        right = 2 * magnitude(tokens)
        tokens.pop(0)
        return left + right


def part1(data):
    start = tokenize(data[0])
    for i in range(1, len(data)):
        tokens = tokenize(data[i])
        start = ["["] + start + [","] + tokens + ["]"]
        printTokens(start)
        while reduceTokens(start):
            printTokens(start)
    print(magnitude(start))


def part2(data):
    maximum = 0
    for i, first in enumerate(data):
        for j, second in enumerate(data):
            if i != j:
                tokens = ["["] + tokenize(first) + [","] + tokenize(second) + ["]"]
                while reduceTokens(tokens):
                    continue
                mag = magnitude(tokens)
                if mag > maximum:
                    maximum = mag
    print(maximum)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
