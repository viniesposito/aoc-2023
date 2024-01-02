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
    loop_otherway = [start]
    
    while True:
        loop.append(a)

        if a == b:
            break
        else:
            loop_otherway.append(b)

        a = [x for x in map[a] if x not in loop][0]
        b = [x for x in map[b] if x not in loop_otherway][0]

    loop_otherway.reverse()
    loop = loop + loop_otherway[:-1]

    print(loop)

    def shoelace_formula(points):
        # https://en.wikipedia.org/wiki/Shoelace_formula
        points.append(points[0])

        total = 0

        for point_a, point_b in zip(points, points[1:]):
            total += point_a[0] * point_b[1] - point_a[1] * point_b[0]

        return abs(total) / 2
    
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    return int(shoelace_formula(loop) - len(loop) / 2 + 1 + 1)

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

test4 = """
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""

test5 = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""

print(f"Part 2 test output = {part2(test3)} \n")
print(f"Part 2 test output = {part2(test4)} \n")
print(f"Part 2 test output = {part2(test5)} \n")

print(f"Part 2 output = {part2(input)} \n")