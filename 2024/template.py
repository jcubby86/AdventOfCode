#!/usr/bin/env python3

import sys

def readInput(fileName: str) -> list[str]:
  with open(fileName, "r") as f:
    return [x.strip() for x in f.readlines()]
  return []

def part1(input: list[str]):
  return input

def part2(input: list[str]):
  pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
      print("missing file name")
      exit(1)

    input = readInput(sys.argv[1])

    print("part 1:", part1(input))
    print("part 2:", part2(input))
