from time import sleep
from random import randrange, choice

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
    
    def attack(self, target):
        target.set_health(target.get_health() - self.__attack)


class Player(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def move(self) -> None:
        time_to_find = randrange(3, 11)
        print(f'{self.name} is moving...')
        sleep(time_to_find)
        print(f'{self.name} has found an enemy')
        self.find_enemy()

    def find_enemy(self) -> None:
        enemy_data = {'name': choice(('Zombie', 'Vampire', 'Skeleton', 'Witch', 'Undead Knight')), 'health': randrange(80, 201), 'attack': randrange(5, 21)}
        target_enemy = Enemy(enemy_data['name'], enemy_data['health'], enemy_data['attack'])
        print(target_enemy.__dict__)
        self.fight(target_enemy)    
        
    def fight(self, target) -> None:
        while True:
            if self.get_health() > 0:
                self.attack(target)
                print('Enemy:', target.get_health())
            else:
                print('Played died')
                break
            if target.get_health() > 0:
                target.attack(self)
                print('Player:', self.get_health())
            else:
                print('Enemy died')
                break
        

class Enemy(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)