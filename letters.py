class Letter:
    def __init__(self, owner, address, content):
        self.owner = owner
        self.content = content
        self.address = address
        self.encrypted = False
        self.opened = False
    def read_letter(self):
        if self.opened == False:
            print("The letter has now been opened and read.")
            self.opened = True
            return self.content
        else:
            print("The letter was already opened!")
            return self.content
    def apply_encryption(self):
        self.encrypted = True
    def return_encryption(self):
        return self.encrypted
    def return_address(self):
        return self.address