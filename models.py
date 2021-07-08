import random


class Player:
    """ Player class """

    def __init__(self, name, chips):
        self.name = name
        self.chips = chips

    def get_cards(self, cards):
        self.card_a = cards[0]
        self.card_b = cards[1]

    def show_cards(self):
        print(f"Player: {self.name}, Cards: {self.card_a[0]} {self.card_b[0]}")

    def blinds_status(self, status):
        self.blinds = status

    def player_cards(self):
        player_cards = [self.card_a, self.card_b]
        return player_cards


class Dealer:
    """ Dealer class """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(
            f"Hello! My name is {self.name} and I'm your dealer! Let's play some Poker!")

    def new_deck(self, new_deck):
        self.deck = new_deck

    def give_player(self, player):
        card1 = random.choice(list(self.deck.items()))
        self.deck.pop(card1[0])
        card2 = random.choice(list(self.deck.items()))
        self.deck.pop(card2[0])
        cards = [card1, card2]
        player.get_cards(cards)

    def flop_cards(self):
        burn_card = random.choice(list(self.deck.items()))
        self.deck.pop(burn_card[0])
        flop1 = random.choice(list(self.deck.items()))
        self.deck.pop(flop1[0])
        flop2 = random.choice(list(self.deck.items()))
        self.deck.pop(flop2[0])
        flop3 = random.choice(list(self.deck.items()))
        self.deck.pop(flop3[0])
        return [flop1, flop2, flop3]

    def turn_card(self):
        burn_card = random.choice(list(self.deck.items()))
        self.deck.pop(burn_card[0])
        turn_card = random.choice(list(self.deck.items()))
        self.deck.pop(turn_card[0])
        return turn_card

    def river_card(self):
        burn_card = random.choice(list(self.deck.items()))
        self.deck.pop(burn_card[0])
        river_card = random.choice(list(self.deck.items()))
        self.deck.pop(river_card[0])
        return river_card


class Table:
    """ Playing table class """

    def __init__(self):
        self.flop = None
        self.turn = None
        self.river = None

    def display_cards(self):
        cards = ""
        if self.flop is not None:
            cards += f"{self.flop[0][0]}  {self.flop[1][0]}  {self.flop[2][0]}  "
        if self.turn is not None:
            cards += f"{self.turn[0]}  "
        if self.river is not None:
            cards += f"{self.river[0]}"
        return print(cards)

    def table_cards(self):
        table_cards = []
        table_cards.append(self.flop[0])
        table_cards.append(self.flop[1])
        table_cards.append(self.flop[2])
        table_cards.append(self.turn)
        table_cards.append(self.river)

        return table_cards
