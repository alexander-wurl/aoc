#!/usr/bin/env python3

import os

import helper

def part1():

    data = helper.getData("5")

    highestSeatId = 0

    for line in data:

        min = 0
        max = 128
        lowerId = 'F'
        upperId = 'B'
        step = 0
        l = []
        l[:] = line

        for e in l:

            h = (max - min) / 2 

            if (e == lowerId):
                # lower half
                max = max - h
            elif (e == upperId):
                # upper half
                min = min + h

            step += 1

            if (step == 7):
                row = min
                min = 0
                max = 8
                lowerId = 'L'
                upperId = 'R'

            if (step == 10):
                column = min
                seatId = (row * 8) + column

                if (seatId >= highestSeatId):
                    highestSeatId = seatId

    return highestSeatId

# main
print("solution for part 1: {}".format(part1()))
