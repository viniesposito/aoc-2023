import re
import numpy as np

test = """
    0 3 6 9 12 15
    1 3 6 10 15 21
    10 13 16 21 30 45
"""

def part1(input):

    input = [re.findall(r"-?\d+", x) for x in input.splitlines() if x != ""]
    input = [np.array(list(map(int, x))) for x in input]
    
    score = 0

    for r in input:
        diffs = [r]
        while not all(diffs[-1] == 0):
            diffs.append(np.diff(diffs[-1]))
        
        for i in range(-2, -len(diffs) - 1, -1):
            next_num = diffs[i][-1] + diffs[i+1][-1]
            diffs[i] = np.append(diffs[i], next_num)

        score += diffs[0][-1]

    return score
            
            
print(f"Part 1 test output = {part1(test)} \n")

with open("day9\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")

def part2(input):

    input = [re.findall(r"-?\d+", x) for x in input.splitlines() if x != ""]
    input = [np.array(list(map(int, x))) for x in input]
    
    score = 0

    for r in input:
        diffs = [r]
        while not all(diffs[-1] == 0):
            diffs.append(np.diff(diffs[-1]))
        
        for i in range(-2, -len(diffs) - 1, -1):
            prev_num = diffs[i][0] - diffs[i+1][0]
            diffs[i] = np.insert(diffs[i], 0, prev_num)

        score += diffs[0][0]

    return score
            
            
print(f"Part 2 test output = {part2(test)} \n")

print(f"Part 2 output = {part2(input)} \n")
