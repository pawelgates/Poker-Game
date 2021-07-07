from models import Player, Dealer, Table


def cards_combination(player, table):
    combination = player.player_cards() + table.table_cards()
    return combination


def hand_check(combination):
    cards = dict(combination)

    # ROYAL FLUSH
    tmp = cards
    royal1 = {"10 clubs": 10, "J clubs": 11,
              "Q clubs": 12, "K clubs": 13, "A clubs": 14}
    royal2 = {"10 diamonds": 10, "J diamonds": 11,
              "Q diamonds": 12, "K diamonds": 13, "A diamonds": 14}
    royal3 = {"10 hearts": 10, "J hearts": 11,
              "Q hearts": 12, "K hearts": 13, "A hearts": 14}
    royal4 = {"10 spades": 10, "J spades": 11,
              "Q spades": 12, "K spades": 13, "A spades": 14}
    if royal1.items() <= tmp.items():
        return "Royal flush"
    if royal2.items() <= tmp.items():
        return "Royal flush"
    if royal3.items() <= tmp.items():
        return "Royal flush"
    if royal4.items() <= tmp.items():
        return "Royal flush"

    # STRAIGHT FLUSH
    tmp = cards

    # FOUR OF A KIND
    tmp = cards
    values = list(tmp.values())
    for num in values:
        if values.count(num) == 4:
            return "Four of a kind"

    # FULL HOUSE
    tmp = cards
    values = list(tmp.values())
    nums = []
    for num in values:
        if values.count(num) == 3:
            nums.append(num)
            break
    if len(nums) != 0:
        for num in values:
            if values.count(num) >= 2 and num != nums[0]:
                return "Full house"

    # FLUSH
    tmp = cards
    dirty_keys = list(tmp.keys())
    clear_keys = []
    for key in dirty_keys:
        key = key.split()
        new_key = key[1]
        clear_keys.append(new_key)
    for shape in clear_keys:
        if clear_keys.count(shape) >= 5:
            return "Flush"

    # STRAIGHT

    # THREE OF A KIND
    tmp = cards
    values = list(tmp.values())
    for num in values:
        if values.count(num) == 3:
            return "Three of a kind"

    # TWO PAIR

    # PAIR

    # HIGH CARD
