from itertools import groupby

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

    for pattern in input:
        for i, row in enumerate(pattern):

            reflection = pattern[i+1:]
            reflection.reverse()
            # mirrored_pattern = reflection + pattern

            print("\n".join(mirrored_pattern), "\n")

print(f"Part 1 test output = {part1(test)} \n")