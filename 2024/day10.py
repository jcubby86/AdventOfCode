#!/usr/bin/env python3

import sys
from collections import defaultdict

dirs = [(0,1), (0,-1), (1,0), (-1,0)]

def readInput(fileName: str) -> list[list[int]]:
  with open(fileName, "r") as f:
    return [list(map(int, list(x.strip()))) for x in f.readlines()]
  return []

def getVal(input: list[list[int]], pos: tuple[int, int]):
  if pos[0] >= 0 and pos[0] < len(input) and pos[1] >=0 and pos[1] < len(input[0]):
    r, c = pos
    return input[r][c]
  else:
    return None

def countNines(input: list[list[int]], paths: defaultdict[tuple[int, int], set], current: tuple[int, int]) -> set:
  reachableNines = set()

  val = getVal(input, current)
  if val is None:
    return reachableNines
  
  for dr,dc in dirs:
    next = current[0] + dr, current[1] + dc
    if getVal(input, next) == val + 1:
      reachableNines.update(paths[next])
  return reachableNines

def countPaths(input: list[list[int]], paths: defaultdict[tuple[int, int], int], current: tuple[int, int]) -> int:
  reachableNines = 0

  val = getVal(input, current)
  if val is None:
    return reachableNines
  
  for dr,dc in dirs:
    next = current[0] + dr, current[1] + dc
    if getVal(input, next) == val + 1:
      reachableNines += paths[next]
  return reachableNines

def getNines(input: list[list[int]]):
  spots: defaultdict[int, set[tuple[int, int]]] = defaultdict(set)
  paths: defaultdict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set)

  for i in range(9, -1, -1):
    for r in range(len(input)):
      for c in range(len(input[r])):
        val = getVal(input, (r, c))
        if i == 9 and val == i:
          spots[9].add((r, c))
          paths[(r, c)].add((r, c))
        elif val == i:
          nines = countNines(input, paths, (r, c))
          spots[i].add((r, c))
          paths[(r, c)].update(nines)
  
  return sum([len(paths[pos]) for pos in spots[0] ])

def getPaths(input: list[list[int]]):
  spots: defaultdict[int, set[tuple[int, int]]] = defaultdict(set)
  paths: defaultdict[tuple[int, int], int] = defaultdict(lambda: 0)

  for i in range(9, -1, -1):
    for r in range(len(input)):
      for c in range(len(input[r])):
        val = getVal(input, (r, c))
        if i == 9 and val == i:
          spots[9].add((r, c))
          paths[(r, c)] = 1
        elif val == i:
          count = countPaths(input, paths, (r, c))
          spots[i].add((r, c))
          paths[(r, c)] = count
  
  return sum([paths[pos] for pos in spots[0] ])

def part1(input):
  return getNines(input)

def part2(input):
  return getPaths(input)

if __name__ == "__main__":
    if len(sys.argv) < 2:
      print("missing file name")
      exit(1)

    input = readInput(sys.argv[1])

    print("part 1:", part1(input))
    print("part 2:", part2(input))
