from itertools import groupby
import numpy as np

test = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

def part1(input):

    input = input.strip().splitlines()
    input = [list(g) for k, g in groupby(input, key = bool) if k]

    def transpose(entry):
        return ["".join(x) for x in list(map(list, zip(*entry)))]

    def find_mirrors(entry):

        for i in range(1, len(entry)):
            if all(a == b for a, b in zip(reversed(entry[:i]), entry[i:])):
                return i
            
        return 0

    score = 0

    for entry in input:
        if horiz_mirror := find_mirrors(entry):
            score += 100 * horiz_mirror
        
        if vert_mirror := find_mirrors(transpose(entry)):
            score += vert_mirror

    return score

print(f"Part 1 test output = {part1(test)} \n")

with open("day13\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")

def part2(input):
        
    input = input.strip().splitlines()
    input = [list(g) for k, g in groupby(input, key = bool) if k]

    def transpose(entry):
        return ["".join(x) for x in list(map(list, zip(*entry)))]
    
    def difference(a, b):
        return sum(x != y for x,y in zip(a, b))

    def find_mirrors(entry):

        for i in range(1, len(entry)):
            if sum(difference(a,b) for a, b in zip(reversed(entry[:i]), entry[i:])) == 1:
                return i
            
        return 0

    score = 0

    for entry in input:
        if horiz_mirror := find_mirrors(entry):
            score += 100 * horiz_mirror
        
        if vert_mirror := find_mirrors(transpose(entry)):
            score += vert_mirror

    return score

print(f"Part 2 test output = {part2(test)} \n")

print(f"Part 2 output = {part2(input)} \n")