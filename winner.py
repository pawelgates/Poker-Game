from models import Player, Dealer, Table


def cards_combination(player, table):
    combination = player.player_cards() + table.table_cards()
    return combination
