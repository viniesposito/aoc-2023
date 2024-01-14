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
    origin = 0, 0
    destination = len(input) - 1, len(input[0]) - 1

    def is_valid(input, pos):
        x, y = pos
        m = len(input)
        n = len(input[0])

        if not (0 <= x < m and 0 <= y < n):
            return False
        
        return True

    def get_neighbors(input, pos):
        x, y = pos

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                new_pos = x + dx, y + dy

                if is_valid(input, new_pos):
                    yield new_pos

    def get_shorter_paths(tentative, positions, through):
        path = tentative[through] + [through]

        for pos in positions:
            if pos in tentative and len(tentative[pos]) <= len(path):
                continue
            yield pos, path

    tentative = {origin: []}
    queue = [(0, origin)]
    certain = set()

    while destination not in certain and queue:
        _, current = heapq.heappop(queue)
        if current in certain:
            continue
        certain.add(current)
        neighbors = set(get_neighbors(input, current)) - certain
        shorter = get_shorter_paths(tentative, neighbors, current)
        for neighbor, path in shorter:
            tentative[neighbor] = path
            heapq.heappush(queue, (len(path), neighbor))
    if destination in tentative:
        best_path = tentative[destination] + [destination]

    return len(best_path)

print(f"Part 1 test output = {part1(test)} \n")

# with open("day17\input", "r") as input:
#     input = "".join([val for val in input])

# print(f"Part 1 output = {part1(input)} \n")