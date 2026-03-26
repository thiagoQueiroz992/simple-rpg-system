class Question:
    def __init__(self, *options: str):
        self.options = options
        print(self.options)