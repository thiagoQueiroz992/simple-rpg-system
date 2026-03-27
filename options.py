class Question:
    def __init__(self, question: str, *options: str):
        self.question = question
        self.options = options
    
    def show_question(self) -> int:
        print(self.question)
        for i, o in enumerate(self.options):
            print(f'[ {i} ] >>> {o}')
        while True:
            try:
                answer = int(input(''))
            except (KeyboardInterrupt, ValueError):
                print('Invalid input!')
                continue
            else:
                if answer in range(0, len(self.options)):
                    return answer
                else:
                    print('Invalid input!')
                    continue
