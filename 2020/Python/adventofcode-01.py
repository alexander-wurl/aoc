#!/usr/bin/env python3

import helper

def part1():
    data = helper.getData("1")

    solution = 0

    for e in data:
        for j in data:
            value = int(e) + int(j)
            if (value == 2020):
                solution = int(e) * int(j)

    return solution

# main
print("solution for part 1: {}".format(part1()))
