from letters import Letter
from person import Person
from letterbox import Letterbox
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.bob = Person("Bob")
        self.alice = Person("Alice")
        self.bob_letterbox = Letterbox(self.bob)
        self.alice_letterbox = Letterbox(self.alice)

    def test_bob_write_letter_to_alice(self):
        #Tests the ability to write and send a letter
        content = "I'm going to sneak in tonight at 8pm, leave the window open please."
        letter = self.bob.write_letter(content)
        self.bob.send_letter(self.alice_letterbox)
        #Now check that the letter is in Alice's letterbox
        #and that Bob is waiting for a letter
        self.assertIn(letter, self.alice_letterbox.letters)
        self.assertTrue(self.bob.waiting_for_letter)

    def test_alice_read_letter(self):
        #Tests the ability to read a letter
        content = "I'm going to sneak in tonight at 8pm, leave the window open please."
        letter = self.bob.write_letter(content)
        self.bob.send_letter(self.alice_letterbox)
        self.alice.check_letterbox(self.alice_letterbox)
        #Now check that the letter is read
        #And that Alice is no longer waiting for a letter and is holding the letter
        self.assertTrue(letter.opened)
        self.assertFalse(self.alice.waiting_for_letter)
        self.assertIn(letter, self.alice.letters)

    def test_bob_check_empty_letterbox(self):
        self.bob.waiting_for_letter = True
        self.bob.check_letterbox(self.bob_letterbox)
        #Check that Bob is still waiting and that both he and the letterbox do not have a letter
        self.assertTrue(self.bob.waiting_for_letter)
        self.assertTrue(self.bob.letters == [])
        self.assertTrue(self.bob_letterbox.letters == [])

    def test_writing_letter_while_waiting(self):
        content = "Why aren't you replying to me was it something I said?"
        self.bob.waiting_for_letter = True
        letter = self.bob.write_letter(content)
        #Check that Bob can't write another letter no matter how desperate he is
        self.assertTrue(self.bob.waiting_for_letter)
        self.assertNotIn(letter, self.bob.letters)


if __name__ == '__main__':
    unittest.main()






