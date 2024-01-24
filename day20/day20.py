import re
from collections import deque

test = """
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

test1 = """
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

def part1(input):
    matches = re.findall(r"(%|&|)(\w+) -> (.+)", input)
    config = {x[1]:x[2].split(", ") for x in matches}
    flip_flops = {x[1]:0 for x in matches if x[0] == "%"}
    conjunctions = {x[1]:0 for x in matches if x[0] == "&"}
    conjunctions = {x:{y:0 for y in config if x in config[y]} for x in conjunctions}
    high = low = 0
    for _ in range(1_000):
        low += 1
        init = [("broadcaster", d, 0) for d in config["broadcaster"]]
        queue = deque(init)
        while queue:
            orig, dest, signal = queue.popleft()
            # print(f"{orig} --{signal}--> {dest}", "\t\t\t", queue)
            if not signal:
                low += 1
            else:
                high += 1
            if dest in flip_flops and not signal:
                flip_flops[dest] = 1 - flip_flops[dest]
                new_signal = flip_flops[dest]
            elif dest in conjunctions:
                conjunctions[dest][orig] = signal
                if all(x == 1 for x in conjunctions[dest].values()):
                    new_signal = 0
                else:
                    new_signal = 1
            else:
                continue

            queue.extend([(dest, d, new_signal) for d in config[dest]])

    return high * low

print(f"Part 1 test output = {part1(test)} \n")

print(f"Part 1 test output = {part1(test1)} \n")

with open("day20\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")