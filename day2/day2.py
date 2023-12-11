test = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    # "Game 100: 9 green, 2 blue, 12 red; 2 blue, 14 red, 2 green; 14 red, 12 green"
    ]

def day2(input):

    score = 0

    for game in input:

        game_id = int("".join([letter for letter in game.split(":")[0] if letter.isdigit()]))
        
        draws = game.split(": ")[1].split("; ")

        good_game = True

        for draw in draws:
            
            color_data = {
                "red":0,
                "green":0,
                "blue":0
            }

            colors = list(color_data.keys())

            for entry in draw.split(", "):
                for color in colors:
                    if color in entry:
                        num = int("".join([letter for letter in entry if letter.isdigit()]))
                        color_data[color] += num

            if color_data["red"] <= 12:
                if color_data["green"] <= 13:
                    if color_data["blue"] <= 14:
                        if good_game and draw == draws[-1]: # sketchy af but gets the job done!
                            print(f"Game {game_id} is ok")
                            score += game_id
                    else:
                        good_game = False
                else:
                    good_game = False
            else:
                good_game = False

    return score

print(f"Test output = {day2(test)} \n")

with open("day2\input", "r") as input:
    print(f"Output = {day2(input)}")

