from rich import inspect
from options import Question, InventoryDisplay
from os import system

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
                    self.__items.append({'item': item, 'amount': a})
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
    
    def selection_mode(self, target):
        system('cls')
        self.display_inventory(target)
        selection = Question('Enter a item\'s slot position:', '0', multi_choice=False, max_range=self.slots).show_question()
        if len(self.__items) - 1 < selection or self.__items == False:
            print('There\'s no item in this slot.')
            self.selection_mode(target)
        else:
            self.use_item(selection, target)
            print('You used the item.')


class Item:
    def __init__(self):
        self.name = 'item'


class Apple(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Apple'
        self.__health_restored = 10
    
    def using_effects(self, target):
        target.set_health(target.get_health() + self.__health_restored)
        if target.get_health() > 100:
            target.set_health(100)


class Wood(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Wood'


class Sword(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Sword'
        self.__damage = 35
    
    def using_effects(self, target):
        target.equipped_weapon = self
        target.set_attack(self.__damage)


class Bone(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Bone'


class Wire(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Wire'


class Ingot(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Ingot'


class Coin(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Coin'


class Meat(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Meat'
        self.__health_restored = 15
    
    def using_effects(self, target):
        target.set_health(target.get_health() + self.__health_restored)
        if target.get_health() > 100:
            target.set_health(100)


class LegendarySword(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Legendary Sword'
        self.__damage = 60
    
    def using_effects(self, target):
        target.equipped_weapon = self
        target.set_attack(self.__damage)
