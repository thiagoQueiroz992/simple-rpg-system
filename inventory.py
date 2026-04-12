from rich import inspect, print
from options import Question, InventoryDisplay
from os import system
from time import sleep

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
        try:
            self.__items[slot]['item'].using_effects(target)
        except:
            print('[red bold]This item cannot be used.[/red bold]')
            sleep(1.5)
        else:
            if self.__items[slot]['item'].can_be_used:
                self.__items[slot]['amount'] -= 1
                if self.__items[slot]['amount'] == 0:
                    self.__items.pop(slot)
            else:
                print('[red bold]' + self.__items[slot]['item'].reason + '[/red bold]')
                sleep(1.5)
    
    def display_inventory(self, target):
        InventoryDisplay(target, self.__items).show_display()
    
    def selection_mode(self, target, mode = 'use'):
        system('cls')
        self.display_inventory(target)
        selection = Question('Enter a item\'s slot position:', '0', question_type='range', max_range=self.slots).show_question()
        if len(self.__items) - 1 < selection or self.__items == False:
            print('[red bold]There\'s no item in this slot.[/red bold]')
            sleep(1.5)
            self.selection_mode(target)
        else:
            if mode == 'use':
                self.use_item(selection, target)
            elif mode == 'destroy':
                self.__items.pop(selection)
            else:
                print(f'Sorry, the mode {mode} does not exist.')


class Item:
    def __init__(self):
        self.name = 'item'
        self.can_be_used = True


class Apple(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Apple'
        self.__health_restored = 10
        self.reason = ''
    
    def using_effects(self, target):
        if target.get_health() < target.default_max_health:
            self.can_be_used = True
            target.set_health(target.get_health() + self.__health_restored)
            if target.get_health() > target.default_max_health:
                target.set_health(100)
        else:
            self.can_be_used = False
            self.reason = f'{target.name}\'s health is full.'


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
        if target.equipped_weapon != None:
            target.get_inventory().add_item(target.equipped_weapon)
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
        if target.equipped_weapon != None:
            target.get_inventory().add_item(target.equipped_weapon)
        target.equipped_weapon = self
        target.set_attack(self.__damage)
