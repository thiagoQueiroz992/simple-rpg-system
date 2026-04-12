import random
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich import print
from rich import inspect
from os import system

class Question:
    def __init__(self, question: str, *options: str, question_type = 'multi_choice', min_range: int = 0, max_range: int = 1):
        self.__question = question
        self.__options = options
        self.__question_type = question_type
        self.__min_range = min_range
        self.__max_range = max_range
    
    def show_question(self) -> int | str:
        question_box = Panel(self.__question, title='Choose Time', style='bold yellow')
        answer_box = Table(expand=True, show_header=False, style='blue')

        print(question_box)
        
        match self.__question_type:
            case 'multi_choice':
                answer_box.add_column('Digit', width=-1, justify='center')
                answer_box.add_column('Option')
                
                for i, o in enumerate(self.__options):
                    answer_box.add_row(str(i), o, style='cyan bold')
                
                print(answer_box)
                
                while True:
                    try:
                        answer = int(input(''))
                    except (KeyboardInterrupt, ValueError):
                        print('[red bold]Invalid input![/red bold]')
                        continue
                    else:
                        if answer in range(0, len(self.__options)):
                            return answer
                        else:
                            print('[red bold]Invalid input![/red bold]')
                            continue
            
            case 'range':
                while True:
                    try:
                        answer = int(input(''))
                    except (KeyboardInterrupt, ValueError):
                        print('[red bold]Invalid input![/red bold]')
                        continue
                    else:                       
                        if answer in range(self.__min_range, self.__max_range):
                            return answer
                        else:
                            print('[red bold]Invalid input![/red bold]')
            
            case 'text':
                while True:
                    try:
                        answer = str(input(''))
                    except (KeyboardInterrupt, ValueError):
                        print('[red bold]Invalid input![/red bold]')
                        continue
                    else:
                        return answer


class InventoryDisplay:
    def __init__(self, target, inv: list):
        self.__target = target
        self.__inv = inv

    def show_display(self):
        system('cls')
        header = Panel(Align('INVENTORY', align='center'), title=self.__target.name, style='yellow bold')
        item_display = Table(style='blue bold', show_header=False, expand=True)
        item_display.add_column('SLOT', width=-2)
        item_display.add_column('ITEM', width=4)
        item_display.add_column('AMOUNT', width=-2)

        print(header)
        for i, s in enumerate(self.__inv):
            item_display.add_row(Align(str(i), align='center'), s['item'].name, Align(str(s['amount']), align='center'))
        
        if len(self.__inv) < 10:
            for r in range(len(self.__inv), 10):
                item_display.add_row(Align(str(r), align='center'), '---', '---')
        print(item_display)
            

class StatusDisplay:
    def __init__(self, target):
        self.__target = target
    
    def show_display(self):
        system('cls')
        header = Panel(Align('STATUS', align='center'), title=self.__target.name, style='yellow bold')
        status_display = Table(style='blue bold', show_header=False, expand=True)
        status_display.add_column('STATUS', width=0)
        status_display.add_column('VALUE', width=3)

        status_display.add_row(Align('[cyan bold]Name[/cyan bold]', align='center'), Align(self.__target.name, align='center'))
        status_display.add_row(Align('[cyan bold]Health[/cyan bold]', align='center'), Align(str(self.__target.get_health()) + ' HP', align='center'))
        status_display.add_row(Align('[cyan bold]Attack[/cyan bold]', align='center'), Align(str(self.__target.get_attack()), align='center'))
        status_display.add_row(Align('[cyan bold]Weapon[/cyan bold]', align='center'), Align(self.__target.equipped_weapon.name if self.__target.equipped_weapon != None else 'In hand and in faith', align='center'))

        print(header)
        print(status_display)


class LootGenerator:
    def __init__(self, loot_table: list):
        self.__loot_table = loot_table
        self.__loot_items = []
    
    def generate_loot(self) -> list:
        for i in self.__loot_table:
            if random.random() <= i[1] * 0.01:
                item_quant = random.randint(i[2], i[3])
                self.__loot_items.append([i[0](), item_quant])
        random.shuffle(self.__loot_items)
        return self.__loot_items


class LootDisplay:
    def __init__(self, target, loot_items: list):
        self.__target = target
        self.__loot = loot_items
    
    def show_display(self) -> None:
        system('cls')
        header = Panel(Align('LOOT', align='center'), title=self.__target.name, style='yellow bold')
        loot_display = Table(style='blue bold', show_header=False, expand=True)
        loot_display.add_column('ITEM', width=3)
        loot_display.add_column('AMOUNT', width=0)

        for l in self.__loot:
            loot_display.add_row(l[0].name, str(l[1]))
        
        print(header)
        print(loot_display)
    
    def collect(self, target_inventory):
        take = Question('Collect loot?', 'YES', 'NO').show_question()

        if take == 0:
            for i in self.__loot:
                target_inventory.add_item(i[0], i[1])
