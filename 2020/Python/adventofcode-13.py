#!/usr/bin/env python3

import helper

# split 'data' by comma, remove 'x' from within, cast each value to int 
def getBusIds(data):
    return [int(e) for e in data.replace(",x", "").split(",")]

# print timetable body
def printTimeTable(time, info):
    print(time + "\t", end = "")
    for e in info:
        print(e + "\t", end = "")
    print("")

def part1():
    
    # data
    data = helper.getData("13")

    # estimated time of (my) arrival at bus stop
    eta = int(data[0])

    # relevant bus ids
    ids = getBusIds(data[1])

    # set index and maximal waiting time using highest bus id
    i = eta
    max_waiting_time = i + max(ids)

    # initial values
    waiting_time = 9999
    bus_id = 0

    while (i <= max_waiting_time):

        bus_stops = []

        for e in ids:
            if ((i % e) == 0):
                bus_stops.append("D")
                t = i - eta
                if (waiting_time > t):
                    waiting_time = t
                    bus_id = e
            else:
                bus_stops.append("-")

        i += 1

    return bus_id * waiting_time

# main
print("solution for part 1: {}".format(part1()))
