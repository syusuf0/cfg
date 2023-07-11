## 2.1 def is_isogram(word):
    """
    Function to verify if a word is an isogram.

    Parameters:
    word (str): The word to verify.

    Returns:
    bool: True if the word is an isogram, False otherwise.
    """
    word = word.lower() # adjust to lower case to deal with capital letters
    return len(word) == len(set(word)) # If the letters are different then it is an isogram

## 2.2 import unittest
from script import is_isogram #script is the name containing the is_isogram function

class TestIsIsogram(unittest.TestCase):
    ## states the test cases in the setUp method
    def setUp(self):
        self.test_cases = {
            'isogram': True, # letters in this are not the same , should return True
            'geeks': False, # letters are repeated, should return False
            '': True, # unfilled string, not repeated, should return True
            'IsOgram': True, # different case but emplyoing the same cases, expected to still return True
        }

    def test_cases(self):
        for word, expected_result in self.test_cases.items():
            with self.subTest(word=word):
                self.assertEqual(is_isogram(word), expected_result)

# This enables it to run as a script  and calls out the test() method
if __name__ == '__main__':
    unittest.main()
