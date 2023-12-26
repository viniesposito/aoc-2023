from collections import Counter
from functools import cmp_to_key

test = """
32T3K 765
T55J5 684
KK677 28
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

    def get_hand_type(hand):

        card_count_list = list(Counter(hand).values())

        if 5 in card_count_list:
            hand_type = 6
        elif 4 in card_count_list:
            hand_type = 5
        elif 3 in card_count_list and 2 in card_count_list:
            hand_type = 4
        elif 3 in card_count_list:
            hand_type = 3
        elif card_count_list.count(2) == 2:
            hand_type = 2
        elif 2 in card_count_list:
            hand_type = 1
        else:
            hand_type = 0

        return hand_type

    def compare_hands(hand1, hand2):
        type1 = get_hand_type(hand1[0])
        type2 = get_hand_type(hand2[0])

        if type1 > type2:
            return 1
        if type1 < type2:
            return -1
        else:
            for i in range(5):
                if hand1[0][i] != hand2[0][i]:
                    if card_map[hand1[0][i]] > card_map[hand2[0][i]]:
                        return 1
                    else:
                        return -1

    input = sorted(input, key=cmp_to_key(compare_hands))
    
    score = 0

    for i, hand in enumerate(input):
        bid = int(hand[1])
        score += (i+1) * bid

    return score

print(f"Part 1 test output = {part1(test)} \n")

with open("day7\input", "r") as input:
    input = "".join([val for val in input])

print(f"Part 1 output = {part1(input)} \n")