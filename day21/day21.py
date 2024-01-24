from heapq import heappush, heappop

test = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""

def part1(input, n):
    input = input.strip().splitlines()
    
    def is_valid(input, pos):
        x, y = pos
        if not (0 <= x < len(input) and 0 <= y < len(input[0])):
            return False
        if input[x][y] == "#":
            return False
        return True
    
    def get_neighbors(input, pos):
        x, y = pos
        for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            new_pos = x + dx, y + dy
            if is_valid(input, new_pos):
                yield new_pos

    init_row = [i for i in range(len(input)) if "S" in input[i]][0]
    init_col = input[init_row].index("S")
    steps = 0
    queue = [(steps, init_row, init_col)]
    while not all([x[0] == n for x in queue]):
        steps, x, y = heappop(queue)
        for new_x, new_y in get_neighbors(input, (x, y)):
            new_steps = steps + 1
            if (new_steps, new_x, new_y) not in queue:
                heappush(queue, (new_steps, new_x, new_y))
        
    return len(queue)

print(f"Part 1 test output = {part1(test, 6)} \n")

with open("day21\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input, 64)} \n")