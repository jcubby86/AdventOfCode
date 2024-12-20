#!/usr/bin/env python3

import sys


def readData(fileName: str):
    with open(fileName, "r") as f:
        data = [x.strip() for x in f.readlines()]
        out = []
        for line in data:
            newLine: list[list[str]] = [[]]
            for x in line.split():
                if x == "|":
                    newLine.append([])
                else:
                    newLine[-1].append(x)
            out.append(newLine)
        return out
    return []


def part1(data):
    count = 0
    for line in data:
        for out in line[1]:
            if len(out) == 2 or len(out) == 3 or len(out) == 4 or len(out) == 7:
                count += 1
    print(count)


def part2(data):
    possibilities = {"tl", "tr", "bl", "br", "t", "b", "m"}
    letters = {"a", "b", "c", "d", "e", "f", "g"}
    for line in data:
        options = dict()
        for p in possibilities:
            options[p] = letters.copy()
        for num in line[0]:
            if len(num) == 2:
                options.update({"tr": options.get("tr").intersection(set(num))})
                options.update({"br": options.get("br").intersection(set(num))})
            if len(num) == 3:
                options.update({"t": options.get("t").intersection(set(num))})
                options.update({"tr": options.get("tr").intersection(set(num))})
                options.update({"br": options.get("br").intersection(set(num))})
            if len(num) == 4:
                options.update({"tr": options.get("tr").intersection(set(num))})
                options.update({"br": options.get("br").intersection(set(num))})
                options.update({"tl": options.get("tl").intersection(set(num))})
                options.update({"m": options.get("m").intersection(set(num))})
        for key in options.keys():
            if key != "tr" and key != "br":
                options.update({key: options.get(key).difference(options.get("tr"))})
        small = []
        for key in options.keys():
            if len(options.get(key)) <= 2:
                small.append(options.get(key))
        for key in options.keys():
            if len(options.get(key)) > 2:
                for s in small:
                    options.update({key: options.get(key).difference(s)})

        print(options)


def attempt2(data):
    map = {
        frozenset("abcefg"): 0,
        frozenset("cf"): 1,
        frozenset("acdeg"): 2,
        frozenset("acdfg"): 3,
        frozenset("bdcf"): 4,
        frozenset("abdfg"): 5,
        frozenset("abdefg"): 6,
        frozenset("acf"): 7,
        frozenset("abcdefg"): 8,
        frozenset("abcdfg"): 9,
    }
    for line in data:
        inp, out = line
        inp = [set(num) for num in inp]
        inp = sorted(inp, key=len)
        mapping = {k: None for k in "abcdefg"}
        mapping["a"] = (inp[1] - inp[0]).pop()
        candf = inp[1] - {mapping["a"]}
        bandd = inp[2] - candf
        print(inp)
        print(mapping)
        print(candf, bandd)
        for i in [3, 4, 5]:
            if bandd.issubset(inp[i]):
                print(candf.union(bandd).union({mapping["a"]}))
                mapping["g"] = (
                    inp[i] - (candf.union(bandd).union({mapping["a"]}))
                ).pop()
                break
        mapping["e"] = (
            inp[-1] - (bandd.union(candf).union(set(mapping[k] for k in "ag")))
        ).pop()
        break


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing file name")
        sys.exit(1)

    data = readData(sys.argv[1])

    print("part 1:", part1(data))
    print("part 2:", part2(data))
