import re

test = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

def part1(input):
    input = input.strip()
    x, y = 0, 0
    bounds = [(x,y)]
    directions = {
        "R": (0, 1),
        "L": (0, -1),
        "D": (1, 0),
        "U": (-1, 0)
    }
    
    for direction, nsteps, _ in re.findall(r"(\w) (\d+) (\(#\w+\))",input):
        dx, dy = directions[direction]
        for _ in range(int(nsteps)):
            x += dx
            y += dy
            if (x,y) != (0, 0):
                bounds.append((x,y))
    
    def shoelace_formula(points):
        # https://en.wikipedia.org/wiki/Shoelace_formula
        points.append(points[0])

        total = 0

        for point_a, point_b in zip(points, points[1:]):
            total += point_a[0] * point_b[1] - point_a[1] * point_b[0]

        return abs(total) / 2

    def picks_theorem(bounds):
        return int(shoelace_formula(bounds) - len(bounds) / 2 + 1 + 1)

    return len(bounds) + picks_theorem(bounds)

print(f"Part 1 test output = {part1(test)} \n")

with open("day18\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")

def part2(input):
    input = input.strip()
    x, y = 0, 0
    bounds = [(x,y)]
    perimeter = 0
    directions = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    
    for nsteps, direction in re.findall(r"#(\w{5})([0-3])",input):
        dx, dy = directions[int(direction)]
        x += dx * int(nsteps, 16)
        y += dy * int(nsteps, 16)
        perimeter += int(nsteps, 16)
        if (x,y) != (0, 0):
            bounds.append((x,y))
    
    def shoelace_formula(points):
        # https://en.wikipedia.org/wiki/Shoelace_formula
        points.append(points[0])

        total = 0

        for point_a, point_b in zip(points, points[1:]):
            total += point_a[0] * point_b[1] - point_a[1] * point_b[0]

        return abs(total) / 2

    def picks_theorem(bounds):
        return int(shoelace_formula(bounds) - len(bounds) / 2 + 1 + 1)

    return int(shoelace_formula(bounds) + perimeter / 2 + 1)

print(f"Part 2 test output = {part2(test)} \n")

print(f"Part 2 output = {part2(input)} \n")
