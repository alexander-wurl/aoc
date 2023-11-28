import helper

data = helper.getData(4)

def marking(board, number):
    # look for number in board, if found replace value by 'X'
    board = [['X' if e == number else e for e in board[i]] for i in range(0,5)]
    return(board)

def unmarked(board):
    # make a single list containing all elements in board
    L = [ e[i] for e in board for i in range(0, 5) ]

    # replace 'X' with '0'
    R = [ '0' if e == 'X' else e for e in L ]

    # cast string elements to integer and return 
    I = [int(e) for e in R]
    return I

def bingo(board, number):
    ret = 0

    # verticals
    for i in range(0, 5):
        verticals = [e[i] for e in board]
        # in case of bingo return sum of unmarked values * number
        if all(x in 'X' for x in verticals):
            return True

    # horizontals
    for h in range(0, 5):
        horizontals = board[h]
        if all(x in 'X' for x in horizontals):
            return True

    return ret

def part1():

    # 100 numbers
    numbers = data[0].split(',')

    # 500 rows
    rows = [e.split() for e in data[1:] if e != '']

    # 100 board's * 25 int's
    boards = [ rows[i:i+5] for i in range(0, len(rows),5)]

    # get a number and check each board for bingo
    for number in numbers:
        for j in range(0, len(boards)):
            boards[j] = marking(boards[j], number)
            if bingo(boards[j], number):
                s = sum(unmarked(boards[j])) * int(number)
                print("solution for part 1: {}".format(s))
                return

def last(boardlist, n):
    # remove board number from boardlist 
    if n in boardlist:
        boardlist.remove(n)
        # if no board to remove ...
        if len(boardlist) == 0:
            # this must be the last board to win!
            return True
    return False

def part2():
    # 100 numbers
    numbers = data[0].split(',')

    # 500 rows
    rows = [e.split() for e in data[1:] if e != '']

    # 100 board's * 25 int's
    boards = [ rows[i:i+5] for i in range(0, len(rows),5)]

    # list with board numbers
    boardlist = [i for i in range(0,99)]

    # get a number and check each board for bingo
    for number in numbers:
        for j in range(0, len(boards)):
            boards[j] = marking(boards[j], number)

            if bingo(boards[j], number):
                # check for last board to win
                if (last(boardlist, j)):
                    s = sum(unmarked(boards[j])) * int(number)
                    print("solution for part 2: {}".format(s))

# main
part1()
part2()