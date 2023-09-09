class Letterbox:
    def __init__(self, owner):
        self.owner = owner
        self.contains_letter = False
        self.letters = []
    def add_letter(self, letter):
        if self.contains_letter == False:
            self.letters.append(letter)
            print("The letter has been put into the letterbox!")
            self.contains_letter = True
    def empty_letterbox(self):
        self.letters = []
        self.contains_letter = False
        print("The letterbox has been emptied.")