import unittest
from menu import Food, Menu, greedy, max_val, fast_max_val

class TestMenuFunctions(unittest.TestCase):

    def setUp(self):
        self.foods = [
            Food("apple", 50, 30),
            Food("banana", 60, 20),
            Food("cherry", 70, 40)
        ]
        self.menu = Menu(
            names=["apple", "banana", "cherry"],
            values=[50, 60, 70],
            calories=[30, 20, 40]
        )

    def test_food_methods(self):
        apple = self.foods[0]
        self.assertEqual(apple.get_value(), 50)
        self.assertEqual(apple.get_cost(), 30)
        self.assertAlmostEqual(apple.density(), 50 / 30)
        self.assertEqual(str(apple), "apple: <50, 30>")

    def test_menu_methods(self):
        self.assertEqual(len(self.menu.get_foods()), 3)
        self.assertIn("apple: <50, 30>", str(self.menu))
        self.menu.build_large_menu(5, 100, 50)
        self.assertEqual(len(self.menu.get_foods()), 5)

    def test_greedy(self):
        result, total_value = greedy(self.foods, 50, lambda x: x.get_value())
        self.assertEqual(total_value, 110)
        self.assertEqual(len(result), 2)

        result, total_value = greedy(self.foods, 50, lambda x: 1 / x.get_cost())
        self.assertEqual(total_value, 110)
        self.assertEqual(len(result), 2)

    def test_max_val(self):
        total_value, items = max_val(self.foods, 50)
        self.assertEqual(total_value, 110)
        self.assertEqual(len(items), 2)

    def test_fast_max_val(self):
        total_value, items = fast_max_val(self.foods, 50)
        self.assertEqual(total_value, 110)
        self.assertEqual(len(items), 2)

def test_menu():
    # Test Menu class basic functionality
    names = ["apple", "banana", "cherry"]
    values = [50, 60, 70]
    calories = [95, 105, 120]
    menu = Menu(names, values, calories)

    # Test get_foods method
    foods = menu.get_foods()
    assert len(foods) == 3
    assert str(foods[0]) == "apple: <50, 95>"
    assert str(foods[1]) == "banana: <60, 105>"
    assert str(foods[2]) == "cherry: <70, 120>"

    # Test __str__ method
    assert str(menu) == "apple: <50, 95>; banana: <60, 105>; cherry: <70, 120>; "

if __name__ == "__main__":
    unittest.main()
