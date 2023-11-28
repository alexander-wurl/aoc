#!/usr/bin/env python
import helper

# extend cube in all dimension by 1
def ExtendCubes3D(cubes) -> list:

    # get and increase outer bundaries by 1
    max_x = max(cubes)[0] + 1
    min_x = min(cubes)[0] - 1
    max_y = max(cubes)[1] + 1
    min_y = min(cubes)[1] - 1
    max_z = max(cubes)[2] + 1
    min_z = min(cubes)[2] - 1

    # convex hull
    convex_hull = []

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            convex_hull.append( (x, y, max_z, ".") )
            convex_hull.append( (x, y, min_z, ".") )

    for x in range(min_x, max_x + 1):
        for z in range(min_z, max_z + 1):
            convex_hull.append( (x, max_y, z, ".") )
            convex_hull.append( (x, min_y, z, ".") )

    for y in range(min_y, max_y + 1):
        for z in range(min_z, max_z + 1):
            convex_hull.append( (max_x, y, z, ".") )
            convex_hull.append( (min_x, y, z, ".") )

    # create a dictionary from element where duplicates will be removed from
    unique_convex_hull = list(dict.fromkeys(convex_hull))
    cubes += unique_convex_hull
    return cubes

def ExtendCubes4D(cubes) -> list:

    # get outer bundaries in x, y and z direction
    max_x = max(cubes)[0] + 1
    min_x = min(cubes)[0] - 1
    max_y = max(cubes)[1] + 1
    min_y = min(cubes)[1] - 1
    max_z = max(cubes)[2] + 1
    min_z = min(cubes)[2] - 1
    max_w = max(cubes)[3] + 1
    min_w = min(cubes)[3] - 1

    convex_hull = []

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_y, max_y + 1):
                convex_hull.append( (x, y, z, max_w, ".") )
                convex_hull.append( (x, y, z, min_w, ".") )

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for w in range(min_w, max_w + 1):
                convex_hull.append( (x, y, max_z, w, ".") )
                convex_hull.append( (x, y, min_z, w, ".") )

    for x in range(min_x, max_x + 1):
        for w in range(min_w, max_w + 1):
            for z in range(min_z, max_z + 1):
                convex_hull.append( (x, max_y, z, w, ".") )
                convex_hull.append( (x, min_y, z, w, ".") )

    for y in range(min_y, max_y + 1):
        for w in range(min_w, max_w + 1):
            for z in range(min_z, max_z + 1):
                convex_hull.append( (max_x, y, z, w, ".") )
                convex_hull.append( (min_x, y, z, w, ".") )

    # create a dictionary from element where duplicates will be removed from
    unique_convex_hull = list(dict.fromkeys(convex_hull))
    cubes += unique_convex_hull
    return cubes

def GetNumberOfActiveCubes(cubes, dims) -> int:
    ret = 0

    for c in cubes:
        if ( c[dims] == "#"):
            ret += 1

    return ret

# print cubes, calculate and return number of active cubes 
def PrintCubes3D(cubes) -> int:

    # sort for x, y and z
    cubes.sort(key = lambda x: (x[0], x[1], x[2]))

    # set min and max +- tolerance
    max_x = max(cubes)[0]
    min_x = min(cubes)[0]
    max_y = max(cubes)[1]
    min_y = min(cubes)[1]
    max_z = max(cubes)[2]
    min_z = min(cubes)[2]

    count = 0

    for z in range(min_z, max_z + 1):
        print("z = {}".format(z))

        for y in range(min_y, max_y + 1):

            for x in range(min_x, max_x + 1):

                if ( (x, y, z, "#") in cubes):
                    print("#", end="")
                    count += 1
                else:
                    print(".", end="")

            print("")

    print("Number of active cubes is {}".format(count))
    return count

# print cubes, calculate and return number of active cubes 
def PrintCubes4D(cubes) -> int:

    # sort for x, y, z and w
    cubes.sort(key = lambda x: (x[0], x[1], x[2], x[3]))

    # set min and max +- tolerance
    max_x = max(cubes)[0]
    min_x = min(cubes)[0]
    max_y = max(cubes)[1]
    min_y = min(cubes)[1]
    max_z = max(cubes)[2]
    min_z = min(cubes)[2]
    max_w = max(cubes)[3]
    min_w = min(cubes)[3]

    count = 0

    for w in range(min_w, max_w + 1):

        for z in range(min_z, max_z + 1):

            print("z = {}, w = {}".format(z, w))

            for y in range(min_y, max_y + 1):

                for x in range(min_x, max_x + 1):

                    if ( (x, y, z, w, "#") in cubes):
                        print("#", end="")
                        count += 1
                    else:
                        print(".", end="")

                print("")

    print("Number of active cubes is {}".format(count))
    return count

