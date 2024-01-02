import re

test = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

def part1(input):

    input = input.splitlines()
    seeds = [x for x in input if "seeds" in x][0]
    seeds = [int(x) for x in re.findall(r"\d+",seeds)]
    input = input[2:]
    
    maps = [x for x in input if any(char.isdigit() for char in x) == False and x != ""]
    
    map_dict_raw = {}

    for val in input:

        if val in maps:
            map = val
            map_dict_raw[map] = []
        else:
            if val != "":
                val_int = [int(x) for x in re.findall(r"\d+",val)]
                map_dict_raw[map].append(val_int)

    locations = []
    
    for seed in seeds:
        for map_name in maps:
            for line in map_dict_raw[map_name]:
                
                if line[1] <= seed < line[1] + line[2]:
                    seed +=  line[0] - line[1]
                    break

            if map_name == maps[-1]:
                locations.append(seed)

    return min(locations)

print(f"Part 1 test output = {part1(test)} \n")

with open("day5\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")

def part2(input):

    input = input.splitlines()
    seeds = [x for x in input if "seeds" in x][0]
    seeds = [int(x) for x in re.findall(r"\d+",seeds)]
    
    seed_list = []

    for i in range(0,len(seeds),2):
        seed_list.append(range(seeds[i],seeds[i]+seeds[i+1]))

    input = input[2:]
    
    maps = [x for x in input if any(char.isdigit() for char in x) == False and x != ""]
    
    map_dict_raw = {}

    for val in input:

        if val in maps:
            map = val
            map_dict_raw[map] = []
        else:
            if val != "":
                val_int = [int(x) for x in re.findall(r"\d+",val)]
                map_dict_raw[map].append(val_int)

    locations = []
    
    for seed_range in seed_list:
        for seed in seed_range:
            for map_name in maps:
                for line in map_dict_raw[map_name]:
                    
                    if line[1] <= seed < line[1] + line[2]:
                        seed +=  line[0] - line[1]
                        break
                    
                if map_name == maps[-1]:
                    locations.append(seed)

    return min(locations)

print(f"Part 2 test output = {part2(test)} \n")

print(f"Part 2 output = {part2(input)} \n")
