import logging
import sys
from util import parse_args, read_comma_separated

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_input(data: list) -> list:
    return [tuple(map(int, x.split("-"))) for x in data]


def part_1(data: list):
    def is_invalid(number):
        s = str(number)
        if len(s) %2 != 0:
            return False
        half = len(s)//2
        return s[:half] == s[half:]

    count = 0
    for low, high in data:
        for number in range(low, high + 1):
            if is_invalid(number):
                count += number
                logger.debug(f"Adding invalid number: {number}")
    return count

def part_2(data: list):
    def is_invalid(number):
        s = str(number)
        for i in range(1, (len(s)//2) + 1):
            t = s[:i]
            if all(s[j:j+i] == t for j in range(0, len(s), i)):
                return True
            
    count = 0
    for low, high in data:
        for number in range(low, high + 1):
            if is_invalid(number):
                count += number
                logger.debug(f"Adding invalid number: {number}")
    return count


if __name__ == "__main__":
    # check all args for verbose flag
    verbose, filename = parse_args(sys.argv)
    if verbose:
        logger.setLevel(logging.DEBUG)
    if filename is None:
        logger.fatal("Missing file name")
        sys.exit(1)

    data = read_comma_separated(filename)
    data = parse_input(data)
    logger.debug(f"Input data: {data}")
    logger.info(f"part 1: {part_1(data)}")
    logger.info(f"part 2: {part_2(data)}")