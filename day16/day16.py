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