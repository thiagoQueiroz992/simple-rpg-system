from rich.panel import Panel
from rich.align import Align
from rich import print

class StartingMenu:
    game_panel = Panel(Align('Oneihl Kingdom Adventure', 'center'))

    def __init__(self):
        print(self.game_panel)