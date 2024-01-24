import re
from math import prod

test = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

def part1(input):
    
    def parse_input(input):
        input = input.strip().splitlines()
        workflows, ratings = input[:input.index("")], input[input.index("") + 1:]
        return workflows, ratings
    
    def parse_workflows(workflows):
        d = {}
        for wf in workflows:
            wf_name, rules = re.findall(r"(\w+){(.+)}", wf)[0]
            rules = [r.split(":") if ":" in r else r for r in rules.split(",")]
            d[wf_name] = rules
        return d

    workflows, ratings = parse_input(input)
    workflows = parse_workflows(workflows)
    
    score = 0
    for rating in ratings:
        x, m, a, s = [int(num) for num in re.findall(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", rating)[0]]
        wf = "in"
        step = "Z"
        while True:
            if wf == "A":
                score += (x+m+a+s)
                break
            elif wf == "R":
                break
            
            for step in workflows[wf]:
                if isinstance(step, list): 
                    if eval(step[0]):
                        wf = step[1]
                        break
                    else:
                        continue
                else:
                    wf = step
        
    return score

print(f"Part 1 test output = {part1(test)} \n")

with open("day19\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")

def part2(input):
    
    def parse_input(input):
        input = input.strip().splitlines()
        workflows, ratings = input[:input.index("")], input[input.index("") + 1:]
        return workflows, ratings
    
    def parse_workflows(workflows):
        d = {}
        for wf in workflows:
            rules_list = []
            wf_name, rules = re.findall(r"(\w+){(.+)}", wf)[0]
            for char, operator, num, dest in re.findall(r"(\w+)(<|>)(\d+):(\w+)", rules):
                rules_list.append((char, operator, int(num), dest))
            d[wf_name] = rules_list + [rules.split(",")[-1]]  
        return d

    workflows, _ = parse_input(input)
    workflows = parse_workflows(workflows)
    
    queue = [("in", (1, 4_000), (1, 4_000), (1, 4_000), (1, 4_000))]
    score = 0

    while queue:
        wf_name, *xmas_ranges = queue.pop()
        if wf_name == "A":
            score += prod(1 + x[1] - x[0] for x in xmas_ranges)
            continue

        elif wf_name == "R":
            continue

        for char, operator, num, dest in workflows[wf_name][:-1]:
            inf, sup = xmas_ranges["xmas".index(char)]
            if (num > sup and operator == "<") or (num < inf and operator == ">"):
                break
            if (num >= sup and operator == ">") or (num <= inf and operator == "<"):
                continue
            if operator == ">":
                passes = (num + 1, sup)
                fails = (inf, num)
            else:
                fails = (num, sup)
                passes = (inf, num - 1)
            xmas_ranges["xmas".index(char)] = fails
            new_xmas_ranges = xmas_ranges[:]
            new_xmas_ranges["xmas".index(char)] = passes
            queue.append((dest, *new_xmas_ranges))
        
        else:
            queue.append((workflows[wf_name][-1], *xmas_ranges))

    return score
    
print(f"Part 2 test output = {part2(test)} \n")

print(f"Part 2 output = {part2(input)} \n")