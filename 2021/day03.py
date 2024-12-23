#!/usr/bin/env python3

import sys


def readData(fileName: str) -> list[str]:
    with open(fileName, "r") as f:
        data = [x.strip() for x in f.readlines()]
        return data
    return []


def part1(data):
    check = [[0, 0] for _ in data[0]]
    for num in data:
        for i, bit in enumerate(num):
            check[i][int(bit)] += 1

    gamma = ""
    epsilon = ""
    for i in check:
        gamma += "0" if i[0] > i[1] else "1"
        epsilon += "0" if i[0] < i[1] else "1"

    print(int(gamma, 2) * int(epsilon, 2))


def part2(data):
    oxy = data
    for i in range(len(data[0])):
        bit = [0, 0]
        for num in oxy:
            bit[int(num[i])] += 1
        oxy2 = []
        for num in oxy:
            if bit[0] > bit[1] and num[i] == "0":
                oxy2.append(num)
            elif bit[0] <= bit[1] and num[i] == "1":
                oxy2.append(num)
        oxy = oxy2
        if len(oxy) == 1:
            break

    co = data
    for i in range(len(data[0])):
        bit = [0, 0]
        for num in co:
            bit[int(num[i])] += 1
        co2 = []
        for num in co:
            if bit[0] > bit[1] and num[i] == "1":
                co2.append(num)
            elif bit[0] <= bit[1] and num[i] == "0":
                co2.append(num)
        co = co2
        if len(co) == 1:
            break
    intoxy = int(oxy[0], 2)
    intco = int(co[0], 2)
    print(intoxy, intco, intoxy * intco)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
