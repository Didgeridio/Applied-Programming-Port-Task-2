class Letter:
    def __init__(self, owner, content):
        self.owner = owner
        self.content = content
        self.opened = False
    def read_letter(self):
        if self.opened == False:
            print("The letter has now been opened and read.")
            self.opened = True
        else:
            print("The letter was already opened!")