def SetActivity3D(data, x, y, z) -> (int, int, int, str):

    cube_is_active = False

    # get current element neighbours
    active_neighbours = []

    # set activity for current element
    if ((x, y, z, "#") in data):
        cube_is_active = True

    # look for active neighbours
    for i in range(x - 1, x + 2):

        for j in range(y - 1, y + 2):

            for k in range(z - 1, z + 2):

                if (((i, j, k, "#") in data) and ((i != x) or (j != y) or (k != z))):
                    active_neighbours.append((i, j, k, "#"))

    # count active neighbours
    count = len(active_neighbours)

    # if sum is 2 or 3 and cube(x, y, z) is active ...
    if (((count == 2) or (count == 3)) and (cube_is_active)):
        return (x, y, z, "#")
    elif ((count == 3) and (not cube_is_active)):
        return (x, y, z, "#")
    else:
        return (x, y, z, ".")

def SetActivity4D(data, x, y, z, w) -> (int, int, int, int, str):

    cube_is_active = False

    # get current element neighbours
    active_neighbours = []

    # set activity for current element
    if ((x, y, z, w, "#") in data):
        cube_is_active = True

    # look for active neighbours
    for i in range(x - 1, x + 2):

        for j in range(y - 1, y + 2):

            for k in range(z - 1, z + 2):

                for l in range(w - 1, w + 2):

                    if (((i, j, k, l, "#") in data) and ((i != x) or (j != y) or (k != z) or (l != w))):
                        active_neighbours.append((i, j, k, l, "#"))

    # count active neighbours
    count = len(active_neighbours)

    # if sum is 2 or 3 and cube(x, y, z) is active ...
    if (((count == 2) or (count == 3)) and (cube_is_active)):
        return (x, y, z, w, "#")
    elif ((count == 3) and (not cube_is_active)):
        return (x, y, z, w, "#")
    else:
        return (x, y, z, w, ".")

def part1(cycles) -> int:
    ret = 0
    data = helper.getData("17")

    # set vars
    cubes = []
    l = len(data[0])
    start = -int((l - 1) / 2)
    y = start
    i = 0

    for e in data:

        x = start

        # add data from file
        for ee in e:
            cubes.append( (x, y, 0, ee) )
            cubes.append( (x, y, -1, ".") )
            cubes.append( (x, y, 1, ".") )
            i += 1
            x += 1

        # next line/data (y increases)
        y += 1

    ExtendCubes3D(cubes)

    # cycle ...
    for cycle in range(1, cycles + 1):
        print("processing cycle: {} ...".format(cycle))
        cubes_new = []

        for cube in cubes:
            cube_new = SetActivity3D(cubes, cube[0], cube[1], cube[2])
            cubes_new.append(cube_new)

        cubes = cubes_new
        ExtendCubes3D(cubes)

    ret = GetNumberOfActiveCubes(cubes, 3)

    return ret

def part2(cycles) -> int:
    ret = 0
    data = helper.getData("17")

    # set vars
    cubes = []
    l = len(data[0])
    start = -int((l - 1) / 2)
    y = start
    i = 0

    for e in data:

        x = start

        # add data from file
        for ee in e:
            cubes.append( (x, y, -1, -1, ".") )
            cubes.append( (x, y, -1, 0, ".") )
            cubes.append( (x, y, -1, 1, ".") )

            cubes.append( (x, y, 0, -1, ".") )
            cubes.append( (x, y, 0, 0, ee) )
            cubes.append( (x, y, 0, 1, ".") )

            cubes.append( (x, y, 1, -1, ".") )
            cubes.append( (x, y, 1, 0, ".") )
            cubes.append( (x, y, 1, 1, ".") )

            i += 1
            x += 1

        # next line/data (y increases)
        y += 1

    ExtendCubes4D(cubes)

    # six cycles
    for cycle in range(1, cycles + 1):
        print("processing cycle: {} ...".format(cycle))
        cubes_new = []

        for cube in cubes:
            cube_new = SetActivity4D(cubes, cube[0], cube[1], cube[2], cube[3])
            cubes_new.append(cube_new)

        cubes = cubes_new

        ExtendCubes4D(cubes)

    ret = GetNumberOfActiveCubes(cubes, 4)

    return ret

# main

print( "Solution for part 1: {}".format(part1(6)) )
print( "Solution for part 2: {}".format(part2(6)) )
