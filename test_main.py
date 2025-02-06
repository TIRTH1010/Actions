# test_main.py
import unittest
from main import greet

class TestMain(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()