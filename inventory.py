from rich import inspect

class Inventory:
    slots = 10
    stack_max_items = 16
    
    def __init__(self):
        self.__items = []
    
    def add_item(self, item):
        for a in range(item.get_amount(), 0, -1):
            for i, s in enumerate(self.__items):
                if isinstance(item, type(s['item'])) and s['amount'] < self.stack_max_items:
                    self.__items[i]['amount'] += 1
                    break
                else:
                    continue
            else:
                if len(self.__items) < self.slots:
                    self.__items.append({'item': item, 'amount': item.get_amount()})
                    break
                else:
                    print('Inventory is full.')
                    break



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


class Wood(Item):
    def __init__(self, amount = 1):
        super().__init__(amount)
        self.name = 'Wood'
