import characters
from rich import inspect, print
from rich.panel import Panel
from rich.align import Align
from os import system
from time import sleep
from options import Question

system('cls')

print(Panel(Align('ONEIHL\'S RPG GAME', align='center', vertical='middle'), subtitle='A RPG style game made for studying purpose', style='bold green', height=5))
sleep(2)
print()

player = characters.Player(Question('Enter your name:', '-', question_type='text').show_question(), 100, 20)
print(Panel(Align(f'Welcome [cyan]{player.name}[/cyan]! You are going to start your new adventure!', align='center'), style='green bold'))
sleep(3.5)
player.idle()