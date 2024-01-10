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
        
        mirrors = []

        for i, _ in enumerate(entry):
            if i > 0:
                if entry[i] == entry[i-1]:
                    rows_above = i - 1
                    rows_below = len(entry) - i - 1

                    above = entry[:rows_above]
                    below = entry[-rows_below:]

                    floor = min(rows_above, rows_below)
                    above = above[-floor:]
                    below = below[:floor]
                    below.reverse()

                    if above == below:
                        mirrors.append(i)

        return np.array(mirrors)
    
    score = 0

    for entry in input:
        horizontal_mirrors = find_mirrors(entry)
        vertical_mirrors = find_mirrors(transpose(entry))

        score += np.sum(100 * horizontal_mirrors) + np.sum(vertical_mirrors)

    return score

print(f"Part 1 test output = {part1(test)} \n")

with open("day13\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")