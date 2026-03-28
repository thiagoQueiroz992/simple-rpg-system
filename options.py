from rich.table import Table
from rich.panel import Panel
from rich import print

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
