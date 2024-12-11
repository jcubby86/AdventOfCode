#!/usr/bin/env python3

def readInput(fileName: str):
  with open(fileName, "r") as f:
    return [list(map(int, x.strip().split())) for x in f.readlines()]

  return []

def getSign(n: int):
  return 1 if n > 0 else -1

def getDiffs(level):
  return [level[i] - level[i - 1] for i in range(1, len(level))]

def check1(level):
  diffs = getDiffs(level)
  sign = getSign(diffs[0])
  return all([(getSign(diff) == sign) and abs(diff) <= 3 and abs(diff) >= 1 for diff in diffs])

def check2(level):
  for i in range(len(level)):
    if check1(level[:i] + level[i+1:]):
      return True
  return False

def part1(levels):
  return len(list(filter(lambda x: x, map(check1, levels))))

def part2(levels):
  return len(list(filter(lambda x: x, map(check2, levels))))

if __name__ == "__main__":
    input = readInput("input.txt")

    print("part 1:", part1(input))
    print("part 2:", part2(input))
