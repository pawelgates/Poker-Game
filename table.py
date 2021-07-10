from models import Player, Dealer, Table
from cards import cards_deck
from hand import cards_combination, hand_check


player1 = Player("Pavel", 2000)
player2 = Player("Moshe", 2000)
player3 = Player("Sasha", 2000)

players = [player1, player2, player3]
dealer = Dealer("John")
table = Table()

table.blinds_span(players)
table.blinds_span(players)
table.blinds_span(players)

dealer.new_deck(cards_deck())

for player in players:
    dealer.give_player(player)
    player.show_cards()


# FLOP
table.flop = dealer.flop_cards()
table.display_cards()

# TURN
table.turn = dealer.turn_card()
table.display_cards()

# RIVER
table.river = dealer.river_card()
table.display_cards()

# WINNER
# TEST
test_fullhouse = [("10 clubs", 10), ("K diamonds", 13), ("Q clubs", 12),
                  ("K clubs", 13), ("A diamonds", 14), ("A hearts", 14), ("A clubs", 14)]
test_flush = [("10 clubs", 10), ("K diamonds", 13),
              ("Q clubs", 12), ("K clubs", 13), ("A clubs", 14), ("6 clubs", 6), ("8 clubs", 8)]
test_straight = [("10 diamonds", 10), ("K diamonds", 13),
                 ("Q clubs", 12), ("K clubs", 13), ("A diamonds", 14), ("6 clubs", 6), ("J clubs", 11)]
test_straight_flush = [("8 diamonds", 8), ("K hearts", 13), ("Q diamonds", 12),
                       ("K clubs", 13), ("10 diamonds", 10), ("9 diamonds", 9), ("J diamonds", 11)]

for player in players:
    print(hand_check(cards_combination(player, table)))
# print(hand_check(test_straight_flush))
