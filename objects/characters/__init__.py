class Character:
    def __init__(self, name: str, health: int, attack: int) -> None:
        self.name = name
        self.__health = health
        self.__attack = attack
    
    def get_health(self) -> int:
        return self.__health
    
    def set_health(self, value: int) -> None:
        if self.__health > 0:
            self.__health = value

class Player(Character):
    def __init__(self, name, health, attack):
        super().__init__(name = 'Player', health = 100, attack = 20)

class Enemy(Character):
    def __init__(self, name, health, attack):
        super().__init__(name = 'Zombie', health = 100, attack = 10)
