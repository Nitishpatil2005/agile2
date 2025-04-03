import unittest

def add(x, y):
    return x + y

class SimpleTest(unittest.TestCase):
    def test_add(self):  # Better naming convention
        self.assertEqual(add(4, 5), 9)  # Fixed assertEqual

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
