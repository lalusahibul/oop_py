from player import Player
from monster import Monster
player1 = Player('Umar')
player2 = Player('Ferry')
monster = Monster('Sopian')
player1.attack(monster,damage=100)
player2.attack(monster,damage=100)
player1.show_info()
player2.show_info()
monster.show_info()