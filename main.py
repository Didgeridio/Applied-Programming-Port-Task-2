from letters import Letter
from resident import Resident
from letterbox import Letterbox
from post_office import PostOffice
from postman import Postman
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.bob = Resident("Bob")
        self.alice = Resident("Alice")
        self.bob_letterbox = Letterbox(self.bob)
        self.alice_letterbox = Letterbox(self.alice)
        self.charli = Postman("Charli")
        self.postoffice = PostOffice("Post Office")

    '''Checks that non-encrypted letters can still be sent if specified'''
    def test_bob_write_letter_to_alice(self):
        print("\n")
        content = "The mission proceeds as planned at 1800 Thursday sharp."
        letter = self.bob.write_letter(content, self.alice_letterbox)
        self.bob.send_letter(self.postoffice)
        self.charli.check_post_office(self.postoffice)
        self.charli.deliver_letter()
        self.assertIn(letter, self.alice_letterbox.letters)
        self.alice.check_letterbox(self.alice_letterbox)
        self.assertTrue(self.bob.waiting_for_letter)
        self.assertTrue(letter.opened)

    '''Checks that sending encrypted letters do indeed work and that they are encrypted and then correctly delivered, 
    decrypted, and read on the receiving side.'''
    def test_alice_send_encrypted_letter_to_bob(self):
        print("\n")
        content = "This line of communication has been compromised. Abort mission."
        print(f"The content is: {content}")
        letter = self.alice.write_letter(content, self.bob_letterbox, encrypted=True)
        self.assertTrue(letter.content, "Znoy rotk ul iussatoigzout ngy hkkt iusvxusoykj. Ghuxz soyyout.")
        self.alice.send_letter(self.postoffice)
        self.charli.check_post_office(self.postoffice)
        self.charli.deliver_letter()
        self.assertTrue(letter.encrypted)
        self.assertIn(letter, self.bob_letterbox.letters)
        self.bob.check_letterbox(self.bob_letterbox)
        self.assertTrue(self.alice.waiting_for_letter)
        self.assertTrue(letter.opened)
        self.assertTrue(letter.content, "This line of communication has been compromised. Abort mission.")

    '''Checks that checking an empty letterbox will leave the recipient as still waiting for a letter'''
    def test_bob_check_empty_letterbox(self):
        print("\n")
        self.bob.waiting_for_letter = True
        self.bob.check_letterbox(self.bob_letterbox)
        #Check that Bob is still waiting and that both he and the letterbox do not have a letter
        self.assertTrue(self.bob.waiting_for_letter)
        self.assertTrue(self.bob.letters == [])
        self.assertTrue(self.bob_letterbox.letters == [])

    '''Checks that a resident can not create a letter and post it while they are still waiting for one'''
    def test_writing_letter_while_waiting(self):
        print("\n")
        content = "Bravo respond have you been compromised?"
        self.bob.waiting_for_letter = True
        letter = self.bob.write_letter(content, self.alice, encrypted=True)
        self.assertTrue(self.bob.waiting_for_letter)
        self.assertNotIn(letter, self.bob.letters)

    '''Checks that if Charli snoops and reads an encrypted letter before delivery it is properly marked as read
    and its contents are still encrypted and unreadable.'''
    def test_charli_opens_letter_before_delivering(self):
        print("\n")
        content = "This line of communication has been compromised. Abort mission."
        print(f"The content is: {content}")
        letter = self.alice.write_letter(content, self.bob_letterbox, encrypted=True)
        self.alice.send_letter(self.postoffice)
        self.charli.check_post_office(self.postoffice)
        self.charli.read_letter(letter)
        print(letter.content)
        self.assertTrue(letter.opened)
        self.assertTrue(letter.content, "Znoy rotk ul iussatoigzout ngy hkkt iusvxusoykj. Ghuxz soyyout.")
        self.charli.deliver_letter()
        self.assertTrue(letter.encrypted)
        self.assertIn(letter, self.bob_letterbox.letters)
        self.bob.check_letterbox(self.bob_letterbox)
        self.assertTrue(self.alice.waiting_for_letter)
        self.assertTrue(letter.opened)
        self.assertTrue(letter.content, "This line of communication has been compromised. Abort mission.")


if __name__ == '__main__':
    unittest.main()






