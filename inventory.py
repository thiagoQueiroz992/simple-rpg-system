from rich import inspect

class Inventory:
    slots = 10
    
    def __init__(self):
        self.__items = []


class Item:
    stack_max_items = 16

    def __init__(self, amount: int = 1):
        self.amount = amount
    
    def use(self, target):
        pass

class Apple(Item):
    def __init__(self, amount = 1):
        super().__init__(amount)
        self.health_restored = 10
    
    def use(self, target):
        super().use(target)

        def cure():
            target.set_health(target.get_health() + self.health_restored)
            if target.get_health() > 100:
                target.set_health(100)
        cure()
