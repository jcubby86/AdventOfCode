import logging
import sys
from util import parse_args, read_lines

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_input(data: list) -> list:
    return [list(map(int, [c for c in x])) for x in data]

def largest_index(l: list[int]) -> int:
    largest = -1
    largest_index = -1
    for i, v in enumerate(l):
        if v > largest:
            largest = v
            largest_index = i
    return largest_index

def part_1(data: list):
    count = 0
    for bank in data:
        index_1 = largest_index(bank[:-1])
        index_2 = largest_index(bank[index_1 + 1:]) + index_1 + 1
        joltage = (bank[index_1] * 10) + bank[index_2]
        count += joltage
        logger.debug(f"In {''.join(map(str, bank))}, you can make the largest joltage possible, {joltage}, by turning on batteries {index_1} and {index_2}.")

    return count


def part_2(data: list):
    count = 0
    for bank in data:
        joltage = ""
        index = 0
        for i in range(-11, 1):
            index = largest_index(bank[index:(i if i != 0 else None)]) + index
            joltage += str(bank[index])
            index += 1
        count += int(joltage)
        logger.debug(f"In {''.join(map(str, bank))}, you can make the largest joltage possible, {joltage}")

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
    logger.debug(f"Input data: {data}")
    logger.info(f"part 1: {part_1(data)}")
    logger.info(f"part 2: {part_2(data)}")
