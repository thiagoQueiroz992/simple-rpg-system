import inventory
from time import sleep
from random import randrange, random, choice
from options import Question, StatusDisplay, LootGenerator, LootDisplay
from loot_tables import looting
from rich import print
from rich import inspect
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from os import system

class Character:
    def __init__(self, name: str, health: int, attack: int):
        self.name = name
        self.__health = health
        self.__attack = attack
    
    def get_health(self) -> int:
        return self.__health
    
    def set_health(self, value: int) -> None:
        if value > 0:
            self.__health = value
        else:
            self.__health = 0
    
    def get_attack(self) -> int:
        return self.__attack
    
    def set_attack(self, value: int):
        if value > 0:
            self.__attack = value
        else:
            self.__attack = 0
    
    def attack(self, target) -> None:
        target.set_health(target.get_health() - self.__attack)
    
    def die(self, death_message: str) -> None:
        system('cls')
        print(Panel(Align(death_message, align='center', vertical='middle'), style='red bold', height=5))


class Player(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.default_max_health = 100
        self.equipped_weapon = None
        self.__inventory = inventory.Inventory()

    def idle(self) -> None:
        system('cls')
        action = Question('What do you want to do now?', 'WALK', 'OPEN INVENTORY', 'VIEW YOUR STATUS', 'EXIT GAME').show_question()
        
        match action:
            case 0:
                print('You are going to walk around.')
                self.move()
            case 1:
                self.open_inventory()
            case 2:
                self.open_status()
            case 3:
                exit()
    
    def move(self) -> None:
        system('cls')
        time_to_find = randrange(3, 11)
        print(f'{self.name} is moving...')
        sleep(time_to_find)

        roll = random()
        if roll * 100 <= 80:
            print(f'{self.name} has found an enemy')
            self.find_enemy()
        else:
            self.find_chest()
    
    def open_inventory(self) -> None:
        self.__inventory.display_inventory(self)
        while True:
            item_management = Question('What will you do in inventory?', 'USE ITEM', 'DESTROY ITEM', 'LEAVE').show_question()
            
            match item_management:
                case 0:
                    self.__inventory.selection_mode(self)
                    self.open_inventory()
                    break
                case 1:
                    self.__inventory.selection_mode(self, 'destroy')
                    self.open_inventory()
                    break
                case 2:
                    self.idle()
                    break
    
    def open_status(self) -> None:
        StatusDisplay(self).show_display()

        close = Question('Close status?', 'CLOSE').show_question()
        if close == 0:
            self.idle()

    def find_enemy(self) -> None:
        enemy_data = {
            'name':choice(('Zombie', 'Vampire', 'Skeleton', 'Witch','Undead Knight')),
            'health': randrange(80, 201),
            'attack': randrange(5, 21)
            }
        
        target_enemy = Enemy(enemy_data['name'], enemy_data['health'], enemy_data['attack'])
        enemy_display = Table('TYPE', 'VALUE', title=target_enemy.name, expand=True, show_header=False, style='bold yellow', title_style='bold yellow')
        enemy_display.add_row('Name', Align(target_enemy.name, align='center'), style='bold green')
        enemy_display.add_row('Health', Align(str(target_enemy.get_health()) + ' HP', align='center'), style='bold green')
        enemy_display.add_row('Attack', Align(str(target_enemy.get_attack()), align='center'), style='bold green')
        
        print(enemy_display)
        
        fight_against_enemy = Question(f'Do you want to fight against [cyan bold]{target_enemy.name}[/cyan bold]?', 'FIGHT', 'FLEE').show_question()

        if fight_against_enemy == 0:
            self.fight(target_enemy)
        else:
            self.idle()
    
    def find_chest(self) -> None:
        print('You found a chest!')

        open_chest = Question('Do you want to open the chest?', 'YES', 'IGNORE CHEST').show_question()

        if open_chest == 0:
            loot_generated = LootGenerator(looting['chest']).generate_loot()
            display = LootDisplay(self, loot_generated)
            display.show_display()
            display.collect(self.__inventory)
        
        self.idle()
        
    def fight(self, target) -> None:
        system('cls')
        print(Panel(Align(f'You are fighting against [cyan]{target.name}[/cyan]!', align='center', vertical='middle'), style='yellow bold', height=5))
        sleep(1)
        fight_action = Question('What will you do?', 'ATTACK', 'DO NOTHING', 'FLEE')
        action_answer = 0
        while True:
            fight_table = Table(expand=True, style='bold blue', show_header=False)
            fight_table.add_column('FIGHTER')
            fight_table.add_column('HEALTH')

            fight_table.add_row(self.name, Align(str(self.get_health()) + ' HP', align='center'))
            fight_table.add_row(target.name, Align(str(target.get_health()) + ' HP', align='center'))
            
            if self.get_health() > 0:
                print(fight_table)
                action_answer = fight_action.show_question()
                system('cls')
                
                match action_answer:
                    case 0:
                        self.attack(target)
                        print(Panel(Align(f'You attacked [cyan]{target.name}[/cyan]!', align='center'), style='yellow bold'))
                        sleep(1)
                    case 1:
                        print(Panel(Align(f'You chose to do nothing.', align='center'), style='purple bold'))
                        sleep(1)
                    case 2:
                        print(Panel(Align(f'You chose to flee the fight.', align='center'), style='blue bold'))
                        sleep(1.5)
                        self.idle()
                        break
            else:
                self.die('YOU DIED!')
                break
            
            if target.get_health() > 0:
                target.attack(self)
                print('\n')
                print(Panel(Align(f'[cyan]{target.name}[/cyan] attacked you!', align='center'), style='red bold'))
                sleep(2)
                system('cls')
            
            else:
                print(Panel(Align(f'YOU DEFEATED [cyan]{target.name.upper()}[/cyan]!', align='center'), style='green bold'))
                sleep(2)
                target.get_loot(self.__inventory)
                self.idle()
                break
    
    def die(self, death_message) -> None:
        super().die(death_message)

        def respawn(respawning_time: int = 5) -> None:
            respawn_question = Question('Respawn?', 'YES', 'QUIT GAME').show_question()
            
            match respawn_question:
                case 0:
                    print('Respawning in:', end=' ')
                    sleep(1)
                    for t in range(respawning_time, 0, -1):
                        print(t, end='...')
                        sleep(1)
                    print()
                    self.set_health(100)
                    self.idle()
                case 1:
                    exit()
        sleep(3)
        respawn()
    
    def get_inventory(self) -> inventory.Inventory:
        return self.__inventory
        

class Enemy(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
    
    def get_loot(self, target_inventory):
        loot_generated = LootGenerator(looting['enemy']).generate_loot()
        display = LootDisplay(self, loot_generated)
        display.show_display()
        display.collect(target_inventory)
