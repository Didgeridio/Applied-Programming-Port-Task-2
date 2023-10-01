from letters import Letter
from letterbox import Letterbox
class Postman:
    def __init__(self, name):
        self.name = name
        self.waiting_for_letter = False
        self.letters = []
    def check_post_office(self, post_office):
        if post_office.letters:
            for letter in post_office.letters:
                self.letters.append(letter)
                print("Charli has picked up the Letter!")
                post_office.empty_letters()
        else:
            print("There are no letters to be delivered at the Post Office")
    def deliver_letter(self):
        if self.letters:
            for letter in self.letters:
                letterbox = Letter.return_address(letter)
                letterbox.add_letter(letter)
            self.letters = []
        else:
            print("Charli has no letters to deliver!")
    def read_letter(self, letter):
        content = letter.read_letter()
        print("Cheeky Charli read the letter!")
        return content



