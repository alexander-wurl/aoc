import helper

data = helper.getData(5)

def verticals(x1, y1, x2, y2, M):
    if (y1 == y2 and x2 > x1):
        for x in range(x1, x2 + 1):
            M[y2][x] = '1' if M[y2][x] == '.' else '2'
    elif (y1 == y2 and x2 <= x1):
        for x in range(x2, x1 + 1):
            M[y2][x] = '1' if M[y2][x] == '.' else '2'

def horizontals(x1, y1, x2, y2, M):
    if ((x1 == x2) and (y2 > y1)):
        for y in range(y1, y2 + 1):
            M[y][x2] = '1' if M[y][x2] == '.' else '2'  
    elif ((x1 == x2) and (y2 <= y1)):
        for y in range(y2, y1+1):
            M[y][x2] = '1' if M[y][x2] == '.' else '2'

def diagonals(x1, y1, x2, y2, M):
    if ((x1 != x2) and (y1 != y2)):

        # for left heading diagonal increase x  
        xstep = 1 if (x1 < x2) else -1

        # for right heading diagonal decrease x  
        ystep = 1 if (y1 < y2) else -1

        # diagonals start
        x, y = x1, y1

        # move along diagonal and set marker
        while x != (x2 + xstep):
            M[y][x] = '1' if M[y][x] == '.' else '2'
            x = x + xstep
            y = y + ystep

def part1():

    # remove ' -> ' and split by comma
    R = [ d.replace(' -> ', ',').split(',') for d in data ]

    # cast to integer
    I = [ [int(e[i]) for i in range(0, 4) ] for e in R ]

    # max values from first and third column and second and fourth column 
    xmax = max([e[0] for e in I] + [e[2] for e in I])
    ymax = max([e[1] for e in I] + [e[3] for e in I])

    # init matrix M[0 ... xmax + 1][0 ... ymax + 1] with .
    M = [ ['.' for x in range(xmax + 1)] for y in range(ymax+1) ]
    
    # from each line ...
    for e in I:
        # ... get x, y coordinates
        x1, y1, x2, y2 = e[0], e[1], e[2], e[3]

        # verticals
        verticals(x1, y1, x2, y2, M)

        # horizontals
        horizontals(x1, y1, x2, y2, M)

    # count 2 in M
    count = sum([1 for e in M for i in range(xmax + 1) if e[i] == '2'])
    print("solution for part 1: {}".format(count))

def part2():

    # remove ' -> ' and split by comma
    R = [ d.replace(' -> ', ',').split(',') for d in data ]

    # cast to integer
    I = [ [int(e[i]) for i in range(0, 4) ] for e in R ]

    # max values from first and third column and second and fourth column 
    xmax = max([e[0] for e in I] + [e[2] for e in I])
    ymax = max([e[1] for e in I] + [e[3] for e in I])

    # init matrix M[0 ... xmax + 1][0 ... ymax + 1] with .
    M = [ ['.' for x in range(xmax + 1)] for y in range(ymax+1) ]
    
    # from each line ...
    for e in I:
        # ... get x, y coordinates
        x1, y1, x2, y2 = e[0], e[1], e[2], e[3]

        # verticals
        verticals(x1, y1, x2, y2, M)

        # horizontals
        horizontals(x1, y1, x2, y2, M)

    for e in I:
        # ... get x, y coordinates
        x1, y1, x2, y2 = e[0], e[1], e[2], e[3]
        
        # diagonals
        diagonals(x1, y1, x2, y2, M)

    # count 2 in M
    count = sum([1 for e in M for i in range(xmax + 1) if e[i] == '2'])
    print("solution for part 2: {}".format(count))

# main
part1()
part2()

