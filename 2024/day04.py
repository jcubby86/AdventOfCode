#!/usr/bin/env python3


def readData(fileName: str) -> list[list[str]]:
    with open(fileName, "r") as f:
        return [list(x.strip()) for x in f.readlines()]

    return []


def checkXmas(l: list[str]) -> int:
    s = "".join(l)
    # print(s, end=', ')
    return 1 if s == "XMAS" or s == "SAMX" else 0


def checkHorizontal(data: list[list[str]], r: int, c: int) -> int:
    if c >= len(data[r]) - 3:
        return 0
    # print('h', end=' ')
    return checkXmas([data[r][c], data[r][c + 1], data[r][c + 2], data[r][c + 3]])
    # return 0


def checkVertical(data: list[list[str]], r: int, c: int) -> int:
    if r >= len(data) - 3:
        return 0
    # print('v', end=' ')
    return checkXmas([data[r][c], data[r + 1][c], data[r + 2][c], data[r + 3][c]])
    # return 0


def checkDiagonalDown(data: list[list[str]], r: int, c: int) -> int:
    if r >= len(data) - 3:
        return 0
    if c >= len(data[r]) - 3:
        return 0
    # print('dd', end=' ')
    return checkXmas(
        [data[r][c], data[r + 1][c + 1], data[r + 2][c + 2], data[r + 3][c + 3]]
    )
    # return 0


def checkDiagonalUp(data: list[list[str]], r: int, c: int) -> int:
    if r < 3:
        return 0
    if c >= len(data[r]) - 3:
        return 0
    # print('du', end=' ')
    return checkXmas(
        [data[r][c], data[r - 1][c + 1], data[r - 2][c + 2], data[r - 3][c + 3]]
    )
    # return 0


def part1(data: list[list[str]]) -> int:
    count = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            result = (
                checkHorizontal(data, r, c)
                + checkVertical(data, r, c)
                + checkDiagonalDown(data, r, c)
                + checkDiagonalUp(data, r, c)
            )
            count += result
            # print(count, r,c,result)

    return count


def checkMas(l: list[str]) -> int:
    s = "".join(l)
    # print(s, end=', ')
    return 1 if s == "MAS" or s == "SAM" else 0


def part2(data: list[list[str]]) -> int:
    count = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            if r < 1 or r >= len(data) - 1 or c < 1 or c >= len(data[r]) - 1:
                continue
            count += (
                1
                if checkMas([data[r - 1][c - 1], data[r][c], data[r + 1][c + 1]])
                and checkMas([data[r + 1][c - 1], data[r][c], data[r - 1][c + 1]])
                else 0
            )
    return count


if __name__ == "__main__":
    data = readData("data.txt")

    print("part 1:", part1(data))
    print("part 2:", part2(data))
