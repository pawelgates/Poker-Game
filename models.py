import random


class Player:
    """ Player class """

    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.table_chips = 0
        self.blinds = 0     # 0 = None, 1 = Small, 2 = Big

    def get_cards(self, cards):
        self.card_a = cards[0]
        self.card_b = cards[1]

    def show_cards(self):
        print(f"Player: {self.name}, Cards: {self.card_a[0]} {self.card_b[0]}")

    def player_cards(self):
        player_cards = [self.card_a, self.card_b]
        return player_cards

    def actions(self):
        def set_blinds(table):
            if self.blinds == 1:
                self.chips -= table.small_blinds
                self.table_chips += table.small_blinds
                return ("SMALL", table.small_blinds)
            elif self.blinds == 2:
                self.chips -= table.small_blinds*2
                self.table_chips += table.small_blinds*2
                return ("BIG", table.small_blinds*2)
            else:
                return ("NONE", 0)

        def check():
            return ("CHECK", 0)

        def fold():
            return ("FOLD", 0)

        def bet(ammount):
            self.chips -= ammount
            self.table_chips += ammount
            return ("BET", ammount)

        def call(bet):
            call = bet - self.table_chips
            self.chips -= call
            self.table_chips += call
            return("CALL", call)

        def all_in():
            all_in = self.chips
            self.chips = 0
            self.table_chips += all_in
            return("ALL IN", all_in)


class Dealer:
    """ Dealer class """

    def __init__(self, name):
        self.name = name
        self.hands = 0

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

    def count_hands(self):
        self.hands += 1


class Table:
    """ Playing table class """

    def __init__(self):
        self.flop = None
        self.turn = None
        self.river = None
        self.chips = None
        self.small_blinds = 0

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

    def blinds_span(self, list_of_players):
        last = list_of_players.pop()
        list_of_players.insert(0, last)
        for player in list_of_players:
            player.blinds = 0
        list_of_players[0].blinds = 1
        list_of_players[1].blinds = 2
