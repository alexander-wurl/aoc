#!/usr/bin/env python3

import helper

def nextOccupiedNeighbours(data, xs, ys):
    # looking for neighbours within restricted range (length of field - 1) 
    lx = len(data) - 1
    ly = len(data[0]) - 1

    ret = []

    x = xs
    y = ys

    # upper left
    while ((x > 0) and (y > 0)):
        if ( (data[x-1][y-1] == '#') or (data[x-1][y-1] == 'L') ):
            ret.append( data[x-1][y-1] )
            break
        x -= 1
        y -= 1

    x = xs
    y = ys

   # upper middle
    while (x > 0):
        if ( (data[x-1][y] == '#') or (data[x-1][y] == 'L') ):
            ret.append( data[x-1][y] )
            break
        x -= 1

    x = xs
    y = ys

    # upper right
    while ((x > 0) and (y < ly)):
        if ( (data[x-1][y+1] == '#') or (data[x-1][y+1] == 'L') ):
            ret.append( data[x-1][y+1] )
            break
        x -= 1
        y += 1

    x = xs
    y = ys

    # left
    while (y > 0):
        if ( (data[x][y-1] == '#') or (data[x][y-1] == 'L') ):
            ret.append( data[x][y-1] )
            break
        y -= 1

    x = xs
    y = ys

    # right
    while (y < ly):
        if ( (data[x][y+1] == '#') or (data[x][y+1] == 'L') ):
            ret.append( data[x][y+1] )
            break
        y += 1

    x = xs
    y = ys

    # lower left
    while ((x < lx) and (y > 0)):
        if ( (data[x+1][y-1] == '#') or (data[x+1][y-1] == 'L') ):
            ret.append( data[x+1][y-1] )
            break
        x += 1
        y -= 1
    
    x = xs
    y = ys

    # lower middle
    while (x < lx):
        if ( (data[x+1][y] == '#') or (data[x+1][y] == 'L') ):
            ret.append( data[x+1][y] )
            break
        x += 1

    x = xs
    y = ys

    # lower right
    while ((x < lx) and (y < ly)):
        if ((data[x+1][y+1] == '#') or (data[x+1][y+1] == 'L')):
            ret.append( data[x+1][y+1] )
            break
        x += 1
        y += 1

    return ret

def neighbours(data, x, y):

    # looking for neighbours within restricted range (length of field - 1) 
    lx = len(data) - 1
    ly = len(data[0]) - 1

    # append at max 8 neighbours
    ret = []

    # upper left
    if (x > 0 and y > 0):
        ret.append( data[x-1][y-1] )

    # upper middle
    if (x > 0):
        ret.append( data[x-1][y] )

    # upper right
    if (x > 0 and y < ly):
        ret.append( data[x-1][y+1] )

    # left
    if (y > 0):
        ret.append( data[x][y-1] )

    # right
    if (y < ly):
        ret.append( data[x][y+1] )

    # lower left
    if (x < lx and y > 0):
        ret.append( data[x+1][y-1] )

    # lower middle
    if (x < lx):
        ret.append( data[x+1][y] )

    # lower right
    if (x < lx and y < ly):
        ret.append( data[x+1][y+1] )

    return ret

def changeSeats(data, param1, part1):

    # start position is upper left
    x = 0
    y = 0

    newdata = data.copy()
    change = False

    for e in data:
        for _ in e:

            if (part1 == True):
                n = neighbours(data, x, y)
            else:
                n = nextOccupiedNeighbours(data, x, y)

            # if current chair (x,y-position) is empty ('L') and none of the neighbour chairs is occupied ('#') ...
            if ( (data[x][y] == 'L') and (str(n).count('#') == 0) ):
                # ... occupy current chair ('#')
                newdata[x] = newdata[x][0:y] + "#" + newdata[x][y+1:]
                change = True

            # if current chair is occupied and >= 4 neighbouring chairs as well ...
            if ( (data[x][y] == '#') and (str(n).count('#') >= param1) ):
                # ... empty ('L') the current one
                newdata[x] = newdata[x][0:y] + "L" + newdata[x][y+1:]
                change = True

            y += 1
        y = 0
        x += 1

    return change, newdata

def part1():
    data = helper.getData("11")
    finaldata = []

    while True:
        (c, newdata) = changeSeats(data, 4, part1 = True)
 
        if (c == False):
            finaldata = data
            break
        else:
            data = newdata
 
    c = 0
    
    for e in finaldata:
        for j in e:
            if (j == '#'):
                c += 1

    return c

def part2():
    data = helper.getData("11")
    finaldata = []

    while True:
        (c, newdata) = changeSeats(data, 5, part1 = False)

        if (c == False):
            finaldata = data
            break
        else:
            data = newdata

    c = 0

    for e in finaldata:
        for j in e:
            if (j == '#'):
                c += 1

    return c

# main

print("solution for part 1: {}".format(part1()))
print("solution for part 2: {}".format(part2()))
