class Alternative:
    def __init__(self, letter, text) -> None:
        self.letter = letter
        self.text = text
        
    def to_string(self):
        return f'{self.letter} - {self.text}'