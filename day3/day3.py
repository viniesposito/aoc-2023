import re
from numpy import prod

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

    gears_list = []
    
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
                num = int(line[col_start:col_end])

            gear_idx_in_adjacent = "".join(adjacent).find("*")

            if gear_idx_in_adjacent > -1:
                
                gear_col = col_left + gear_idx_in_adjacent % (col_right - col_left)
                
                gear_row = row + gear_idx_in_adjacent // (col_right - col_left) - 1

                if row_above == 0:
                    gear_row += 1
                elif row_below == num_lines:
                    gear_row -= 1
                
                gears_list.append([(gear_row,gear_col), num])

    gears_num = set(map(lambda x:x[0], gears_list))
    gears_list = [[y[1] for y in gears_list if y[0] == x] for x in gears_num]
    gears_list = [val for val in gears_list if len(val) == 2]
    output = sum([prod(val) for val in gears_list])
    
    print(gears_list)

    return output

print(f"Part 2 test output = {part2(test)} \n")

print(f"Part 2 output = {part2(input)} \n")
