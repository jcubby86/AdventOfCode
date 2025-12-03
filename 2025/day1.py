import logging
import sys
from util import parse_args, read_lines

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_input(data: list) -> list:
    return [(x[0], int(x[1:])) for x in data]


def part_1(data: list):
    pos = 50
    count = 0
    for direction, value in data:
        if direction == "R":
            pos += value
        elif direction == "L":
            pos -= value

        pos = pos % 100
        if pos == 0:
            count += 1
        logger.debug(f"The dial is rotated {direction}{value} to point at {pos}.")
    return count


def part_2(data: list):
    pos = 50
    count = 0
    for direction, value in data:
        for _ in range(value):
            if direction == "R":
                pos += 1
            elif direction == "L":
                pos -= 1

            pos = pos % 100
            if pos == 0:
                count += 1
        logger.debug(f"The dial is rotated {direction}{value} to point at {pos}, count: {count}")
    return count


if __name__ == "__main__":
    # check all args for verbose flag
    verbose, filename = parse_args(sys.argv)
    if verbose:
        logger.setLevel(logging.DEBUG)
    if filename is None:
        logger.fatal("Missing file name")
        sys.exit(1)

    data = read_lines(filename)
    data = parse_input(data)
    logger.info(f"part 1: {part_1(data)}")
    logger.info(f"part 2: {part_2(data)}")