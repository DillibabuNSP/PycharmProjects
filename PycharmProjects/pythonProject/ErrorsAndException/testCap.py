import unittest
import Cap


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = Cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = Cap.cap_text(text)
        self.assertEqual(result, 'Monty python')


if __name__ == '__main__':
    unittest.main()
