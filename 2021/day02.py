def parse():
    f = open('input/day2.txt', 'r')
    lines = [x.split() for x in f.readlines()]
    pairs = [(x, int(y)) for x, y in lines]
    return pairs


def part1(data):
    pos = 0
    depth = 0
    for x, y in data:
        if x == 'forward':
            pos += y
        if x == 'up':
            depth -= y
        if x == 'down':
            depth += y
    print(pos * depth)


def part2(data):
    pos = 0
    aim = 0
    depth = 0
    for x, y in data:
        if x == 'forward':
            pos += y
            depth += aim * y
        if x == 'up':
            aim -= y
        if x == 'down':
            aim += y
    print(pos * depth)


if __name__ == '__main__':
    d = parse()
    part1(d)
    part2(d)
