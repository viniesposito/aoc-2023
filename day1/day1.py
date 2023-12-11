import regex as re

def part1(inputs):
    x = 0

    for input in inputs:
        numbers = [i for i in list(input) if i.isnumeric()]
        x += int(numbers[0]+numbers[-1])

    return x

inputs1 = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]
print(f"Part 1 test output = {part1(inputs1)}")

with open("day1\input", "r") as calibration_values:
    print(f"Part 1 output = {part1(calibration_values)}")

def part2(inputs):
    
    num_dict = {
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9",
    }

    pattern = r"(" + "|".join(num_dict.keys()) + r"|\d)"

    x = 0

    for input in inputs:
        
        numbers = re.findall(pattern, input, overlapped=True)
        numbers = [num_dict.get(val) if val in num_dict.keys() else val for val in numbers]
        
        x += int(numbers[0]+numbers[-1])

    return x

inputs2 = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]
print(f"Part 2 test output = {part2(inputs2)}")

with open("day1\input", "r") as calibration_values:
    print(f"Part 2 output = {part2(calibration_values)}")