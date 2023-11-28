#!/usr/bin/env python3

import helper

def part1():

    # make list of strings
    instructions = helper.getData("8")

    # initial values
    accumulator = 0
    running = True
    instructionNumber = 1
    instructionSet = []

    # loop as long as instruction and line number are unique 
    while running:

        instruction = instructions[instructionNumber-1]
        iInstruction = str(instructionNumber) + " " + instruction

        if (iInstruction not in instructionSet):
            instructionSet.append(iInstruction)

            operation = instruction[0:3]
            argument = instruction[4:]

            if (operation == "acc"):
                accumulator += int(argument)
                instructionNumber += 1
            elif (operation == "jmp"):
                instructionNumber += int(argument)
            elif (operation == "nop"):
                instructionNumber += 1

        else:
            running = False

    return str(accumulator)

# main
print("solution for part 1: {}".format(part1()))

