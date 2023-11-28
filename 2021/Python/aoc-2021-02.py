#!/usr/bin/env python3
import helper

data = helper.getData(2)


def part1():
    horizontal = sum([int(e.split()[1]) for e in data if e.split()[0] == 'forward'])
    depth = sum([int(e.split()[1]) for e in data if e.split()[0] == 'down']) \
        - sum([int(e.split()[1]) for e in data if e.split()[0] == 'up'])
    print("solution for part 1: {}".format(horizontal * depth))

def part2():

    horizontal = 0
    depth = 0
    aim = 0

    for e in data:
        dir = e.split()[0]
        val = int(e.split()[1])

        if dir == 'forward':
            horizontal += val
            depth += aim * val
        elif dir == 'down':
            aim += val
        elif dir == 'up':
            aim -= val

    print("solution for part 2: {}".format(horizontal * depth))

# main
part1()
part2()