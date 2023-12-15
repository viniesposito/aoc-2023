import re
from math import prod

test = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

def part1(input):

    score = 0
    
    input = [val for val in input.split("\n") if val != ""]
    num_lines = len(input)
    
    for row, line in enumerate(input):
        
        for match in re.finditer(r"\d+", line):
            col_start = match.start()
            col_end = match.end()

            row_above = max(row - 1,0)
            row_below = min(row + 1,num_lines)+1

            col_left = max(col_start - 1, 0)
            col_right = min(col_end + 1, len(line))

            adjacent = [i[col_left:col_right] for i in input[row_above:row_below]]
            
            pattern = r"[^.0-9]+"
            
            if re.findall(pattern,"".join(adjacent)):
                score += int(line[col_start:col_end])

    return score

print(f"Part 1 test output = {part1(test)} \n")

with open("day3\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")

def part2(input):

    input = [val for val in input.splitlines() if val != ""]
    
    n = len(input)

    data = [[[[], False] for y in x] for x in input]

    for r, line in enumerate(input):

        for match in re.finditer(r"\d+", line):
            s = match.start()
            e = match.end()
            m = len(line)

            adjacent = [val[max(0, s-1):min(e+1,m)] for val in input[max(0,r-1):(1+min(r+1,n))]]

            if [val for val in "".join(adjacent) if val != "." and not val.isdigit()]:
                num = int(line[s:e])
                

                for i in range(max(0,r-1),min(r+2,n)):
                    for j in range(max(0,s-1),(min(e+1,m))):
                        
                        data[i][j][0].append(num)
                        
                        if input[i][j] == "*":
                            data[i][j][1] = True
                        
    gears = [[y for y in x if len(y[0]) == 2 and y[1]] for x in data]

    score = 0

    gear_ratios = []

    for gear in gears:
        if gear:
            for entry in gear:
                
                score += entry[0][0]*entry[0][1]
                gear_ratios.append(entry[0][0]*entry[0][1])

    return score

print(f"Part 2 test output = {part2(test)} \n")

print(f"Part 2 output = {part2(input)} \n")
