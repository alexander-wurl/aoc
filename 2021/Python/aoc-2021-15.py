from requests import NullHandler
import helper

class node:
    def __init__(self, row, column, M) -> None:
 
        # size 
        rows = len(M) - 1
        columns = len(M) - 1
        
        # error handling
        if row > rows or column > columns:
            return

        # set position for node
        self.row = row
        self.column = column
        
        # neighbours are located horizontal and vertical
        self.Neighbours = {}

        # visited
        self.visited = False

        # distance to start node
        self.distance = 99999

        # risk value/risk value
        self.value = M[row][column]

        # predecessor
        self.predecessor = NullHandler

        # neighbours
        if row == 0 and column == 0:
            # START, 2 neighbours (row, column)
            self.Neighbours.update({"bottom": [1, 0]})
            self.Neighbours.update({"right": [0, 1]})
            # no 'risk level'
            self.distance = 0
        elif row == rows and column == columns:
            # END, 2 neighbours
            self.Neighbours.update({"top": [rows - 1, column]})
            self.Neighbours.update({"left": [row, column - 1]})
        elif row == 0 and column == columns:
            # top right, 2 neighbours
            self.Neighbours.update({"bottom": [row + 1, column]})
            self.Neighbours.update({"left": [row, column - 1]})
        elif column == 0 and row == rows:
            # bottom left, 2 neighbours
            self.Neighbours.update({"top": [row - 1, column]})
            self.Neighbours.update({"right": [row, column + 1]})
        elif column == 0:
            # (1), 3 neighbours
            self.Neighbours.update({"top": [row - 1, column]})
            self.Neighbours.update({"bottom": [row + 1, column]})
            self.Neighbours.update({"right": [row, column + 1]})
        elif column == columns:
            # (2), 3 neighbours
            self.Neighbours.update({"top": [row - 1, column]})
            self.Neighbours.update({"bottom": [row + 1, column]})
            self.Neighbours.update({"left": [row, column - 1]})
        elif row == 0:
            # (3), 3 neighbours
            self.Neighbours.update({"left": [row, column - 1]})
            self.Neighbours.update({"right": [row, column + 1]})
            self.Neighbours.update({"bottom": [row + 1, column]})
        elif row == rows:
            # (4), 3 neighbours
            self.Neighbours.update({"left": [row, column - 1]})
            self.Neighbours.update({"right": [row, column + 1]})
            self.Neighbours.update({"top": [row - 1, column]})
        else:
            # 4 neighbours
            self.Neighbours.update({"left": [row, column - 1]})
            self.Neighbours.update({"right": [row, column + 1]})
            self.Neighbours.update({"top": [row - 1, column]})
            self.Neighbours.update({"bottom": [row + 1, column]})

def distanceupdate(Graph, u, v):
    newdist = u.distance + v.value
    if newdist < v.distance:
        v.distance = newdist
        v.predecessor = u

def getnode(Graph, row, column):
    for n in Graph:
        if n.row == row and n.column == column:
            return n

def getnodewithsmallestdistance(Graph):
    min = 99999
    minq = NullHandler
    for q in Graph:
        if (q.distance <= min) and (q.visited == False):
            min = q.distance
            minq = q
    minq.visited = True
    return minq

def setmatrix(data):
    rows = 0
    columns = 0

    # get size from first line/row
    for r in data[0]:
        for c in r:
            columns += 1
        rows += 1

    # init M
    M = [[0 for r in range(rows)] for c in range(columns)]
    
    # set data, data = M :)
    for row in range(0, rows):
        for column in range(0, columns):
            M[row][column] = int( data[row][column] )

    return rows, columns, M

def part1():

    data = helper.getData(15)
    
    rows, columns, M = setmatrix(data)
    Graph = []

    for row in range(0, rows):
        for column in range(0, columns):
            Graph.append(node(row, column, M))

    # Dijkstra
    # get node u with smallest distance (first time start node)
    u = getnodewithsmallestdistance(Graph)

    # as long as u was marked not visited
    while u != NullHandler:

        # get u's neighbour
        neighbours = u.Neighbours

        # update distance and predecessor if shorter path was found
        for n in neighbours:
            row = neighbours[n][0]
            column = neighbours[n][1]
            v = getnode(Graph, row, column)
            distanceupdate(Graph, u, v)

        u = getnodewithsmallestdistance(Graph)

    # finally print distance to start (last node)
    lastnode = Graph[len(Graph) - 1]
    print("solution for part 1: {}".format(lastnode.distance))

# main
part1()

