test = """
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\ 
..../.\\\.. 
.-.-/..|..
.|....-|.\ 
..//.|....
"""

def part1(input):

    input = [x.strip() for x in input.strip().splitlines()]

    queue = [[0, 0, "right"]]
    history = []
    energized = []

    ny = len(input)
    nx = len(input[0])

    while queue:

        x, y, direction = queue.pop()
        energized.append((x, y))
        
        char = input[x][y]

        if [x, y + 1, "right"] not in history and y + 1 < ny:
            if ((direction == "down" and char in "\\-") or (direction == "up" and char in "/-") or
                (direction == "right" and char in "-.")):
                next = [x, y + 1, "right"]
                queue.append(next)
                history.append(next)

        if [x + 1, y, "down"] not in history and x + 1 < nx:
            if ((direction == "right" and char in "\\|") or (direction == "down" and char in "|.") or
                (direction == "left" and char in "/|")):
                next = [x + 1, y, "down"]
                queue.append(next)
                history.append(next)

        if [x, y - 1, "left"] not in history and y > 0:
            if ((direction == "up" and char in "\-") or (direction == "down" and char in "/-") or
                (direction == "left" and char in ".-")):
                next = [x, y - 1, "left"]
                queue.append(next)
                history.append(next)

        if [x - 1, y, "up"] not in history and x > 0:
            if ((direction == "up" and char in ".|") or (direction == "right" and char in "/|") or
                (direction == "left" and char in "\\|")):
                next = [x - 1, y, "up"]
                queue.append(next)
                history.append(next)

    return len(set(energized))

print(f"Part 1 test output = {part1(test)} \n")

with open("day16\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")

def part2(input):
    input = [x.strip() for x in input.strip().splitlines()]

    ny = len(input)
    nx = len(input[0])

    starts = [[0, j, "down"] for j in range(ny)]
    starts.extend([[nx - 1, j, "up"] for j in range(ny)])
    starts.extend([[i, 0, "right"] for i in range(nx)])
    starts.extend([[ny - 1, 0, "left"] for i in range(nx)])

    energized_list = []

    for s, start in enumerate(starts):
        
        queue = [start]
        history = []
        energized = []

        while queue:

            x, y, direction = queue.pop()
            energized.append((x, y))
            
            char = input[x][y]

            if [x, y + 1, "right"] not in history and y + 1 < ny:
                if ((direction == "down" and char in "\\-") or (direction == "up" and char in "/-") or
                    (direction == "right" and char in "-.")):
                    next = [x, y + 1, "right"]
                    queue.append(next)
                    history.append(next)

            if [x + 1, y, "down"] not in history and x + 1 < nx:
                if ((direction == "right" and char in "\\|") or (direction == "down" and char in "|.") or
                    (direction == "left" and char in "/|")):
                    next = [x + 1, y, "down"]
                    queue.append(next)
                    history.append(next)

            if [x, y - 1, "left"] not in history and y > 0:
                if ((direction == "up" and char in "\-") or (direction == "down" and char in "/-") or
                    (direction == "left" and char in ".-")):
                    next = [x, y - 1, "left"]
                    queue.append(next)
                    history.append(next)

            if [x - 1, y, "up"] not in history and x > 0:
                if ((direction == "up" and char in ".|") or (direction == "right" and char in "/|") or
                    (direction == "left" and char in "\\|")):
                    next = [x - 1, y, "up"]
                    queue.append(next)
                    history.append(next)

        energized_list.append(len(set(energized)))

        print(f"Start {s+1}/{len(starts)} done.")

    return max(energized_list)

print(f"Part 2 test output = {part2(test)} \n")

print(f"Part 2 output = {part2(input)} \n")