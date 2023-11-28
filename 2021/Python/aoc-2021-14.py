import re

import helper


def part1():

    data = helper.getData(14)

    polymer = data[0]
    data = data[2:]
    rules = {}

    for d in data:
        tmp = d.split(" -> ")
        rules.update({tmp[0]: tmp[1]})

    steps = 10
    ret = polymer

    for _ in range(steps):

        polymer = ret
        ret = polymer

        for i in range(len(polymer) - 1):

            stop = False
            for r in rules:
                if stop != True:
                    input = ret[i * 2:(i * 2) + 2]
                    tmp = re.sub(r, rules[r], input)
                    if tmp != input:
                        output = input[0] + tmp + input[1]
                        ret = ret[0:i * 2] + output + ret[(i * 2) + 2:]
                        stop = True

    # evaluate length for each letter
    res = []
    for e in ret:
        tmp = re.findall(e, ret)
        res.append(len(tmp))

    # length for most common element minus least common element
    solution = max(res) - min(res)
    print("solution for part 1: {}".format(solution))

# main
part1()

