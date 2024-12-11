def day1():
	f = open('input/day1.txt', 'r')
	lines = [int(x.strip()) for x in f.readlines()]

	window = 3
	count = 0
	prev = -1
	for i in range(len(lines)-window):
		curr = sum(lines[i:(i + window)])
		if curr > prev:
			count += 1
		prev = curr
	print(count)


if __name__ == '__main__':
	day1()
