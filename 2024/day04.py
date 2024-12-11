#!/usr/bin/env python3

def readInput(fileName: str) -> list[list[str]]:
  with open(fileName, "r") as f:
    return [list(x.strip()) for x in f.readlines()]

  return []

def checkXmas(l: list[str]) -> int:
  s = ''.join(l)
  # print(s, end=', ')
  return 1 if s == 'XMAS' or s == 'SAMX' else 0
    

def checkHorizontal(input: list[list[str]], r: int, c: int) -> int:
  if (c >= len(input[r]) - 3):
    return 0
  # print('h', end=' ')
  return checkXmas([input[r][c],input[r][c+1],input[r][c+2],input[r][c+3]])
  # return 0

def checkVertical(input: list[list[str]], r: int, c: int) -> int:
  if (r >= len(input) - 3):
    return 0
  # print('v', end=' ')
  return checkXmas([input[r][c],input[r+1][c],input[r+2][c],input[r+3][c]])
  # return 0

def checkDiagonalDown(input: list[list[str]], r: int, c: int) -> int:
  if (r >= len(input) - 3):
    return 0
  if (c >= len(input[r]) - 3):
    return 0
  # print('dd', end=' ')
  return checkXmas([input[r][c],input[r+1][c+1],input[r+2][c+2],input[r+3][c+3]])
  # return 0

def checkDiagonalUp(input: list[list[str]], r: int, c: int) -> int:
  if (r < 3):
    return 0
  if (c >= len(input[r]) - 3):
    return 0
  # print('du', end=' ')
  return checkXmas([input[r][c],input[r-1][c+1],input[r-2][c+2],input[r-3][c+3]])
  # return 0

def part1(input: list[list[str]]) -> int:
  count = 0
  for r in range(len(input)):
    for c in range(len(input[0])):
      result = checkHorizontal(input, r, c) + checkVertical(input, r, c) + checkDiagonalDown(input, r, c) + checkDiagonalUp(input, r, c)
      count += result
      # print(count, r,c,result)

  return count

def checkMas(l: list[str]) -> int:
  s = ''.join(l)
  # print(s, end=', ')
  return 1 if s == 'MAS' or s == 'SAM' else 0

def part2(input: list[list[str]]) -> int:
  count = 0
  for r in range(len(input)):
    for c in range(len(input[0])):
      if r < 1 or r >= len(input) -1 or c < 1 or c >= len(input[r]) - 1:
        continue
      count += 1 if checkMas([input[r-1][c-1], input[r][c], input[r+1][c+1]]) and checkMas([input[r+1][c-1], input[r][c], input[r-1][c+1]]) else 0
  return count

if __name__ == "__main__":
    input = readInput("input.txt")

    print("part 1:", part1(input))
    print("part 2:", part2(input))
