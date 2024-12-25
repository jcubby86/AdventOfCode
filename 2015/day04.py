#!/usr/bin/env python3

import sys
import hashlib


def readData(fileName: str) -> str:
    with open(fileName, "r") as f:
        return f.read().strip()
    return ''

def part1(data: str, count):
    i = 1
    while True:
        m = hashlib.md5(data.encode())
        m.update(str(i).encode())
        s = m.hexdigest()

        if s[0:count] == '0'*count:
            return i

        i += 1


    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data, 5))
    print("part 2:", part1(data, 6))
