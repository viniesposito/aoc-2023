import re

test = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

def part1(input):

    input = [x for x in input.splitlines() if x != ""]

    score = 0

    for row in input:
        numbers = row.split(":")[1].split("|")
        [winning_nums,nums_chosen] = [re.findall(r"\d+",numbers[0]), re.findall(r"\d+",numbers[1])]
        
        wins = []

        for num in nums_chosen:
            if num in winning_nums:
                wins.append(num)
        
        if wins:
            score += 2**(len(wins)-1)

    return score

print(f"Part 1 test output = {part1(test)} \n")

with open("day4\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")

def part2(input):
    
    input = [x for x in input.splitlines() if x != ""]

    score = [1 for x in input]
    
    for i, row in enumerate(input):
        numbers = row.split(":")[1].split("|")
        [winning_nums,nums_chosen] = [re.findall(r"\d+",numbers[0]), re.findall(r"\d+",numbers[1])]
        
        wins = []

        for num in nums_chosen:
            if num in winning_nums:
                wins.append(num)
        
        n_wins = len(wins)
        
        for j in range(i+1,i+n_wins+1):
            
            score[j] += score[i]

    return sum(score)

print(f"Part 2 test output = {part2(test)} \n")

print(f"Part 2 output = {part2(input)} \n")
