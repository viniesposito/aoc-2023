from itertools import chain, combinations
import re

test = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

def part1(input):

    input = [x.split(" ") for x in input.splitlines() if x != ""]
    
    def generate_all_combos(s):
        unknown_idxs = [i for i, x in enumerate(s) if x == "?"]

        all_unknown_combinations = chain.from_iterable(combinations(unknown_idxs, l) for l in range(len(unknown_idxs)+1))

        out = []

        for idxs in all_unknown_combinations:
            chars = list(s)

            for i in idxs:
                chars[i] = "#"

            chars = "".join(chars)

            chars = chars.replace("?", ".")

            out.append(chars)

        return out
    
    def verify_validity(s, arrangement):
        sections = [len(x) for x in re.findall(r"\#+", s)]
        
        return sections == arrangement

    score = 0

    for entry, arr in input:
        arr = [int(n) for n in re.findall(r"\d+", arr)]

        score += len([x for x in generate_all_combos(entry) if verify_validity(x, arr)])

    return score


print(f"Part 1 test output = {part1(test)} \n")

with open("day12\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")