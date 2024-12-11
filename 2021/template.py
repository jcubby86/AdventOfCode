def parse(file):
    f = open('input/{}.txt'.format(file), 'r')
    data = [x.strip() for x in f.readlines()]
    return data


def part1(data):
    pass


def part2(data):
    pass


if __name__ == '__main__':
    d = parse('day')
    part1(d)
    part2(d)
