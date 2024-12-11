#!/usr/bin/env python3

def readInput(fileName: str) -> list[str]:
  with open(fileName, "r") as f:
    return [x.strip() for x in f.readlines()]

  return []

def part1(input: list[str]):
  pass

def part2(input: list[str]):
  pass

if __name__ == "__main__":
    input = readInput("input.txt")

    print("part 1:", part1(input))
    print("part 2:", part2(input))
