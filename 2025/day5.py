import logging
import sys
from util import parse_args, read_lines, track_time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_input(data: list) -> list:
    ranges = []
    ingredients = []
    for row in data:
        if row == '':
            break
        ranges.append(tuple(map(int, row.split('-'))))
    for row in data[len(ranges)+1:]:
        ingredients.append(int(row))
    return ranges, ingredients

def part_1(ranges: list, ingredients: list):
    count = 0
    for ingredient in ingredients:
        for r in ranges:
            if r[0] <= ingredient <= r[1]:
                count +=1
                logger.debug(f"Ingredient {ingredient} fits in range {r}")
                break
    return count

def part_2(ranges: list, ingredients: list):
    # sort ranges by start value
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    i = 0
    while i < len(sorted_ranges) - 1:
        current = sorted_ranges[i]
        next_range = sorted_ranges[i + 1]
        if current[1] >= next_range[0]:  # overlapping or contiguous
            merged_range = (current[0], max(current[1], next_range[1]))
            sorted_ranges[i] = merged_range
            del sorted_ranges[i + 1]
            logger.debug(f"Merged ranges {current} and {next_range} into {merged_range}")
        else:
            i += 1
    logger.debug(f"Merged ranges: {sorted_ranges}")

    count = 0
    for r in sorted_ranges:
        count += r[1] - r[0] + 1
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
    logger.info(f"part 1: {track_time(part_1)(*data)}")
    logger.info(f"part 2: {track_time(part_2)(*data)}")