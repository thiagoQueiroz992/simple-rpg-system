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
        self.__current_fighting_enemy = None

    def move(self):
        time_to_find = randrange(3, 11)
        print(f'{self.name} is moving...')
        sleep(time_to_find)
        print(f'{self.name} has found an enemy')
        enemy_data = {'name': choice(('Zombie', 'Vampire', 'Skeleton', 'Witch', 'Undead Knight')), 'health': randrange(80, 201), 'attack': randrange(5, 21)}
        self.__current_fighting_enemy = Enemy(enemy_data['name'], enemy_data['health'], enemy_data['attack'])
        print(self.__current_fighting_enemy.__dict__)
        self.fight()
    
    def fight(self):
        while True:
            if self.get_health() > 0:
                self.attack(self.__current_fighting_enemy)
                print('Enemy:', self.__current_fighting_enemy.get_health())
            else:
                print('Played died')
                break

            if self.__current_fighting_enemy.get_health() > 0:
                self.__current_fighting_enemy.attack(self)
                print('Player:', self.get_health())
            else:
                print('Enemy died')
                break
        

class Enemy(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)