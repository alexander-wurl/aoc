#!/usr/bin/env python

import helper
from itertools import product

def getSumOfValuesInDictionary(dict):
    v = (dict.values())
    s = sum(v)
    return s

def part1():

    data = helper.getData("14")

    mask = ""
    memory = {}

    for e in data:

        # get mask ...
        if (e[0:7] == "mask = "):
            mask = e[7:]
        else:
            # ... or adress and value
            pos = e.find("] = ")
            address = e[4:pos]
            value = e[pos+4:]

            # convert value to binary, remove prefix
            bvalue = str(bin(int(value)))[2:]

            # fill leading gap with zeros
            while (len(bvalue) < 36):
                bvalue = "0" + str(bvalue)

            # use mask to define binary value
            for (i, b) in enumerate(mask):
                if (b == "0"):
                    bvalue = bvalue[0:i] + "0" + bvalue[i+1:]
                elif (b == "1"):
                    bvalue = bvalue[0:i] + "1" + bvalue[i+1:]
                pass

            # binary value to int
            value = int(bvalue, 2)

            # update value if already exists otherwise add
            memory[address] = value

    print("solution for part 1: {}".format(getSumOfValuesInDictionary(memory)))

def part2():

    data = helper.getData("14")

    mask = ""
    memory = {}

    for e in data:

        # get mask ...
        if (e[0:7] == "mask = "):
            mask = e[7:]
        else:
            # ... or address and value
            pos = e.find("] = ")
            address = e[4:pos]
            value = int(e[pos+4:])

            # convert address to binary, remove prefix
            baddress = str(bin(int(address)))[2:]

            # fill leading gap with zeros
            while (len(baddress) < 36):
                baddress = "0" + str(baddress)

            # use mask to define binary address
            for (i, b) in enumerate(mask):
                if (b == "1"):
                    baddress = baddress[0:i] + "1" + baddress[i+1:]
                elif (b == "X"):
                    baddress = baddress[0:i] + "X" + baddress[i+1:]
                pass

            # use baddress as new mask
            n = baddress.count("X")

            # binary decision table
            l = list(product([0, 1], repeat = n))

            for i in l:

                k = 0
                newbaddress = baddress

                # replace 'X' in binary adress with values in decision table 
                for (j, b) in enumerate(baddress):
                    if (b == "X"):
                        newbaddress = newbaddress[0:j] + str(i[k]) + newbaddress[j+1:]
                        k += 1

                # binary newaddress to int
                newaddress = int(newbaddress, 2)

                # update value if already exists otherwise add
                memory[newaddress] = value
                
    print("solution for part 2: {}".format(getSumOfValuesInDictionary(memory)))

# main
part1()
part2()
