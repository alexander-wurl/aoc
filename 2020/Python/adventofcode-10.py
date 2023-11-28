#!/usr/bin/env python3

import helper

def recursion(voltage, d1, d2, d3):
    # find elements in list which are 1, 2, or 3 lower
    # then use each of them for recursive call

    global diff1
    global diff2
    global diff3

    if (voltage <= max):

        for e in data:
            if (e - voltage == 1):
                # diff = 1
                diff1.append("1|" + str(e) + "|" + str(voltage))
                recursion(e, d1 + 1, d2, d3)
                data.remove(e)
            elif (e - voltage == 2):
                # diff = 2
                diff2.append("2|" + str(e) + "|" + str(voltage))
                recursion(e, d1, d2 + 1, d3)
                data.remove(e)
            elif (e - voltage == 3):
                # diff = 3
                diff3.append("3|" + str(e) + "|" + str(voltage))
                recursion(e, d1, d2, d3 + 1)
                data.remove(e)
    else:
        pass

temp = helper.getData("10")

# to int
data = [int(e) for e in temp]
data.sort()

# set max as defined, append to list
max = max(data) + 3
data.append(max)

# lists to append each connected adapter 
diff1 = []
diff2 = []
diff3 = []

# start recursion
recursion(0, 0, 0, 0)


print("solution for part 1: {}".format(str(len(diff1) * len(diff3))))
