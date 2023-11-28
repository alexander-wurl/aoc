#!/usr/bin/env python3

from itertools import combinations

import helper

def isValidNumber(preamble, number):
    for e in combinations(preamble, 2):

        sum = int(e[0]) + int(e[1])

        if (e[0] != e[1]) and (sum == int(number)):
            return True
    return False
    

def part1():
    data = helper.getData("9")

    # preamble length
    f = 25

    # current index
    i = f

    # solution
    ret = ""

    # e is current element
    for e in data[f:]:

        # build preamble from previous numbers
        start = i-f
        stop = i
        preamble = data[start:stop]

        # check for valid numbers in preamble 
        if (isValidNumber(preamble, e) == False):
            ret = "{} + is not valid!".format(e)

        i += 1

    return ret

# main
print("solution for part 1: {}".format(part1()))

