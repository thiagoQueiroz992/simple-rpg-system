from rich import inspect
from options import InventoryDisplay

class Inventory:
    slots = 10
    stack_max_items = 16
    
    def __init__(self):
        self.__items = []
    
    def add_item(self, item, amount: int = 1) -> None:
        for a in range(amount, 0, -1):
            for i, s in enumerate(self.__items):
                if isinstance(item, type(s['item'])) and s['amount'] < self.stack_max_items:
                    self.__items[i]['amount'] += 1
                    break
                else:
                    continue
            else:
                if len(self.__items) < self.slots:
                    self.__items.append({'item': item, 'amount': amount})
                    break
                else:
                    print('Inventory is full.')
                    break
    
    def use_item(self, slot: int, target) -> None:
        self.__items[slot]['amount'] -= 1
        self.__items[slot]['item'].using_effects(target)
        if self.__items[slot]['amount'] == 0:
            self.__items.pop(slot)
    
    def display_inventory(self, target):
        InventoryDisplay(target, self.__items).show_display()


class Item:
    def __init__(self):
        self.name = 'item'
    
    def using_effects(self, target):
        pass


class Apple(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Apple'
        self.__health_restored = 10
    
    def using_effects(self, target):
        super().using_effects(target)

        target.set_health(target.get_health() + self.__health_restored)
        if target.get_health() > 100:
            target.set_health(100)


class Wood(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Wood'
