#!/usr/bin/env python
from collections import deque

def isInDict(found, memory) -> int:
    ret = 0

    l = list(memory.items())[:-1]

    for key, value in l:
        if value == found:
            ret = key
            break

    return ret

def startGame(n: int):

    memory = {1: 14, 2: 3, 3: 1, 4: 0, 5: 9, 6: 5}
    currentTurn = list(memory)[-1] + 1

    while (currentTurn <= n):

        lastValue = memory.get(currentTurn - 1)
        index = isInDict(lastValue, memory)

        if (index > 0):
            numberSpoken = (currentTurn - 1) - index
            del memory[index]
        else:
            numberSpoken = 0

        memory[currentTurn] = numberSpoken
        currentTurn += 1

    return numberSpoken

# main

# part 1
print("solution for part 1: {}".format(startGame(2020)))

# part 2
#print("solution for part 1: {}".format(startGame(30000000)))
