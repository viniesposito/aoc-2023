test = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""" 

def part1(input):
    
    input = input.strip().splitlines()

    def tilt_east(row):
        return "#".join(["".join(sorted(x)) for x in row.split("#")])

    def tilt_block_east(block):
        return [tilt_east(x) for x in block]

    def rotate_cw(block):
        return ["".join(x) for x in list(zip(*block[::-1]))]
    
    def rotate_ccw(block):
        return ["".join(x) for x in list(reversed(list(zip(*block[::]))))]
    
    def repeat_func(func, ntimes, x):
        for i in range(ntimes):
            x = func(x)

        return x
    
    def tilt(block, direction):
        if direction == "E":
            return tilt_block_east(block)
        if direction == "N":
            return rotate_ccw(tilt_block_east(rotate_cw(block)))
        if direction == "W":
            return repeat_func(rotate_ccw, 2, tilt_block_east(repeat_func(rotate_cw, 2, block)))
        if direction == "S":
            return rotate_cw(tilt_block_east(rotate_ccw(block)))

    def score_block(block):
        score = 0

        for i, row in enumerate(block):
            score += row.count("O")*(len(block) - i)
        
        return score

    return score_block(tilt(input, "N"))

print(f"Part 1 test output = {part1(test)} \n")

with open("day14\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")

def part2(input):

    input = input.strip().splitlines()

    def tilt_east(row):
        return "#".join(["".join(sorted(x)) for x in row.split("#")])

    def tilt_block_east(block):
        return [tilt_east(x) for x in block]

    def rotate_cw(block):
        return ["".join(x) for x in list(zip(*block[::-1]))]
    
    def rotate_ccw(block):
        return ["".join(x) for x in list(reversed(list(zip(*block[::]))))]
    
    def repeat_func(func, ntimes, x):
        for i in range(ntimes):
            x = func(x)

        return x
    
    def tilt(block, direction):
        if direction == "E":
            return tilt_block_east(block)
        if direction == "N":
            return rotate_ccw(tilt_block_east(rotate_cw(block)))
        if direction == "W":
            return repeat_func(rotate_ccw, 2, tilt_block_east(repeat_func(rotate_cw, 2, block)))
        if direction == "S":
            return rotate_cw(tilt_block_east(rotate_ccw(block)))

    def score_block(block):
        score = 0

        for i, row in enumerate(block):
            score += row.count("O")*(len(block) - i)
        
        return score
    
    def cycle(block):
        return tilt(tilt(tilt(tilt(block, "N"), "W"), "S"), "E")
    
    def get_cycle_metrics(block, N):
        x = block[:]
        seen_grids = ["".join(x)]

        for i in range(N):
            x = cycle(x)
            grid = "".join(x)

            if grid in seen_grids:
                steps_to_cycle = seen_grids.index(grid)
                cycle_length = i - steps_to_cycle + 1
                break
            else:
                seen_grids.append(grid)

        return steps_to_cycle + (N - steps_to_cycle) % cycle_length

    return score_block(repeat_func(cycle, get_cycle_metrics(input, 1_000_000_000), input))

print(f"Part 2 test output = {part2(test)} \n")

print(f"Part 2 output = {part2(input)} \n")