class Word:
    word=""
    attempt = 0
    meaning=""

    def __init__(self, word="", attempt=5, meaning=""):
        self.word = word.upper()
        self.attempt = attempt
        self.meaning = meaning
