#!/usr/bin/env python3

from collections import defaultdict
import sys

LEFT_BOX = "["
RIGHT_BOX = "]"
BOX = "O"
WALL = "#"
EMPTY = "."
ROBOT = "@"

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"

dirs = {LEFT: (0, -1), RIGHT: (0, 1), UP: (-1, 0), DOWN: (1, 0)}


def readData(fileName: str) -> tuple[list[list[str]], list[str]]:
    with open(fileName, "r") as f:
        warehouse, moves = f.read().split("\n\n")
    return [list(line) for line in warehouse.split("\n")], [
        c for c in moves if c != "\n"
    ]


def printWarehouse(warehouse):
    for row in warehouse:
        print("".join(row))


def findRobot(warehouse) -> tuple[int, int]:
    for r in range(len(warehouse)):
        for c in range(len(warehouse[0])):
            if warehouse[r][c] == ROBOT:
                return (r, c)
    return (-1, -1)


def part1(original: list[list[str]], moves: list[str]) -> int:
    warehouse = [list("".join(row)) for row in original]

    def tryMoveBox(r, c, dir) -> bool:
        if warehouse[r][c] == EMPTY:
            return True
        elif warehouse[r][c] == BOX:
            if tryMoveBox(r + dir[0], c + dir[1], dir):
                warehouse[r][c] = EMPTY
                warehouse[r + dir[0]][c + dir[1]] = BOX
                return True
        return False

    # print("Initial state:")
    # printWarehouse(original)

    robot = findRobot(warehouse)
    for move in moves:
        dir = dirs[move]
        r, c = robot[0] + dir[0], robot[1] + dir[1]

        if tryMoveBox(r, c, dir):
            warehouse[robot[0]][robot[1]] = EMPTY
            robot = (r, c)
            warehouse[robot[0]][robot[1]] = ROBOT
        # print()
        # print("Move", move)
        # printWarehouse(warehouse)

    count = 0
    for r in range(len(warehouse)):
        for c in range(len(warehouse[0])):
            if warehouse[r][c] == "O":
                count += (r * 100) + c

    return count


def part2(original: list[list[str]], moves: list[str]) -> int:
    for r in range(len(original)):
        row = original[r]
        for c in range(len(row)):
            if row[c] == WALL:
                row[c] = WALL + WALL
            if row[c] == BOX:
                row[c] = LEFT_BOX + RIGHT_BOX
            if row[c] == EMPTY:
                row[c] = EMPTY + EMPTY
            if row[c] == ROBOT:
                row[c] = ROBOT + EMPTY
        original[r] = list("".join(row))

    warehouse = [list("".join(row)) for row in original]

    def tryMoveBox(r, c, move: str) -> bool:
        if warehouse[r][c] == EMPTY:
            return True
        elif warehouse[r][c] == LEFT_BOX or warehouse[r][c] == RIGHT_BOX:
            if move == LEFT:
                if tryMoveBox(r, c - 2, move):
                    warehouse[r][c - 2] = LEFT_BOX
                    warehouse[r][c - 1] = RIGHT_BOX
                    warehouse[r][c] = EMPTY
                    return True
            elif move == RIGHT:
                if tryMoveBox(r, c + 2, move):
                    warehouse[r][c] = EMPTY
                    warehouse[r][c + 1] = LEFT_BOX
                    warehouse[r][c + 2] = RIGHT_BOX
                    return True
            elif move == UP or move == DOWN:
                dir = dirs[move]
                nr = r + dir[0]
                if warehouse[r][c] == LEFT_BOX:
                    if tryMoveBox(nr, c, move) and tryMoveBox(nr, c + 1, move):
                        warehouse[nr][c] = LEFT_BOX
                        warehouse[nr][c + 1] = RIGHT_BOX
                        warehouse[r][c] = EMPTY
                        warehouse[r][c + 1] = EMPTY
                        return True
                elif warehouse[r][c] == RIGHT_BOX:
                    if tryMoveBox(nr, c - 1, move) and tryMoveBox(nr, c, move):
                        warehouse[nr][c - 1] = LEFT_BOX
                        warehouse[nr][c] = RIGHT_BOX
                        warehouse[r][c - 1] = EMPTY
                        warehouse[r][c] = EMPTY
                        return True
        return False

    # print("Initial state:")
    # printWarehouse(warehouse)

    robot = findRobot(warehouse)
    for move in moves:
        # print(move)
        dir = dirs[move]
        r, c = robot[0] + dir[0], robot[1] + dir[1]
        temp = [list("".join(row)) for row in warehouse]
        if tryMoveBox(r, c, move):
            warehouse[robot[0]][robot[1]] = EMPTY
            robot = (r, c)
            warehouse[robot[0]][robot[1]] = ROBOT
        else:
            warehouse = temp

        # print()
        # print("Move", move)
        # printWarehouse(warehouse)

    count = 0
    for r in range(len(warehouse)):
        for c in range(len(warehouse[r])):
            if warehouse[r][c] == LEFT_BOX:
                count += (r * 100) + c

    return count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(*data))
    print("part 2:", part2(*data))
