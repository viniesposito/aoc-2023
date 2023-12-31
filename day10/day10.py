test1 = """
.....
.S-7.
.|.|.
.L-J.
.....
"""

test2 = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

def part1(input):

    input = [x for x in input.splitlines() if x != ""]
    
    map = {}

    for i, row in enumerate(input):
        for j, node in enumerate(row):
            
            adjacent = []

            if node in "F|7":
                adjacent.append((i+1,j))
            if node in "|LJ":
                adjacent.append((i-1,j))
            if node in "-J7":
                adjacent.append((i,j-1))
            if node in "F-L":
                adjacent.append((i,j+1))
            if node == "S":
                start = (i,j)
                
            map[(i,j)] = adjacent

    start_adjacent = [k for k, v in map.items() if start in v]
    
    a = start_adjacent[0]
    b = start_adjacent[1]
    
    been = [start]

    steps = 1

    while a != b:
        been.append(a)
        been.append(b)
        
        a = [x for x in map[a] if x not in been][0]
        b = [x for x in map[b] if x not in been][0]

        steps += 1

    return steps

print(f"Part 1 test output = {part1(test1)} \n")
print(f"Part 1 test output = {part1(test2)} \n")

with open("day10\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")

def part2(input):

    input = [x for x in input.splitlines() if x != ""]
    
    map = {}

    for i, row in enumerate(input):
        for j, node in enumerate(row):
            
            adjacent = []

            if node in "F|7":
                adjacent.append((i+1,j))
            if node in "|LJ":
                adjacent.append((i-1,j))
            if node in "-J7":
                adjacent.append((i,j-1))
            if node in "F-L":
                adjacent.append((i,j+1))
            if node == "S":
                start = (i,j)
                
            map[(i,j)] = adjacent

    start_adjacent = [k for k, v in map.items() if start in v]
    
    a = start_adjacent[0]
    b = start_adjacent[1]
    
    loop = [start]

    while True:
        loop.append(a)
        loop.append(b)
        
        if a == b:
            break

        a = [x for x in map[a] if x not in loop][0]
        b = [x for x in map[b] if x not in loop][0]

    for i, row in enumerate(input):
        for j, node in enumerate(row):
            
            # if (i,j) not in loop and node == "." 

test3 = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""

part2(test3)