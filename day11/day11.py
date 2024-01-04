from itertools import combinations

test = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

def part1(input):

    input = [x for x in input.splitlines() if x != ""]

    n_rows = len(input)
    n_cols = len(input[0])

    rows_have_galaxies = [False for x in range(n_rows)]
    cols_have_galaxies = [False for x in range(n_cols)]

    for i, row in enumerate(input):
        for j, point in enumerate(row):

            if point == "#":
                rows_have_galaxies[i] = True
                cols_have_galaxies[j] = True

    for r, row_idx in enumerate([i for i in range(n_rows) if not rows_have_galaxies[i]]):
        input.insert((r+row_idx), "." * n_cols)
    
    expanded_input = []

    for row in input:
        for c, col_idx in enumerate([i for i in range(n_cols) if not cols_have_galaxies[i]]):
            row = row[:(c+col_idx)] + "." + row[(c+col_idx):]

        expanded_input.append(row)

    galaxies = [(i,j) for i in range(len(expanded_input)) for j in range(len(expanded_input[0])) if expanded_input[i][j] == "#"]  

    score = 0

    for pair in combinations(galaxies, 2):
        steps = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
        
        score += steps
    
    return score

print(f"Part 1 test output = {part1(test)} \n")

with open("day11\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")

def part2(input):

    input = [x for x in input.splitlines() if x != ""]

    n_rows = len(input)
    n_cols = len(input[0])
    expansion = 1_000_000

    rows_with_galaxies = []
    cols_with_galaxies = []

    for i, row in enumerate(input):
        for j, entry in enumerate(row):
            if entry == "#":
                rows_with_galaxies.append(i)
                cols_with_galaxies.append(j)

    rows_without_galaxies = [i for i in range(n_rows) if i not in rows_with_galaxies]
    cols_without_galaxies = [i for i in range(n_cols) if i not in cols_with_galaxies]

    galaxies = [(i,j) for i in range(len(input)) for j in range(len(input[0])) if input[i][j] == "#"]

    def num_empty_between_galaxies(glx1, glx2, mult):
        xrange = range(min(glx1[0],glx2[0]), max(glx1[0],glx2[0]))
        yrange = range(min(glx1[1],glx2[1]), max(glx1[1],glx2[1]))

        empty_rows_traversed = [x for x in rows_without_galaxies if x in xrange]
        empty_cols_traversed = [y for y in cols_without_galaxies if y in yrange]

        expanded_steps = (len(empty_rows_traversed) + len(empty_cols_traversed)) * (mult - 1)

        return expanded_steps

    score = 0

    for pair in combinations(galaxies, 2):
        xsteps = abs(pair[0][0] - pair[1][0])
        ysteps = abs(pair[0][1] - pair[1][1])
        score += xsteps + ysteps + num_empty_between_galaxies(pair[0], pair[1], expansion)
    
    return score

print(f"Part 2 test output = {part2(test)} \n")

print(f"Part 2 output = {part2(input)} \n")