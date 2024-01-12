test = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

def part1(input):
    
    input = input.split(",")
    
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