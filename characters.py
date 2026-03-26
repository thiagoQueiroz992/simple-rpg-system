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
    
    def attack(self, target):
        target.set_health(target.get_health() - self.__attack)


class Player(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)


class Enemy(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)