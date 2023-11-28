import helper

def printM(M):
    for e in M:
        print(e)

def increaseEnergy(M):
    for i in range(10):
        for j in range(10):
            M[i][j] += 1

def flash(M):
    for i in range(10):
        for j in range(10):
            if M[i][j] > 9:
                M[i][j] = 0
                increaseAdjacent(M, i, j)

def increaseAdjacent(M, i, j):
    for k in range (i - 1, i + 2):
        for l in range (j - 1, j + 2):
            if ((k > -1 and k < 10) and (l > -1 and l < 10) and (M[k][l] != 0)):
                M[k][l] += 1
                flash(M)

def countFlashes(M):
    ret = 0
    for i in range(10):
        for j in range(10):
            if M[i][j] == 0:
                ret += 1
    return ret

def initM(data):
    M = [ [0 for x in range(10)] for y in range(10) ]

    i = 0
    j = 0

    for e in data:
        for el in e:
            M[j][i] = int(el)
            i += 1

        i = 0
        j += 1
    return M

def part1():
    data = helper.getData(11)
    M = initM(data)

    flashes = 0

    for step in range(1, 101):
        increaseEnergy(M)
        flash(M)
        flashes += countFlashes(M)

    print("solution for part 1: {}".format(flashes))

# main
part1()