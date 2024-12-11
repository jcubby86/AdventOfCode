#!/usr/bin/env python3

from itertools import groupby
from operator import itemgetter
import collections

def readInput(fileName: str):
  with open(fileName, "r") as f:
    input = [x.strip() for x in f.readlines()]
    index = input.index('')

    rules = collections.defaultdict(list)
    for k, v in [s.split('|') for s in input[:index]]:
      rules[int(k)].append(int(v))

    return rules, [list(map(int, s.split(','))) for s in input[index+1:]]

  return []

def checkUpdate(rules, update):
  indices = {number: i for i, number in enumerate(update)}

  for k in rules:
    if k not in indices:
      continue
    for v in rules[k]:
      if v not in indices:
        continue
      if indices[k] > indices[v]: return False
  return True

def fixUpdate(rules, update):
  remaining = set(update)
  newRules = collections.defaultdict(set)
  for k in rules:
    if k in remaining:
      newRules[k] = set([v for v in rules[k] if v in remaining])
      
  result = []
  while len(remaining) > 0:
    result += [n for n in remaining if len(newRules[n].intersection(remaining)) < 1]
    remaining.difference_update(set(result))
  return result

def part1(rules, updates):
  total = 0
  for update in updates:
    if checkUpdate(rules, update):
      total += update[len(update)//2]
  return total

def part2(rules, updates):
  total = 0
  for update in updates:
    if not checkUpdate(rules, update):
      result = fixUpdate(rules, update)
      total += result[len(result)//2]
  return total

if __name__ == "__main__":
    input = readInput("input.txt")

    print("part 1:", part1(*input))
    print("part 2:", part2(*input))
