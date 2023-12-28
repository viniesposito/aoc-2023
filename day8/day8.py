from math import lcm

test1 = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

test2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

def part1(input):

    input = [x for x in input.splitlines() if x != ""]

    instructions = input[0]
    input = input[1:]
    
    network_dict = {x[:3]:[x[7:10], x[-4:-1]] for x in input}
    
    steps = 0
    node = "AAA"

    while node != "ZZZ":
        
        instruction = instructions[steps % len(instructions)]
    
        if instruction == "L":
            node = network_dict[node][0]
        else:
            node = network_dict[node][1]
        
        steps += 1

    return steps

print(f"Part 1 test output = {part1(test1)} \n")
print(f"Part 1 test output = {part1(test2)} \n")

with open("day8\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")

test3 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

def part2(input):
    
    input = [x for x in input.splitlines() if x != ""]

    instructions = input[0]
    input = input[1:]
    
    network_dict = {x[:3]:[x[7:10], x[-4:-1]] for x in input}
    
    nodes = [n for n in network_dict.keys() if n[-1] == "A"]
    
    steps_list = []

    for node in nodes:
        steps = 0

        while node[-1] != "Z":
        
            instruction = instructions[steps % len(instructions)]
            
            if instruction == "L":
                node = network_dict[node][0]
            else:
                node = network_dict[node][1]
            
            steps += 1
        
        steps_list.append(steps)
        
    return lcm(*steps_list)

print(f"Part 2 test output = {part2(test3)} \n")

print(f"Part 2 output = {part2(input)} \n")