class PostOffice:
    def __init__(self, name):
        self.name = name
        self.letters = []
    def add_letter(self, letter):
        self.letters.append(letter)
        print("The letter has been put in the drop box!")
    def empty_letters(self):
        self.letters = []
        print("There are now no letters at the Post Office")