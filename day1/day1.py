def part1(inputs):
    x = 0

    for input in inputs:
        # input = re.sub(pattern, lambda x: num_dict[x.group()], input)
        # print(input)
        numbers = [i for i in list(input) if i.isnumeric()]
        x += int(numbers[0]+numbers[-1])

    return x

inputs1 = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]

f = open("input", "r")
print(part1(f))

def part2(inputs):
