from letters import Letter
class Resident:
    def __init__(self, name):
        self.name = name
        self.waiting_for_letter = False
        self.letters = []

    def send_letter(self, letterbox):
        for letter in self.letters:
            letterbox.add_letter(letter)
        self.letters = []

    '''Simple encryption using the alphabet to move letters along its index. Quite simple to crack
    but also simple to implement so felt realistic for this scenario. Is optionally called during the 
    write_letter() function. Its sister function decrypt_letter() simply solves the encryption
    and returns the original content of the letter'''
    def encrypt_letter(self, content, key):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        encrypted_text = ""
        for character in content:
            if character.isalpha():
                is_upper = character.isupper()
                character = character.upper()
                if character in alphabet:
                    position = alphabet.index(character)
                    encrypted_position = (position + key) % 26
                    encrypted_character = alphabet[encrypted_position]
                    if not is_upper:
                        encrypted_character = encrypted_character.lower()
                    encrypted_text += encrypted_character
                else:
                    #If it is a symbol write it normally
                    encrypted_text += character
            else:
                encrypted_text += character
        return encrypted_text
    def decrypt_letter(self, content, key):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        decrypted_text = ""
        for character in content:
            if character.isalpha():
                is_upper = character.isupper()
                character = character.upper()
                if character in alphabet:
                    position = alphabet.index(character)
                    decrypted_position = (position - key) % 26
                    decrypted_character = alphabet[decrypted_position]
                    if not is_upper:
                        decrypted_character = decrypted_character.lower()
                    decrypted_text += decrypted_character
                else:
                    # If it is a symbol write it normally
                    decrypted_text += character
            else:
                decrypted_text += character
        return decrypted_text

    '''Writes a letter and encrypts it using encrypt_letter() if it is specified within the call of the function.
    The letter is then added to the Residents list of letters and they are set to be waiting for a letter.'''
    def write_letter(self, content, address, encrypted=False):
        if self.waiting_for_letter == False:
            if encrypted:
                encrypted_content = self.encrypt_letter(content, 6)
                encrypted_letter = Letter(self, address, encrypted_content)
                Letter.apply_encryption(encrypted_letter)
                self.waiting_for_letter = True
                self.letters.append(encrypted_letter)
                print(f"{self.name} has written an encrypted letter!")
                return encrypted_letter
            else:
                new_letter = Letter(self, address, content)
                self.waiting_for_letter = True
                self.letters.append(new_letter)
                print(f"{self.name} has written a new letter!")
                return new_letter
        else:
            print(f"{self.name} is still waiting for a letter...")
            return None

    '''Checks the letterbox for a letter and if there is one reads it. If it is encrypted it first decrypts 
    the letter and then reads its contents'''
    def check_letterbox(self, letterbox):
        if letterbox.contains_letter:
            for letter in letterbox.letters:
                self.letters.append(letter)
                self.waiting_for_letter = False
                letterbox.empty_letters()
                encryption = Letter.return_encryption(letter)
                if encryption:
                    encrypted_content = letter.read_letter()
                    decrypted_content = self.decrypt_letter(encrypted_content, 6)
                    print(f"The Letter was successfully received, decrypted and reads: {decrypted_content}")
                else:
                    content = letter.read_letter()
                    print(f"The Letter was successfully received and reads: {content}")
        else:
            print("The letterbox is empty!")