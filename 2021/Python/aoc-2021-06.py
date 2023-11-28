import helper

class fish:

    # a fish class
    def __init__(self, daystolive = 9):
        self.daystolive = daystolive

    def sleep(self):
        self.daystolive -= 1 if self.daystolive else 0

    def babyfish(self):
        self.daystolive = 7
        return fish(9)

def part1():
    data = helper.getData(6)[0].split(',')
    fishs = []

    for d in data:
       fishs.append(fish(int(d)))

    running = True
    day = 0

    while (running):

        for f in fishs:

            if f.daystolive == 0:
                fishs.append( f.babyfish() )

            f.sleep()

        day += 1

        if day == 80:
            running = False
            print("solution for part 1: {}".format(len(fishs)))

def fishsleep(D):
    # 0 must be stored
    zeros = D[0]

    # decrease days for remaining days in dictionary
    for i in range(0, 9):
        D.update({i - 1:D[i]})
        D.update({i:0})

    # add fish with 6 remaining days and zeros 
    D.update({6:D[6] + zeros})
    # new fish with 8 remaining days
    D.update({8:zeros})

    return D

def fishinit(data):
    # use dictionary
	D = {}

    # values between 0 and 8 represent remaining days
	for i in range(0, 9):
		s = sum(1 for d in data if int(d) == i)
		D.update({i:s})

	return D

def fishcount(D):
    sum = 0

    # count values in dictionary -> number of all fishes
    for i in range(0, 9):
        sum += D[i]

    return sum

def part2():
    data = helper.getData(6)[0].split(',')
    D = fishinit(data)

    for _ in range(1, 257):
        D = fishsleep(D)

    print("solution for part 1: {}".format(fishcount(D)))


# main
part1()
part2()