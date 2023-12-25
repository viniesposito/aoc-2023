import re

test = """
Time:      7  15   30
Distance:  9  40  200
"""

def part1(input):

    input = [x for x in input.splitlines() if x != ""]
    time_list = re.findall(r"\d+",input[0])
    dist_list = re.findall(r"\d+",input[1])
    
    score = 1

    for t, time in enumerate(time_list):
        count = 0
        time = int(time)
        
        for i in range(time+1):
            dist_traveled = i * (time - i)
            
            if dist_traveled > int(dist_list[t]):
                count += 1

        score *= count

    return score

print(f"Part 1 test output = {part1(test)} \n")

with open("day6\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")

def part2(input):

    input = [x for x in input.splitlines() if x != ""]
    time = int("".join(re.findall(r"\d+",input[0])))
    dist = int("".join(re.findall(r"\d+",input[1])))
    
    count = 0
    
    for i in range(time+1):
        dist_traveled = i * (time - i)
        
        if dist_traveled > dist:
            count += 1
        else:
            if count > 0:
                break

    return count

print(f"Part 2 test output = {part2(test)} \n")

print(f"Part 2 output = {part2(input)} \n")