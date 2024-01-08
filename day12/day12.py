from itertools import chain, combinations
import re
from functools import cache

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

def part2(input):

    input = [x.split(" ") for x in input.splitlines() if x != ""]

    @cache
    def calc_num_of_valid_solutions(s, groups):
        
        # was stuck for a long time, only unblocked after seeing this guy's great walkthrough of his solution on Reddit
        # https://advent-of-code.xavd.id/writeups/2023/day/12/

        if not s:
            return len(groups) == 0

        if not groups:
            return "#" not in s

        char = s[0]
        rest = s[1:]

        if char == ".":
            return calc_num_of_valid_solutions(rest, groups)

        if char == "#":

            current_group = groups[0]

            if len(s) >= current_group and all(c != "." for c in s[:current_group]) and (len(s) == current_group or s[current_group] != "#"):
                return calc_num_of_valid_solutions(s[(1+current_group):], groups[1:])
            else:
                return 0

        if char == "?":
            return calc_num_of_valid_solutions("#" + rest, groups) + calc_num_of_valid_solutions("." + rest, groups)

    score = 0

    for entry, arr in input:

        expansion_factor = 5

        entry = "?".join(expansion_factor*[entry])

        arr = expansion_factor * tuple([int(n) for n in re.findall(r"\d+", arr)])
        
        score += calc_num_of_valid_solutions(entry, arr)

    return score

print(f"Part 2 test output = {part2(test)} \n")

print(f"Part 2 output = {part2(input)} \n")