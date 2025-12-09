import logging
import sys
from util import parse_args, read_lines, track_time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_input(data):
    return [tuple(map(int, line.split(","))) for line in data]


def print_tiles(reds, greens, max_x, max_y):
    if not logger.isEnabledFor(logging.DEBUG):
        return
    for y in range(max_y + 2):
        line = ""
        for x in range(max_x + 3):
            if (x, y) in reds:
                line += "#"
            elif (x, y) in greens:
                line += "X"
            else:
                line += "."
        logger.debug(line)
    logger.debug("")


def part_1(data):
    max_area = 0
    for i, point1 in enumerate(data):
        for j, point2 in enumerate(data):
            if j <= i:
                continue
            dist = abs(point1[0] - point2[0] + 1) * abs(point1[1] - point2[1] + 1)
            if dist > max_area:
                max_area = dist
                logger.debug(
                    f"New max area {max_area} from points {point1} and {point2}"
                )
    return max_area


def part_2(data):
    max_x = max(x for x, _ in data)
    max_y = max(y for _, y in data)
    reds = set(data)
    greens = set()

    print_tiles(reds, greens, max_x, max_y)

    for i in range(len(data)):
        x1, y1 = data[i]
        x2, y2 = data[(i + 1) % len(data)]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                greens.add((x1, y))
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                greens.add((x, y1))

    print_tiles(reds, greens, max_x, max_y)

    max_area = 0
    for i, point1 in enumerate(data):
        for j, point2 in enumerate(data):
            if j <= i:
                continue
            min_x = min(point1[0], point2[0])
            min_y = min(point1[1], point2[1])
            width = abs(point1[0] - point2[0])
            height = abs(point1[1] - point2[1])
            dist = (width + 1) * (height + 1)
            for x1, y1 in greens:
                if min_x < x1 < min_x + width and min_y < y1 < min_y + height:
                    dist = 0
                    break
            if dist > max_area:
                max_area = dist
                logger.debug(
                    f"New max area {max_area} from points {point1} and {point2}"
                )
    return max_area


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
