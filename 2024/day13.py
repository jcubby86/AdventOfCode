#!/usr/bin/env python3

import sys

import re

def safe(x):
  if x is None:
    raise Exception()
  return x

def readInput(fileName: str) -> list[tuple[int, int]]:
  with open(fileName, "r") as f:
    lines = [x.strip() for x in f.readlines()]
    claws = []
    for i in range(0, len(lines), 4):
      a = safe(re.fullmatch('Button A: X\+(\d+), Y\+(\d+)', lines[i])).groups()
      b = safe(re.fullmatch('Button B: X\+(\d+), Y\+(\d+)', lines[i + 1])).groups(1)
      p = safe(re.fullmatch("Prize: X=(\d+), Y=(\d+)", lines[i+2])).groups()
      claws.append(list([tuple(map(int, x)) for x in [a,b,p]]))
    return claws
  return []

def checkClaw(a, b, prize):
  ax, ay = a
  bx, by = b
  px, py = prize
  # px, py = px + 10000000000000, py + 10000000000000

  aPresses, bPresses = {}, {}

  cx, cy, i = 0, 0, 0
  while cx < px and cy < py:
    cx, cy, i = cx + ax, cy + ay, i + 1
    aPresses[(cx, cy)] = i

  cx, cy, i = 0, 0, 0
  while cx < px and cy < py:
    cx, cy, i = cx + bx, cy + by, i + 1
    bPresses[(cx, cy)] = i
  
  options = set()

  for c in aPresses:
    cx, cy = c
    if (px - cx, py - cy) in bPresses:
      options.add((aPresses[c] * 3) + bPresses[(px - cx, py - cy)])
  for c in bPresses:
    cx, cy = c
    if (px - cx, py - cy) in aPresses:
      options.add((aPresses[(px - cx, py - cy)] * 3) + bPresses[c])

  return min(options) if len(options) > 0 else 0

def part1(input):
  return sum([checkClaw(*claw) for claw in input])

def part2(input):
  pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
      print("missing file name")
      exit(1)

    input = readInput(sys.argv[1])

    print("part 1:", part1(input))
    print("part 2:", part2(input))
