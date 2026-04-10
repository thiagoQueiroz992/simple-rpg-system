import inventory
from time import sleep
from random import randrange, random, choice
from options import Question, StatusDisplay, LootGenerator, LootDisplay
from loot_tables import looting
from rich import print
from rich import inspect
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
        print(death_message)


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
            item_management = Question('What will you do in inventory?', 'USE ITEM', 'LEAVE').show_question()
            if item_management == 0:
                self.__inventory.selection_mode(self)
                self.open_inventory()
                break
            else:
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
        print(target_enemy.__dict__)
        
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
        print(f'You are fighting against {target.name}!')
        fight_action = Question('What will you do?', 'ATTACK', 'DO NOTHING', 'FLEE')
        action_answer = 0
        while True:
            if self.get_health() > 0:
                action_answer = fight_action.show_question()
                system('cls')
                
                match action_answer:
                    case 0:
                        self.attack(target)
                        print(f'You attacked {target.name}!')
                    case 1:
                        print('You chose to do nothing.')
                    case 2:
                        print('You chose to flee the fight.')
                        self.idle()
                        break
            else:
                self.die('YOU DIED!')
                break
            
            if target.get_health() > 0:
                target.attack(self)
                print(f'\n\n{target.name} attacked you!\n\n')
            
            else:
                print(f'YOU DEFEATED {target.name.upper()}!')
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
        respawn()
        

class Enemy(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
    
    def get_loot(self, target_inventory):
        loot_generated = LootGenerator(looting['enemy']).generate_loot()
        display = LootDisplay(self, loot_generated)
        display.show_display()
        display.collect(target_inventory)
