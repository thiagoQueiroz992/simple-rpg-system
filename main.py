from objects.characters import Player, Enemy
#from objects.inventory import Inventory
from objects.starting_menu import StartingMenu

player = Player('Player', 100, 20)
player.set_health(120)
print(player.get_health())