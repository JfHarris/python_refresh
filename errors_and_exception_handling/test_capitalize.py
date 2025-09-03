# tests for capitalize.py

# import unittest and scripts to test
import unittest
import capitalize

# test simple things first, grow in complexity

class TestCap(unittest.TestCase):

    def test_one_word(self): # function to test capitalize.py
        text = "python" # test text to pass to cap_text in capitalize.py
        result = capitalize.cap_text(text) # function name from capitalize.py
        self.assertEqual(result, "Python") # we expect result to be Python
    
    def test_multiple_words(self):
        text = "more words"
        result = capitalize.cap_text(text)
        self.assertEqual(result, "More Words")

if __name__ == "__main__":
    unittest.main()