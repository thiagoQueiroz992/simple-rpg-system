from rich.panel import Panel
from rich.align import Align
from rich import print

class StartingMenu:
    game_panel = Panel(Align('Oneihl Kingdom Adventure', 'center'))
    new_game_button = Panel(Align('Press Enter to start a new game', 'center'), width=40)

    def __init__(self):
        print(self.game_panel)
        print(self.new_game_button)