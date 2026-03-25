class Character:
    def __init__(self, name: str, health: int, attack: int) -> None:
        self.name = name
        self.__health = health
        self.__attack = attack

class Player(Character):
    def __init__(self, name, health, attack):
        super().__init__(name = 'Player', health = 100, attack = 20)

