import math


def parse(file):
    f = open('input/{}.txt'.format(file), 'r')
    data = [int(x) for x in f.readlines()[0].strip().split(',')]
    return data


def part2(data):
    avg = round(sum(data)/len(data))
    best = math.inf
    changed = True
    start = avg
    while changed:
        changed = False
        cost = 0
        for i in data:
            cost += sum([j+1 for j in range(abs(i - start))])
        if cost < best:
            best = cost
            changed = True
            start -= 1
    changed = True
    start = avg
    while changed:
        changed = False
        cost = 0
        for i in data:
            cost += sum([j+1 for j in range(abs(i - start))])
        if cost < best:
            best = cost
            changed = True
            start += 1
    print(best)


def part1(data):
    avg = round(sum(data) / len(data))
    best = math.inf
    changed = True
    start = avg
    while changed:
        changed = False
        cost = 0
        for i in data:
            cost += abs(i - start)
        if cost < best:
            best = cost
            changed = True
            start -= 1
    changed = True
    start = avg
    while changed:
        changed = False
        cost = 0
        for i in data:
            cost += abs(i - start)
        if cost < best:
            best = cost
            changed = True
            start += 1
    print(best)


if __name__ == '__main__':
    d = parse('day7')
    part1(d)
    part2(d)
