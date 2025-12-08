import logging
import sys
from util import parse_args, read_lines, track_time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def part_1(data):
    tach_set = set()
    tachyons = []
    splitters = set()

    for col in range(len(data[0])):
        if data[0][col] == "S":
            tachyons.append((0, col))

    while len(tachyons) > 0:
        row, col = tachyons.pop(0)
        if row >= len(data) or col < 0 or col >= len(data[0]):
            continue
        elif data[row][col] == "^":
            splitters.add((row, col))
            if (row, col - 1) not in tach_set:
                tachyons.append((row, col - 1))
                tach_set.add((row, col - 1))
            if (row, col + 1) not in tach_set:
                tachyons.append((row, col + 1))
                tach_set.add((row, col + 1))
        else:
            if (row + 1, col) not in tach_set:
                tachyons.append((row + 1, col))
                tach_set.add((row + 1, col))
    return len(splitters)


def part_2(data):
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == "S":
                data[row][col] = 1
            elif row == 0:
                data[row][col] = 0
            elif row > 0 and data[row][col] != "^":
                timelines = 0
                if col > 0 and data[row][col - 1] == "^":
                    timelines += data[row - 1][col - 1]
                if col < len(data[row]) - 1 and data[row][col + 1] == "^":
                    timelines += data[row - 1][col + 1]
                if data[row - 1][col] not in (".", "^"):
                    timelines += data[row - 1][col]
                data[row][col] = timelines
    return sum([x for x in data[-1] if isinstance(x, int)])


if __name__ == "__main__":
    # check all args for verbose flag
    verbose, filename = parse_args(sys.argv)
    if verbose:
        logger.setLevel(logging.DEBUG)
    if filename is None:
        logger.fatal("Missing file name")
        sys.exit(1)

    data = [list(x) for x in read_lines(filename)]
    # logger.debug(f"Input data:\n{'\n'.join(data)}")
    logger.info(f"part 1: {track_time(part_1)(data)}")
    logger.info(f"part 2: {track_time(part_2)(data)}")
