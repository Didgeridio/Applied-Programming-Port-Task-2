from letters import Letter
class Person:
    def __init__(self, name):
        self.name = name
        self.waiting_for_letter = False
        self.letters = []

    def write_letter(self, content):
        if self.waiting_for_letter == False:
            new_letter = Letter(self, content)
            self.waiting_for_letter = True
            self.letters.append(new_letter)
            print(f"{self.name} has written a new letter!")
            return new_letter
        else:
            print(f"{self.name} is still waiting for a letter...")
            return None

    def send_letter(self, letterbox):
        for letter in self.letters:
            letterbox.add_letter(letter)
        self.letters = []

    def check_letterbox(self, letterbox):
        if letterbox.contains_letter:
            for letter in letterbox.letters:
                self.letters.append(letter)
                self.waiting_for_letter = False
                letterbox.empty_letterbox()
                letter.read_letter()
        else:
            print("The letterbox is empty!")




