from os import stat
import helper
import statistics

def getfuel(part):

    # read data and cast to int
    data = helper.getData(7)[0].split(',')
    data = [int(e) for e in data]

    # statistics
    mean = statistics.mean(data)
    stabw = statistics.stdev(data)

    # start vars
    fuel = 0
    result = []

    # most reasonable would be mean to be start search, limited by stdev
    for pos in range(int(mean - stabw), int(mean + stabw)):

        # fuel needed for steps between pos and current position
        for d in data:
            if part == "part1":
                fuel += abs(d - pos)
            else:
                fuel += sum(i for i in range(0, abs(d - pos) + 1) )

        # save results, reset fuel
        result.append(fuel)
        fuel = 0

    return min(result)

def part1():

    print("solution for part 1: {}".format(getfuel("part1")))

def part2():

    print("solution for part 2: {}".format(getfuel("part2")))


# main
part1()
part2()