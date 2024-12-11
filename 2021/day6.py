def parse(file):
    f = open('input/{}.txt'.format(file), 'r')
    data = [x.strip() for x in f.readlines()]
    return [int(x) for x in data[0].split(',')]


def part1(data):
    # print(data)
    for i in range(256):
        length = len(data)
        for j in range(length):
            if data[j] == 0:
                data[j] = 6
                data.append(8)
            else:
                data[j] -= 1
        # print(data)
    print(len(data))


def part2(data):
    nums = [0 for i in range(10)]
    for fish in data:
        nums[fish] += 1
    for i in range(256):
        nums[9] += nums[0]
        nums[7] += nums[0]
        for j in range(9):
            nums[j] = nums[j+1]
        nums[9] = 0
        print(i+1, nums)
    print(sum(nums))


if __name__ == '__main__':
    d = parse('day6')
    # part1(d)
    part2(d)
