import logging
import sys
from util import parse_args, read_lines, track_time
from functools import cache

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_input(data):
    presents = []
    for i in range(0, 30, 5):
        p = []
        for r in range(3):
            p.append(tuple([1 if c == "#" else 0 for c in data[i + 1 + r]]))
        presents.append(tuple(p))

    regions = []
    for line in data[30:]:
        l, r = line.split(":")
        width, height = map(int, l.strip().split("x"))
        quantities = tuple(map(int, r.strip().split(" ")))
        regions.append((width, height, quantities))

    return (presents, regions)


@cache
def rotate_present(present):
    return tuple(tuple(present[2 - c][r] for c in range(3)) for r in range(3))


@cache
def flip_present(present):
    return tuple(tuple(present[r][2 - c] for c in range(3)) for r in range(3))


@cache
def all_orientations(present):
    orientations = set()
    p = present
    for _ in range(4):
        orientations.add(p)
        orientations.add(flip_present(p))
        p = rotate_present(p)
    return orientations


def print_grid(width, height, occupied):
    for c in range(height):
        row = ""
        for r in range(width):
            if (r, c) in occupied:
                row += "#"
            else:
                row += "."
        logger.debug(row)


@cache
def try_place(width, height, occ, qts):
    if sum(qts) == 0:
        return True
    if width < 3 or height < 3:
        return False

    quantities = list(qts)
    occupied = set(occ)
    logger.debug(f"Quantities: {quantities}")

    last_col = [(c, width - 1) for c in range(height)]
    last_row = [(height - 1, r) for r in range(width)]

    for c, r in last_col + last_row:
        if c < 2 or r < 2:
            continue
        for i, present in enumerate(presents):
            if quantities[i] == 0:
                continue
            for o, orientation in enumerate(all_orientations(present)):
                occ_present = set()
                logger.debug(f"Trying to place present {i} orientation {o} at {(r, c)}")
                for c2 in range(3):
                    for r2 in range(3):
                        if orientation[c2][r2] == 1:
                            occ_present.add((r + r2 - 2, c + c2 - 2))
                if len(occ_present.intersection(occupied)) == 0:
                    logger.debug(f"Placing present {i} orientation {o} at {(r, c)}")
                    print_grid(width, height, occupied.union(occ_present))
                    quantities[i] -= 1
                    if try_place(
                        width,
                        height,
                        tuple(occupied.union(occ_present)),
                        tuple(quantities),
                    ):
                        return True
                    quantities[i] += 1
    return try_place(width - 1, height - 1, tuple(occupied.difference(last_col + last_row)), qts)


def part_1(data):
    _, regions = data
    count = 0
    for region in regions:
        print(f"Processing region: {region}")
        width, height, quantities = region
        
        pres_count = 0
        for i, c in enumerate(quantities):
            present = presents[i]
            pres_count += sum([sum(row) for row in present]) * c
        if pres_count < width * height:
            count += 1

        # if try_place(width, height, (), quantities):
        #     count += 1
    return count


def part_2(data):
    pass


if __name__ == "__main__":
    # check all args for verbose flag
    verbose, filename = parse_args(sys.argv)
    if verbose:
        logger.setLevel(logging.DEBUG)
    if filename is None:
        logger.fatal("Missing file name")
        sys.exit(1)

    data = parse_input(read_lines(filename))
    presents = data[0]
    logger.debug(f"Input data: {data}")
    logger.info(f"part 1: {track_time(part_1)(data)}")
    logger.info(f"part 2: {track_time(part_2)(data)}")
