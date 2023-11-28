#!/usr/bin/env python3

import os

import helper

def part1():

    questions = ""
    solution = 0

    data = helper.getData("6")

    for line in data:

        if (line == ''):
            tlist = list("abcdefghijklmnopqrstuvwxyz")
            
            for e in questions:
                if (e in tlist):
                    tlist.remove(e)
            
            questions = ""

            v = 26 - len(tlist)
            solution += v
        else:
            questions = questions + line
        
    return solution

# main

print("solution for part 1: {}".format(part1()))
