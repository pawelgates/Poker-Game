
from hand import hand_check


def cards_deck():
    deck = {
        "2 clubs": 2,
        "2 diamonds": 2,
        "2 hearts": 2,
        "2 spades": 2,
        "3 clubs": 3,
        "3 diamonds": 3,
        "3 hearts": 3,
        "3 spades": 3,
        "4 clubs": 4,
        "4 diamonds": 4,
        "4 hearts": 4,
        "4 spades": 4,
        "5 clubs": 5,
        "5 diamonds": 5,
        "5 hearts": 5,
        "5 spades": 5,
        "6 clubs": 6,
        "6 diamonds": 6,
        "6 hearts": 6,
        "6 spades": 6,
        "7 clubs": 7,
        "7 diamonds": 7,
        "7 hearts": 7,
        "7 spades": 7,
        "8 clubs": 8,
        "8 diamonds": 8,
        "8 hearts": 8,
        "8 spades": 8,
        "9 clubs": 9,
        "9 diamonds": 9,
        "9 hearts": 9,
        "9 spades": 9,
        "10 clubs": 10,
        "10 diamonds": 10,
        "10 hearts": 10,
        "10 spades": 10,
        "J clubs": 11,
        "J diamonds": 11,
        "J hearts": 11,
        "J spades": 11,
        "Q clubs": 12,
        "Q diamonds": 12,
        "Q hearts": 12,
        "Q spades": 12,
        "K clubs": 13,
        "K diamonds": 13,
        "K hearts": 13,
        "K spades": 13,
        "A clubs": 14,
        "A diamonds": 14,
        "A hearts": 14,
        "A spades": 14
    }
    return deck


def hands():
    hands = {
        "Royal flush": 10,
        "Straight flush": 9,
        "Four of a kind": 8,
        "Full house": 7,
        "Flush": 6,
        "Straight": 5,
        "Three of a kind": 4,
        "Two pair": 3,
        "Pair": 2,
        "High card": 1
    }
    return hands
