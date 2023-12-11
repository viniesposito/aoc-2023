import re

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


