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
    print(instructions)
    print(network_dict)
    steps = 0
    node = input[0][:3]

    while node != "ZZZ":
        # print(steps)
        instruction = instructions[steps % len(instructions)]
        # print(instruction)
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