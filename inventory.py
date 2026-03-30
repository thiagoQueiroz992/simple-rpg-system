class Inventory:
    slots = 10
    
    def __init__(self):
        self.__items = []

    class Item:
        stack_max_item_quant = 16

        def __init__(self, stack_item_quant: int = 1):
            self.__stack_item_quant = stack_item_quant
