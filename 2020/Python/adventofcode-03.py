#!/usr/bin/env python3

import helper

def part1():
    data = helper.getData("3")

    start = 0
    trees = 0

    for line in data:

        if (start > 30):
            start = start - 31

        if (line[start] == '#'):
            trees += 1

        start = start + 3

    return trees

# main
print("solution for part 1: {}".format(part1()))
