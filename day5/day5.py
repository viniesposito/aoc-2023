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

    # input = [x for x in input.splitlines() if x != ""]
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

    lookup_dict = {}

    for map_name in maps:
        # print(map_name)
        map_raw = map_dict_raw[map_name]
        
        map_dict = {x:x for x in range(100)}
        
        for range_list in map_raw:
            # print(range_list)
            source_range = range(range_list[1],range_list[1]+range_list[2])
            dest_range = range(range_list[0],range_list[0]+range_list[2])
        
            for i in range(len(source_range)):
                # print(i)
                map_dict[source_range[i]] = dest_range[i]

        lookup_dict[map_name] = map_dict

    
    locations = []
    
    for seed in seeds:
        for map_name in maps:
            seed = lookup_dict[map_name][seed]
            
            if map_name == maps[-1]:
                locations.append(seed)

    return min(locations)

print(f"Part 1 test output = {part1(test)} \n")

# with open("day5\input", "r") as input:
#     input = "".join([val for val in input])

# print(f"Part 1 output = {part1(input)} \n")