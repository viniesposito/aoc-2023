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

    rows_have_galaxies = [False for i in range(n_rows)]
    cols_have_galaxies = [False for i in range(n_cols)]

    for i, row in enumerate(input):
        for j, point in enumerate(row):

            if point == "#":
                rows_have_galaxies[i] = True
                cols_have_galaxies[j] = True

    for row_idx in [i for i in range(n_rows) if not rows_have_galaxies[i]]:
        input.insert(row_idx, "." * n_cols)
    
    expanded_input = []

    for row in input:
        for c, col_idx in enumerate([i for i in range(n_cols) if not cols_have_galaxies[i]]):
            row = row[:(c+col_idx)] + "." + row[(c+col_idx):]

        expanded_input.append(row)

    galaxies = []

    for i, row in enumerate(expanded_input):
        for j, point in enumerate(row):

            if point == "#":
                galaxies.append((i,j))
    
    score = 0

    for pair in combinations(galaxies, 2):
        diff_x = abs(pair[0][0] - pair[1][0]) 
        diff_y = abs(pair[0][1] - pair[1][1])

        if diff_y == len(expanded_input[0]) - 1:
            diff_y -= 1
        
        score += (diff_x + diff_y)
    
    return score

print(f"Part 1 test output = {part1(test)} \n")

with open("day11\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")
