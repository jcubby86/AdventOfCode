#!/usr/bin/env python3

from collections import defaultdict, deque
import sys
from functools import cache


def readData(fileName: str) -> list[int]:
    with open(fileName, "r") as f:
        return [int(x.strip()) for x in f.readlines()]
    return []


@cache
def process(secret: int) -> int:
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret


@cache
def mix(secret: int, other: int) -> int:
    return secret ^ other


def prune(secret: int) -> int:
    return secret % 16777216


def getTotalBananas(d: dict) -> int:
    return sum([k * d[k] for k in d])


def solve(data: list[int]) -> tuple[int, int]:
    p1 = 0
    counts: dict = defaultdict(lambda: defaultdict(lambda: 0))
    for monkey in data:
        visited = defaultdict(lambda: 0)
        secrets: deque[int] = deque()
        secrets.append(monkey)
        for i in range(2000):
            secrets.append(process(secrets[-1]))

            if len(secrets) == 5:
                ones = [secrets[j] % 10 for j in range(5)]
                diffs = tuple([ones[j] - ones[j - 1] for j in range(1, 5)])

                if diffs not in visited:
                    visited[diffs] = ones[-1]
                    counts[diffs][ones[-1]] += 1

                secrets.popleft()
        p1 += secrets[-1]

    return p1, max([getTotalBananas(counts[k]) for k in counts])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    p1, p2 = solve(data)

    print("part 1:", p1)
    print("part 2:", p2)
