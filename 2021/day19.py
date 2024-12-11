def parse(file):
    f = open('input/{}.txt'.format(file), 'r')
    data = [x.strip() for x in f.readlines()]
    scanners = []
    mode = 'wait'
    for line in data:
        if line == '':
            mode = 'wait'
        elif mode == 'wait' and line[0] == '-':
            scanners.append([])
            mode = 'read'
        else:
            scanners[-1].append([int(x) for x in line.split(',')])
    return scanners


def makeBases():
    bases = []
    for i in range(1, 7):
        newI = i if i < 4 else 3-i
        for j in range(1, 7):
            newJ = j if j < 4 else 3-j
            if abs(newJ) == abs(newI):
                continue
            for k in range(1, 7):
                newK = k if k < 4 else 3-k
                if abs(newK) == abs(newI) or abs(newK) == abs(newJ):
                    continue
                # print(newI, newJ, newK)
                bases.append([basisLine(newI), basisLine(newJ), basisLine(newK)])
                # print()
    return bases


def basisLine(var):
    return [0 for _ in range(abs(var)-1)] + [var//abs(var)] + [0 for _ in range(3-abs(var))]


def part1(data):
    bases = makeBases()
    for base in bases:
        print(base)
    print(len(bases))
    return
    for line in data:
        print(line)


def part2(data):
    pass


if __name__ == '__main__':
    d = parse('test19')
    part1(d)
    part2(d)
