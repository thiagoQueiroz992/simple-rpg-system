from time import sleep
from random import randrange, choice
from options import Question
from rich import print

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
    
    def attack(self, target) -> None:
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
            exit()
        
    def fight(self, target) -> None:
        print(f'You are fighting against {target.name}!')
        fight_action = Question('What will you do?', 'ATTACK', 'DO NOTHING', 'FLEE')
        action_answer = 0
        while True:
            if self.get_health() > 0:
                action_answer = fight_action.show_question()
                
                match action_answer:
                    case 0:
                        self.attack(target)
                        print(f'You attacked {target.name}!')
                    case 1:
                        print('You chose to do nothing.')
                    case 2:
                        print('You chose to flee the fight.')
                        break
        

class Enemy(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)