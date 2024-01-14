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

    def get_neighbors(input, pos, direction, k):
        x, y = pos

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_pos = x + dx, y + dy

            if (dx,dy) == direction:
                k += 1
            else:
                k = 1

            if is_valid(input, new_pos) and k <= 3:
                yield new_pos

    def score_path(input, path):
        score = 0

        if path[0] == (0,0):
            s = 1
        else:
            s = 0

        for x,y in path[s:]:
            score += int(input[x][y])

        return score

    def get_shorter_paths(input, tentative, positions, through):
        path = tentative[through] + [through]

        for pos in positions:
            if pos in tentative and score_path(input, tentative[pos]) > score_path(input, path):
                continue
            yield pos, path

    tentative = {origin: []}
    queue = [(0, origin, (0, 0), 1)]
    certain = set()

    while destination not in certain and queue:
        _, current, direction, k = heapq.heappop(queue)
        if current in certain:
            continue
        certain.add(current)
        neighbors = set(get_neighbors(input, current, direction, k)) - certain
        shorter = get_shorter_paths(input, tentative, neighbors, current)
        for neighbor, path in shorter:
            tentative[neighbor] = path
            new_direction = (neighbor[0] - current[0], neighbor[1] - current[1])
            if new_direction == direction:
                k += 1
                if k > 3:
                    continue
            else:
                k = 1
            heapq.heappush(queue, (score_path(input, path + [neighbor]), neighbor, new_direction, k))
    if destination in tentative:
        best_path = tentative[destination] + [destination]

    print(score_path(input, best_path))

    return best_path

def show_path(path, input):
    input = input.strip().splitlines()
    for x, y in path:
        input[x] = input[x][:y] + "@" + input[x][y + 1 :]
    return "\n".join(input) + "\n"

print(show_path(part1(test),test))

print(f"Part 1 test output = {part1(test)} \n")

# with open("day17\input", "r") as input:
#     input = "".join([val for val in input])

# print(f"Part 1 output = {part1(input)} \n")