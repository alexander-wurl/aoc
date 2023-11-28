#!/usr/bin/env python3

import helper

def moveNorth(position: [int, int], value: int, direction: [int, int]) -> ([int, int], [int, int]):
    position[1] += int(value)
    return (position, direction)

def moveSouth(position: [int, int], value: int, direction: [int, int]) -> ([int, int], [int, int]):
    position[1] -= int(value)
    return (position, direction)

def moveEast(position: [int, int], value: int, direction: [int, int]) -> ([int, int], [int, int]):
    position[0] += int(value)
    return (position, direction)

def moveWest(position: [int, int], value: int, direction: [int, int]) -> ([int, int], [int, int]):
    position[0] -= int(value)
    return (position, direction)

def moveForward(position: [int, int], value: int, direction: [int, int]) -> ([int, int], [int, int]):
    r = helper.np.dot(value, [direction[0], direction[1]])
    o = [position[0], position[1]]
    newposition = helper.np.add(o, r)
    return (newposition, direction)

def turnLeft(position: [int, int], degrees: int, direction: [int, int]) -> ([int, int], [int, int]):
    newdirection = helper.rotate(direction, [0, 0], degrees)
    return (position, newdirection)

def turnRight(position: [int, int], degrees: int, direction: [int, int]) -> ([int, int], [int, int]):
    newdirection = helper.rotate(direction, [0, 0], -degrees)
    return (position, newdirection)

# possible actions as dictionary
actions = {
    "N": moveNorth,
    "S": moveSouth,
    "E": moveEast,
    "W": moveWest,
    "L": turnLeft,
    "R": turnRight,
    "F": moveForward
}

def part1():
    # current position ((x, y) = (east, north))
    position = [0, 0]

    # direction vector ((x, y) = (east, north))
    direction = [1, 0]

    # load data
    data = helper.getData("12")

    # process action and value line by line
    for e in data:
        action = e[0]
        value = int(e[1:])
        (position, direction) = actions[action](position, value, direction)

    # calculate manhatten distance
    distance = abs(int(position[0])) + abs(int(position[1]) )

    # solution
    return distance

# main
print("solution for part 1: {}".format(part1()))