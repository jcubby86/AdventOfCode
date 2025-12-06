import logging
import sys
from util import parse_args, read_lines, track_time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_lines(fileName: str) -> list:
    with open(fileName, "r") as f:
        return [x.replace('\n', '') for x in f.readlines()]
    return []


def part_1(data):
    
    def parse_input(data: list) -> list:
        numbers = [tuple(map(int, row.split())) for row in data[:-1]]
        operators = tuple(data[-1].split())
        return numbers, operators
    
    numbers, operators = parse_input(data)
    
    answers = [0 if op == '+' else 1 for op in operators]
    for row in numbers:
        for i, num in enumerate(row):
            if operators[i] == '+':
                answers[i] += num
            else:
                answers[i] *= num
    return sum(answers)

def part_2(data):
    
    def parse_input(data: list) -> list:
        columns = []
        for c in range(len(data[0]) - 1, -1, -1):
            column = ''
            for r in range(len(data)):
                # logger.debug(f"r: {r}, c: {c}, {len(data[r])}")
                column += data[r][c]
            columns.append(column.strip())
        logger.debug(f"columns: {columns}")
        return columns
    
    columns = parse_input(data)
    columns.append('')
    problems = [[]]
    
    for column in columns:
        if column == '':
            last_number = problems[-1][-1]
            problems[-1][-1] = last_number[:-1]
            problems[-1].append(last_number[-1])
            problems.append([])
        else:
            problems[-1].append(column)
    problems.pop()
    logger.debug(f"problems: {problems}")

    count = 0
    for problem in problems:
        if problem[-1] == '*':
            result = 1
            for num in problem[:-1]:
                result *= int(num)
            count += result
        else:
            count += sum(map(int, problem[:-1]))
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
    logger.info(f"part 1: {track_time(part_1)(data)}")
    logger.info(f"part 2: {track_time(part_2)(data)}")