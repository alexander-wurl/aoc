#!/usr/bin/env python3
import helper

data = helper.getData(1)

# part 1
def part1():
    increased = 0

    for index in range(1, len(data)):
        
        if (int(data[index]) - int(data[index - 1])) > 0:
            increased += 1

    print("solution for part 1: {}".format(increased))


# part 2
def part2():
    increased = 0

    for index in range(1, len(data)):
        sum1 = sum(list(map(int, data[index:index + 3])))
        sum2 = sum(list(map(int, data[index - 1:index + 2])))
        
        if sum1 > sum2:
            increased += 1

    print("solution for part 2: {}".format(increased))

# main
part1()
part2()