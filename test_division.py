import unittest
from main import division, divisionModified, getItem


class TestDivision(unittest.TestCase):

    def test_division(self):
        self.assertEqual(division(8, 2), 4)
        # self.assertEqual(division(2, 0), "Ошибка деления") # ошибка: ZeroDivisionError: division by zero
        # self.assertEqual(division("Число 2", "Type Error")) # ошибка: TypeError: unsupported operand type(s) for /: 'str' and 'str'

    def test_divisionModified(self):
        self.assertEqual(divisionModified(2, 2), 1)
        self.assertEqual(divisionModified(8.8, 2), 4.4)
        self.assertEqual(divisionModified(
            "Число", 2), "Error: Type Error")
        self.assertEqual(divisionModified(2, 0), "Error: Division zero")

    def test_getItem(self):
        items = [1, 2, 3]

        # вне диапозоне - проходит тест
        self.assertRaises(IndexError, getItem, items, 5)

        # ошибка типа - проходит тест
        self.assertRaises(TypeError, getItem, items, "число 2")

        # ошибка типа - не проходит текст, т.к написан возврат строки
        # self.assertRaises(TypeError, divisionModified, "10", "2")


if __name__ == "__main__":
    unittest.main()
