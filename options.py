from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich import print
from rich import inspect

class Question:
    def __init__(self, question: str, *options: str):
        self.__question = question
        self.__options = options
    
    def show_question(self) -> int:
        question_box = Panel(self.__question, title='Choose Time', style='bold yellow')
        answer_box = Table(expand=True, show_header=False, style='blue')
        
        answer_box.add_column('Digit', width=-1, justify='center')
        answer_box.add_column('Option')
        
        for i, o in enumerate(self.__options):
            answer_box.add_row(str(i), o, style='cyan bold')
        
        print(question_box)
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


class InventoryDisplay:
    def __init__(self, target, inv: list):
        self.__target = target
        self.__inv = inv

    def show_display(self):
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
            
