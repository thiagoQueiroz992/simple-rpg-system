from rich import inspect

class Inventory:
    slots = 10
    stack_max_items = 16
    
    def __init__(self):
        self.__items = []
    
    def add_item(self, item):
        if len(self.__items) <= self.slots:
            for a in range(item.get_amount(), 0, -1):
                if not self.__items:
                    self.__items.append(item)
                    break
                else:
                    for s in self.__items:
                        if isinstance(item, type(s)) and s.get_amount() < self.stack_max_items:
                            s.set_amount(s.get_amount() + 1)
                        else:
                            if len(self.__items) < 10:
                                self.__items.append(item)
                                break
                            else:
                                break
        else:
            print('Inventory is full')



class Item:
    def __init__(self, amount: int = 1):
        self.name = 'item'
        self.__amount = amount
    
    def use(self, target):
        self.__amount -= 1

    def get_amount(self) -> int:
        return self.__amount
    
    def set_amount(self, amount: int = 1):
        self.__amount += amount

class Apple(Item):
    def __init__(self, amount = 1):
        super().__init__(amount)
        self.name = 'Apple'
        self.__health_restored = 10
    
    def use(self, target):
        super().use(target)

        def cure():
            target.set_health(target.get_health() + self.__health_restored)
            if target.get_health() > 100:
                target.set_health(100)
        cure()
