import helper


def countrhombus(M):
    ret = 0
    for e in M:
        for r in e:
            if r == '#': ret += 1
    return ret

def part1():

    data = helper.getData(13)

    rows = 0
    columns = 0

    for e in data:
        if e != "":
            tmp = e.split(",")
            if len(tmp) > 1:
                if (int(tmp[0]) > rows): rows = int(tmp[0])
                if (int(tmp[1]) > columns): columns = int(tmp[1])

    # set data without folding instructions
    M = [ ["." for row in range(rows + 1)] for column in range(columns + 1) ]

    # set folding instruction
    F = []

    for e in data:
        if e != "":
            tmp = e.split(",")
            if len(tmp) > 1:
                x = int(tmp[0])
                y = int(tmp[1])
                M[y][x] = "#"
            else:
                tmp = str(str(e).split(" ")[2]).split("=")
                axis = tmp[0]
                value = tmp[1]
                F.append([axis, value])


    # y = fold horizontal
    #horizontalline = 7
    #M = foldhorizontal(M, horizontalline)

    # x = fold vertical
    verticalline = 655
    M = foldvertical(M, verticalline)

    print("solution for part 1: {}".format(countrhombus(M)))


# x = fold vertical
def foldvertical(M, verticalline):
    # horizontal length
    columns = len(M[0])
    # vertical length
    rows = len(M)

    for column in range(verticalline + 1, columns):
        for row in range(0, rows):
            if M[row][column] == '#':
                M[row][columns - column - 1] = M[row][column]

    # set N ...
    ret = [ ["." for column in range(verticalline)] for row in range(rows) ]
    # ... and values for combined side
    for row in range(rows):
        for column in range(verticalline):
            ret[row][column] = M[row][column]

    return ret

# y = fold horizontal
def foldhorizontal(M, horizontalline):
    # horizontal length
    columns = len(M[0])
    # vertical length
    rows = len(M)

    # 
    for column in range(0, columns):
        for row in range(rows - 1, horizontalline + 1, -1):
            # fx, fy = values from bottom to horizontal line
            fx = column
            fy = rows - (row + 1)
            # overwrite top part if bottom is '#'
            if (M[row][column] == '#'):
                M[(rows - 1) - row][column] = M[row][column]

    N = [ ["." for column in range(columns)] for row in range(horizontalline) ]

    # set N with new values
    for column in range(columns):
        for row in range(horizontalline):
            N[row][column] = M[row][column]

    return(N)

# main
part1()

