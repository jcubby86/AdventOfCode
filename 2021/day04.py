#!/usr/bin/env python3

import sys


def readData(fileName: str):
    with open(fileName, "r") as f:
        data = [x.strip() for x in f.readlines()]
        turns = [int(x) for x in data[0].split(",")]
        boards = []

        for i in range(2, len(data), 6):
            board = []
            for j in range(i, i + 5):
                board.append([int(x) for x in data[j].split()])
            boards.append(board)

        return turns, boards
    return []


def part1(data):
    turns = data[0]
    boards = data[1]
    print(boards)

    for turn in turns:
        for board in boards:
            for row in board:
                for j, val in enumerate(row):
                    if val == turn:
                        row[j] = 1000 + val
            if checkBoard(board):
                print(countBoard(board) * turn)
                return


def part2(data):
    turns = data[0]
    boards = data[1]
    print(boards)
    s = set()

    for turn in turns:
        for i, board in enumerate(boards):
            for row in board:
                for j, val in enumerate(row):
                    if val == turn:
                        row[j] = 1000 + val
            if checkBoard(board):
                s.add(i)
                if len(s) == len(boards):
                    print(countBoard(board) * turn)
                    return


def checkBoard(board):
    for i in range(5):
        row = True
        col = True
        for j in range(5):
            row = row and board[i][j] >= 1000
            col = col and board[j][i] >= 1000
        if row or col:
            return True
    return False


def countBoard(board):
    sum = 0
    for row in board:
        for val in row:
            if val < 1000:
                sum += val
    return sum


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
