test = """
32T3K 765
T55J5 684
KK677 28
KKK67 98
KTJJT 220
QQQJA 483
"""

def part1(input):

    card_map = {
        "A" : 14,
        "K" : 13,
        "Q" : 12,
        "J" : 11,
        "T" : 10,
        "9" : 9,
        "8" : 8,
        "7" : 7,
        "6" : 6,
        "5" : 5,
        "4" : 4,
        "3" : 3,
        "2" : 2,
        "1" : 1
    }

    input = [x.split(" ") for x in input.splitlines() if x != ""]

    n_hands = len(input)

    score_list = []
    hand_pts_list = []

    for hand_list in input:
        hand = hand_list[0]

        card_count_list = []

        for item in card_map.keys():
            card_count = hand.count(item)

            if card_count > 0:
                card_count_list.append(card_count)

        if 5 in card_count_list:
            score = 6
        elif 4 in card_count_list:
            score = 5
        elif 3 in card_count_list and 2 in card_count_list:
            score = 4
        elif 3 in card_count_list:
            score = 3
        elif card_count_list.count(2) == 2:
            score = 2
        elif 2 in card_count_list:
            score = 1
        else:
            score = 0

        score_list.append(score)
        hand_pts_list.append([card_map[card] for card in hand])

    score_list = [1+sorted(score_list).index(x) for x in score_list]
    input = [input[i]+[score_list[i]] for i in range(n_hands)]
    input = [input[i]+[hand_pts_list[i]] for i in range(n_hands)]
    # each entry in input = [hand string, bid string, score int, hand pts list of int]
    sorted_input = [x for _, x in sorted(zip(score_list, input))]
    print(sorted(score_list))
    for i in range(1, n_hands):
        print(f"Looking at hand {i} vs {i-1}: {sorted_input[i][0]} vs {sorted_input[i-1][0]}")
        score = sorted_input[i][2]
        score_prev = sorted_input[i-1][2]
        if score == score_prev:
            print(f"Tie found! Two cards with score = {score}")
            for j in range(5):
                if sorted_input[i][3][j] > sorted_input[i-1][3][j]:
                    sorted_input[i][2] += 1
                    print(f"Hand {i} won! Its score was bumped to {sorted_input[i][2]}\n")
                    break
                elif sorted_input[i][3][j] < sorted_input[i-1][3][j]:
                    sorted_input[i-1][2] += 1
                    print(f"Hand {i-1} won! Its score was bumped to {sorted_input[i-1][2]}\n")
                    break
            print(i)        
            if sorted_input[(i+1):]:
                print("fuck",i)
                print([sorted_input[k][2] for k in range(i+1,n_hands)])
                # sorted_input[(i+1):] = [val[2]+1 for val in sorted_input[(i+1):]]
                

    print(sorted_input)



part1(test)