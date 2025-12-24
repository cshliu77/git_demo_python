import unittest
from main import additionMethod, subtractionMethod, divisionMethod, multiplicationMethod

class TestMain(unittest.TestCase):

    def test_additionMethod(self):
        self.assertEqual(additionMethod(2, 3), 5)
        self.assertEqual(additionMethod(-1, 1), 0)
        self.assertEqual(additionMethod(0, 0), 0)

    def test_subtractionMethod(self):
        self.assertEqual(subtractionMethod(5, 3), 2)
        self.assertEqual(subtractionMethod(1, 1), 0)
        self.assertEqual(subtractionMethod(10, 5), 5)

    def test_multiplicationMethod(self):
        self.assertEqual(multiplicationMethod(2, 3), 6)
        self.assertEqual(multiplicationMethod(-1, 5), -5)
        self.assertEqual(multiplicationMethod(0, 100), 0)

    def test_divisionMethod(self):
        self.assertEqual(divisionMethod(6, 3), 2)
        self.assertEqual(divisionMethod(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            divisionMethod(5, 0)

if __name__ == '__main__':
    unittest.main()
