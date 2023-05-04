class Question:
    def __init__(self, info, statement, alternatives) -> None:
        self.info = info
        self.statement = statement
        self.alternatives = alternatives
        
    def to_html(self):
        alts = ''
        for al in self.alternatives:
            alts += f"<p>{al.letter} - {al.text}</p>"
        return f"<h1>{self.info.num_question}</h1>{self.statement}{alts}"