from add_path import add_path
add_path()

import random

class Food:
    """A food item with a name, value, and calories."""
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def get_value(self):
        return self.value

    def get_cost(self):
        return self.calories

    def density(self):
        return self.get_value() / self.get_cost()

    def __str__(self):
        return f"{self.name}: <{self.value}, {self.calories}>"


class Menu:
    """A menu of food items."""
    def __init__(self, names=None, values=None, calories=None):
        if names is None:
            names = []
        if values is None:
            values = []
        if calories is None:
            calories = []
        self.foods = []
        for i in range(len(values)):
            self.foods.append(Food(names[i], values[i], calories[i]))

    def build_large_menu(self, num_items, max_val, max_cost):
        """Build a random menu with given number of items."""
        self.foods = []
        for i in range(num_items):
            self.foods.append(
                Food(str(i),
                     random.randint(1, max_val),
                     random.randint(1, max_cost))
            )

    def get_foods(self):
        return self.foods

    @staticmethod
    def get_foods_str(foods):
        """Return a string representation of a list of Food objects."""
        return "; ".join(str(item) for item in foods)

    def __str__(self):
        return Menu.get_foods_str(self.foods)


# --------------------- Greedy Algorithm ---------------------
def greedy(items, max_cost, key_function):
    """A greedy algorithm to pick items based on a given key function."""
    items_copy = sorted(items, key=key_function, reverse=True)
    result = []
    total_value, total_cost = 0.0, 0.0
    for item in items_copy:
        if total_cost + item.get_cost() <= max_cost:
            result.append(item)
            total_cost += item.get_cost()
            total_value += item.get_value()
    return (result, total_value)


# --------------------- Recursive 0/1 Knapsack ---------------------
def max_val(to_consider, avail):
    """Recursive brute-force search for the best combination."""
    if not to_consider or avail == 0:
        result = (0, ())
    elif to_consider[0].get_cost() > avail:
        result = max_val(to_consider[1:], avail)
    else:
        next_item = to_consider[0]
        with_val, with_to_take = max_val(to_consider[1:], avail - next_item.get_cost())
        with_val += next_item.get_value()
        without_val, without_to_take = max_val(to_consider[1:], avail)
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
        else:
            result = (without_val, without_to_take)
    return result


# --------------------- Memoized 0/1 Knapsack ---------------------
def fast_max_val(to_consider, avail, memo=None):
    """Optimized 0/1 knapsack using memoization."""
    if memo is None:
        memo = {}
    if (len(to_consider), avail) in memo:
        return memo[(len(to_consider), avail)]
    elif not to_consider or avail == 0:
        result = (0, ())
    elif to_consider[0].get_cost() > avail:
        result = fast_max_val(to_consider[1:], avail, memo)
    else:
        next_item = to_consider[0]
        with_val, with_to_take = fast_max_val(to_consider[1:], avail - next_item.get_cost(), memo)
        with_val += next_item.get_value()
        without_val, without_to_take = fast_max_val(to_consider[1:], avail, memo)
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
        else:
            result = (without_val, without_to_take)
    memo[(len(to_consider), avail)] = result
    return result


# --------------------- Main Program ---------------------
def main():
    names = ['apple', 'banana', 'cake', 'steak', 'wine', 'nuts']
    values = [50, 40, 100, 200, 150, 160]
    calories = [60, 30, 150, 300, 200, 180]

    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    max_calories = 500

    print("Menu:")
    print(menu)
    print(f"\nMaximum calories allowed = {max_calories}\n")

    # Greedy by value
    taken, val = greedy(foods, max_calories, Food.get_value)
    print(f"[Greedy by value] total value = {val}")
    print(Menu.get_foods_str(taken), "\n")

    # Greedy by cost
    taken, val = greedy(foods, max_calories, lambda x: 1 / x.get_cost())
    print(f"[Greedy by cost] total value = {val}")
    print(Menu.get_foods_str(taken), "\n")

    # Greedy by density
    taken, val = greedy(foods, max_calories, Food.density)
    print(f"[Greedy by density] total value = {val}")
    print(Menu.get_foods_str(taken), "\n")

    # Brute force
    val, taken = max_val(foods, max_calories)
    print(f"[Brute force recursion] total value = {val}")
    print(Menu.get_foods_str(taken), "\n")

    # Memoized
    val, taken = fast_max_val(foods, max_calories)
    print(f"[Memoized recursion] total value = {val}")
    print(Menu.get_foods_str(taken), "\n")


if __name__ == "__main__":
    main()
