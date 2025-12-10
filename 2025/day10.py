import logging
import sys
from unittest import result
import numpy as np
import mpmath
from scipy.optimize import nnls, lsq_linear, milp, linprog
from util import parse_args, read_lines, track_time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


MAX_INT = 1 << 31


def parse_input(data):
    machines = []
    for line in data:
        sections = line.split()

        lights = [1 if c == "#" else 0 for c in sections[0][1:-1]]
        buttons = [set(map(int, x[1:-1].split(","))) for x in sections[1:-1]]
        joltage = tuple(map(int, sections[-1][1:-1].split(",")))

        machines.append({"lights": lights, "buttons": buttons, "joltage": joltage})
    return machines


def part_1(data):
    count = 0
    for machine in data:
        logger.debug(f"Processing machine: {machine}")
        buttons = machine["buttons"]
        desired = tuple(machine["lights"])
        current = [0] * len(desired)

        memo = {}

        def find_solution(current, depth=0):
            if current == desired:
                return 0
            if depth >= 500:
                return MAX_INT
            if current in memo:
                return memo[current]

            # logger.debug(f"{'  '*depth}current: {current}, desired: {desired}")
            best_option = MAX_INT
            memo[current] = MAX_INT
            for i, b in enumerate(buttons):
                # logger.debug(
                #     f"{'  '*depth}current: {current} Trying button {i} which toggles lights {b}"
                # )
                test_state = [x for x in current]
                for index in b:
                    test_state[index] = 1 - test_state[index]
                res = find_solution(tuple(test_state), depth + 1)
                if res < best_option:
                    best_option = res
            memo[current] = best_option + 1
            return best_option + 1

        res = find_solution(tuple(current))
        count += res
        logger.debug(f"Machine {machine} requires {res} presses")
    return count


def part_2(data):
    count = 0
    for m, machine in enumerate(data):
        # logger.debug(f"Processing machine: {machine}")
        buttons = machine["buttons"]
        joltage = machine["joltage"]

        A = []
        for j in range(len(joltage)):
            row = []
            for i in range(len(buttons)):
                if j in buttons[i]:
                    row.append(1)
                else:
                    row.append(0)
            A.append(row)

        c = np.ones(len(buttons))
        A = np.array(A)
        b = np.array(joltage)
        res = linprog(c, A_eq=A, b_eq=b, integrality=True)
        logger.debug(f"Machine {m} requires {res.fun} presses")
        count += int(res.fun)
    return count


if __name__ == "__main__":
    # check all args for verbose flag
    verbose, filename = parse_args(sys.argv)
    if verbose:
        logger.setLevel(logging.DEBUG)
    if filename is None:
        logger.fatal("Missing file name")
        sys.exit(1)

    data = parse_input(read_lines(filename))
    logger.debug(f"Input data:\n{'\n'.join(str(d) for d in data)}")
    logger.info(f"part 1: {track_time(part_1)(data)}")
    logger.info(f"part 2: {track_time(part_2)(data)}")
