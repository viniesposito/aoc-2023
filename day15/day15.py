import re

test = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

def part1(input):
    
    input = input.strip().split(",")
    
    def hash(step):

        output = 0

        for char in step:
            output += ord(char)
            output *= 17
            output %= 256

        return output
    
    return sum(hash(step) for step in input)

print(f"Part 1 test output = {part1(test)} \n")

with open("day15\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")

def part2(input):

    input = input.strip().split(",")

    def hash(step):

        output = 0

        for char in step:
            output += ord(char)
            output *= 17
            output %= 256

        return output

    boxes = {i:{} for i in range(256)}

    for step in input:
        label = re.search(r"^[a-z]+", step).group()
        operation = re.search(r"-|=", step).group()
        if focal_length := re.search(r"\d$", step):
            focal_length = int(focal_length.group())
        
        box = hash(label)

        if operation == "-":
            if label in boxes[box]:
                boxes[box].pop(label)
        
        if operation == "=":
            boxes[box][label] = focal_length

        focusing_power = 0

        for box in boxes:
            for i, slot in enumerate(boxes[box]):
                focusing_power += (1 + box) * (1 + i) * boxes[box][slot]

    return focusing_power

print(f"Part 2 test output = {part2(test)} \n")

print(f"Part 2 output = {part2(input)} \n")