import logging
import sys
from util import parse_args, read_lines, track_time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_input(data):
    lines = [line.split() for line in data]
    return {line[0].replace(":", ""): tuple(line[1:]) for line in lines}


def part_1(data):

    memo = {}

    def solve(input):
        if input in memo:
            return memo[input]
        count = 0
        for output in data.get(input, ()):
            if output == "out":
                count += 1
            else:
                count += solve(output)
        memo[input] = count
        return count

    return solve("you")


def part_2(data):

    memo = {}

    def solve(input, dac=False, fft=False):
        if (input, dac, fft) in memo:
            return memo[(input, dac, fft)]
        count = 0
        for output in data.get(input, ()):
            if output == "out":
                count += 1 if dac and fft else 0
            else:
                count += solve(output, dac or input == "dac", fft or input == "fft")
        memo[(input, dac, fft)] = count
        return count

    return solve("svr")


if __name__ == "__main__":
    # check all args for verbose flag
    verbose, filename = parse_args(sys.argv)
    if verbose:
        logger.setLevel(logging.DEBUG)
    if filename is None:
        logger.fatal("Missing file name")
        sys.exit(1)

    data = parse_input(read_lines(filename))
    logger.debug(f"Input data: {data}")
    logger.info(f"part 1: {track_time(part_1)(data)}")
    logger.info(f"part 2: {track_time(part_2)(data)}")
