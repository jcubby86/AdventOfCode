#!/usr/bin/env python3

import collections

dirs = [(-1,0), (0,1), (1, 0), (0, -1)]

def readInput(fileName: str) -> list[list[str]]:
  with open(fileName, "r") as f:
    return [list(x.strip()) for x in f.readlines()]
  return []

def move(pos, currentDir) -> tuple[int, int]:
  r, c = pos
  direction = dirs[currentDir]
  return r + direction[0], c + direction[1]

def turn(currentDir):
  return (currentDir + 1) % len(dirs)

def traverse(input, startPos):
  visited: dict[tuple[int, int], set[int]] = collections.defaultdict(set)
  pos: tuple[int, int] = startPos
  currentDir = 0

  while getLocation(input, pos) is not None and not(pos in visited and currentDir in visited[pos]):
    visited[pos].add(currentDir)
    next = move(pos, currentDir)
    if (getLocation(input, next) == '#'): 
      currentDir = turn(currentDir)
    else:  
      pos = next
  return visited.keys(), getLocation(input, pos) is not None

def getLocation(input: list[list[str]], pos: tuple[int, int]) -> None | str:
  r,c = pos
  if r < 0 or r >= len(input) or c < 0 or c >= len(input[r]):
    return None
  else:
    return input[r][c]

def part1(input):
  width = len(input[0])
  startPos = [x for xs in input for x in xs ].index('^')
  visited, _ = traverse(input, (startPos//width, startPos%width))
  return len(visited)

def part2(input):
  width = len(input[0])
  startIndex = [x for xs in input for x in xs ].index('^')
  startPos = (startIndex//width, startIndex%width)
  visited, _ = traverse(input, startPos)

  count = 0
  for candidate in filter(lambda x: x != startPos, visited):
    r, c = candidate
    input[r][c] = '#'
    if traverse(input, startPos)[1]:
      count += 1
    input[r][c] = '.'
  return count

if __name__ == "__main__":
    print("part 1:", part1(readInput("input.txt")))
    print("part 2:", part2(readInput("input.txt")))