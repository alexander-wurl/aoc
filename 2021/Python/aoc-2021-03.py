#!/usr/bin/env python3
import helper

data = helper.getData(3)

def commonbit(d, bit):

    # put each bit at same place to a column
    cols = [ [int(e[j]) for e in d] for j in range(len(d[0]))]

    # common bit ...
    binary = [ bit if e.count(1) >= e.count(0) else abs(bit - 1) for e in cols]

    # convert to string and return 
    ret = ''.join(str(e) for e in binary)
    return ret

def part1():

    # most common bit
    mbits = commonbit(data, 1)

    # convert to decimals and concatenate bits -> epsilon
    epsilon = int(''.join(str(e) for e in mbits), 2)

    # least common bit
    lbits = commonbit(data, 0)

    # convert to decimals and concatenate bits -> gamma
    gamma = int(''.join(str(e) for e in lbits), 2)

    # power consumption
    power = epsilon * gamma

    print("solution for part 1: {}".format(power))

def removeifcommon(d, bit):
    i = 0
    
    # remove item from list if (i.) bit and common bit are equal 
    while len(d) > 1:
        mcb = commonbit(d, bit)
        d = [e for e in d if e[i] == mcb[i]]
        i += 1

    return int(''.join(str(e) for e in d), 2)

def part2():

    oxygen = removeifcommon(data, 1)
    co2 = removeifcommon(data, 0)
    life = oxygen * co2
    print("solution for part 2: {}".format(life))

# main
part1()
part2()
