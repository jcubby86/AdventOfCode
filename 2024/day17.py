#!/usr/bin/env python3

import re
import sys


def nextInstruction(registers):
    registers["ip"] += 2


def getCombo(registers, operand):
    if operand <= 3:
        return operand
    if operand == 4:
        return registers["a"]
    if operand == 5:
        return registers["b"]
    if operand == 6:
        return registers["c"]
    return 0


def adv(registers, operand):
    registers["a"] //= 2 ** getCombo(registers, operand)
    nextInstruction(registers)


def bxl(registers, operand):
    registers["b"] ^= operand
    nextInstruction(registers)


def bst(registers, operand):
    registers["b"] = getCombo(registers, operand) % 8
    nextInstruction(registers)


def jnz(registers, operand):
    if registers["a"] != 0:
        registers["ip"] = operand
    else:
        nextInstruction(registers)


def bxc(registers, operand):
    registers["b"] ^= registers["c"]
    nextInstruction(registers)


def out(registers, operand):
    registers["out"].append(getCombo(registers, operand) % 8)
    nextInstruction(registers)


def bdv(registers, operand):
    registers["b"] = registers["a"] // (2 ** getCombo(registers, operand))
    nextInstruction(registers)


def cdv(registers, operand):
    registers["c"] = registers["a"] // (2 ** getCombo(registers, operand))
    nextInstruction(registers)


def readData(fileName: str):
    with open(fileName, "r") as f:
        return list(map(int, re.findall("-?\\d+", f.read())))
    return []


def part1(data):
    operations = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
    registers = {"a": data[0], "b": data[1], "c": data[2], "ip": 0, "out": []}
    program = data[3:]

    while registers["ip"] < len(program):
        operation = operations[program[registers["ip"]]]
        operand = program[registers["ip"] + 1]
        operation(registers, operand)
        # print(re.match('<function (.+) at .+>', str(operation))[1], registers, operand)

    return registers["out"]


def getOut(a: int, data) -> int:
    data[0] = a
    result = part1(data)
    # print(",".join(map(str, result)))
    return result[0]


def part2(data):
    program = data[3:]

    aValues = set()
    aValues.add(0)
    for num in program[::-1]:
        newValues = set()
        for curr in aValues:
            for i in range(8):
                newVal = (curr << 3) + i
                if getOut(newVal, data) == num:
                    newValues.add(newVal)
        aValues = newValues
        # print(quines)
    return min(aValues)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", ",".join(map(str, part1(data))))
    print("part 2:", part2(data))
