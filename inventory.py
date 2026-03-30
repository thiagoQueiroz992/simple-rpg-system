from rich import inspect

class Inventory:
    slots = 10
    
    def __init__(self):
        self.__items = []


class Item:
    stack_max_items = 16

    def __init__(self, amount: int = 1):
        self.amount = amount
