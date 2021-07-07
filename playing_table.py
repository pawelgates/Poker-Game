from models import Player, Dealer, Table
from cards import cards_deck
from hand import cards_combination, hand_check


player1 = Player("Pavel", 2000)
player2 = Player("Moshe", 2000)

players = [player1, player2]
dealer = Dealer("John")
table = Table()

dealer.new_deck(cards_deck())

for player in players:
    dealer.give_player(player)

player1.show_cards()
player2.show_cards()

# FLOP
table.flop = dealer.flop_cards()
print(type(table.flop[0]))
table.display_cards()

# TURN
table.turn = dealer.turn_card()
table.display_cards()

# RIVER
table.river = dealer.river_card()
table.display_cards()

# WINNER

hand_check(cards_combination(player2, table))
