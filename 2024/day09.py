#!/usr/bin/env python3

import sys

def readInput(fileName: str) -> str:
    with open(fileName, "r") as f:
        return f.read().strip()

    return ""


def part1(input: str):
    arr = []
    for i in range(len(input)):
        if i % 2 == 0:
            arr += [i // 2] * int(input[i])
        else:
            arr += ["."] * int(input[i])

    l, r = 0, len(arr) - 1

    while l < r:
        if arr[l] == "." and arr[r] != ".":
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        elif arr[l] == ".":
            r -= 1
        else:
            l += 1
    return sum([i * x for i, x in enumerate(arr) if isinstance(x, int)])


def part2(input: str):
    arr: list[tuple[int, int]] = []
    for i in range(len(input)):
        if i % 2 == 0:
            arr.append((i//2, int(input[i])))
        else:
            arr.append((-1, int(input[i])))

    r = len(arr) - 1
    while r > 0:
        # print(''.join([(str(block) if block != -1 else '.') * blockSize for block, blockSize in arr ]))

        l = 0
        while l < r:
            free, freeSize, = arr[l]
            block, blockSize = arr[r]
            if block == -1:
                break
            elif free != -1:
                l += 1
            elif blockSize == freeSize:
                arr[l], arr[r] = arr[r], arr[l]
                break
            elif blockSize < freeSize:
                arr[r] = (-1, blockSize)
                arr[l] = (block, blockSize)
                arr.insert(l+1, (-1, freeSize - blockSize))
                break
            else:
                l += 1
        r -= 1
    arr2 = sum([[block] * blockSize for block, blockSize in arr], [])
    return sum([i * int(x) for i, x in enumerate(arr2) if x != -1])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        exit(1)

    input = readInput(sys.argv[1])

    print("part 1:", part1(input))
    print("part 2:", part2(input))
