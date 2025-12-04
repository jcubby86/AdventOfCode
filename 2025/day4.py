import logging
import sys
from util import parse_args, read_lines

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

neighbors = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),          (0, 1),
             (1, -1),  (1, 0), (1, 1)]

def parse_input(data: list) -> list:
    return [list(line) for line in data]

def part_1(data: list):
    count = 0
    for i, row in enumerate(data):
        for j, c in enumerate(row):
          if c == '.':
              continue
          occupied = 0
          for n in neighbors:
            ni, nj = i + n[0], j + n[1]
            if 0 <= ni < len(data) and 0 <= nj < len(row):
                if data[ni][nj] == '@':
                    occupied += 1
          if occupied < 4:
              count += 1
    return count

def part_2(data: list):
    count = 0
    changed = True
    while changed:
        changed = False
        for i, row in enumerate(data):
            for j, c in enumerate(row):
              if c == '.':
                  continue
              occupied = 0
              for n in neighbors:
                ni, nj = i + n[0], j + n[1]
                if 0 <= ni < len(data) and 0 <= nj < len(row):
                    if data[ni][nj] == '@':
                        occupied += 1
              if occupied < 4:
                  count += 1
                  changed = True
                  data[i][j] = '.'
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
