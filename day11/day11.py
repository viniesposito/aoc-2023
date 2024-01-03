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
    expansion = int(1e2)

    rows_with_galaxies = []
    cols_with_galaxies = []

    for i, row in enumerate(input):
        for j, entry in enumerate(row):
            if entry == "#":
                rows_with_galaxies.append(i)
                cols_with_galaxies.append(j)

    rows_without_galaxies = [i for i in range(n_rows) if i not in rows_with_galaxies]
    cols_without_galaxies = [i for i in range(n_cols) if i not in cols_with_galaxies]

    skip = 0

    for r, row in enumerate(input):
        if r in rows_without_galaxies:
            input = input[:(skip+r)] + ["." * n_cols] * (expansion - 1) + input[(skip+r):]
            skip += (expansion - 1)

    input_expanded = []

    for row in input:
        skip = 0
        temp = row

        for c, entry in enumerate(row):
            if c in cols_without_galaxies:
                temp = temp[:(skip+c)] + "." * (expansion - 1) + temp[(skip + c):]
                skip += (expansion - 1)

        input_expanded.append(temp)

    galaxies = [(i,j) for i in range(len(input_expanded)) for j in range(len(input_expanded[0])) if input_expanded[i][j] == "#"]

    score = 0

    for pair in combinations(galaxies, 2):
        steps = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
        score += steps
    
    return score

print(f"Part 2 test output = {part2(test)} \n")