import heapq

test = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

def part1(input):
    
    input = input.strip().splitlines()
    input = [[int(c) for c in r] for r in input]

    origin = 0,0
    end = len(input) - 1, len(input[0]) -1
    m, n = end
    history = set()
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    queue = [(0, origin, (0,0), 0)]

    while queue:
        load, pos, direction, k = heapq.heappop(queue)
        x, y = pos
        dx, dy = direction
        if pos == end:
            break
        if (pos, direction, k) in history:
            continue
        history.add((pos, direction, k))
        for new_direction in directions:
            new_dx, new_dy = new_direction
            if new_dx == -dx and new_dy == -dy:
                continue
            new_x, new_y = x + new_dx, y + new_dy
            new_pos = new_x, new_y
            if new_x < 0 or new_y < 0 or new_x > m or new_y > n:
                continue
            going_straight = (new_direction == direction)
            if going_straight and k == 3:
                continue
            new_k = k + 1 if going_straight else 1
            new_load = load + input[new_x][new_y]
            heapq.heappush(queue, (new_load, new_pos, new_direction, new_k))

    return load

print(f"Part 1 test output = {part1(test)} \n")

with open("day17\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")