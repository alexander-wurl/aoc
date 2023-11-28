#!/usr/bin/env python3

import helper

def part1():
	f = helper.getData("2")

	solution = 0

	for line in f:
		w = line.split(" ")
		mm = w[0].split("-")
		min = mm[0]
		max = mm[1]
		c = w[1][0]
		count = w[2].count(c)

		if (count >= int(min)) and (count <= int(max)):
			solution += 1

	return solution

# main
print("solution for part 1: {}".format(part1()))
