import helper

def part1():

    # read data and cast to int
    data = helper.getData(8)

    tmp = []
    for d in data:

        # check only right side
        rside = d.split(' | ')[1].split(' ')
        
        for r in rside:
            # digit 1 = 2 elements
            # digit 4 = 4 elements
            # digit 7 = 3 elements
            # digit 8 = 7 elements

            # digit 1, 4, 7 and 8 have unique elements
            # get elements in rside with that length
            if len(r) == 2 or len(r) == 4 or len(r) == 3 or len(r) == 7:
                tmp.append(r)

    count = len(tmp)

    print("solution for part 1: {}".format(count))

def part2():
    pass

# main
part1()
#part2()
