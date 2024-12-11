def main():
	i = 8
	temp = open('template.py', 'r')
	out = open('day{}.py'.format(i), 'w+')

	for line in temp.readlines():
		out.write(line)


if __name__ == '__main__':
	main()
