
class Food(object):
    """A food item with a name, value, and calories

    attributes:
    value: a number representing the value of the food
    calories: a number representing the calories of the food
    name: a string representing the name of the food
    
    """
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def get_value(self):
        return self.value
    def get_cost(self):
        return self.calories
    def density(self):
        return self.get_value()/self.get_cost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'

def build_menu(names, values, calories):
    """names, values, calories lists of same length.
       name a list of strings
       values and calories lists of numbers
       returns list of Foods"""
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu

def greedy(items, max_cost, key_function):
    """Assumes items a list, max_cost >= 0,
         key_function maps elements of items to numbers"""
    items_copy = sorted(items, key = key_function,
                       reverse = True)
    result = []
    total_value, total_cost = 0.0, 0.0
    for i in range(len(items_copy)):
        if (total_cost+items_copy[i].get_cost()) <= max_cost:
            result.append(items_copy[i])
            total_cost += items_copy[i].get_cost()
            total_value += items_copy[i].get_value()
    return (result, total_value)

def test_greedy(items, constraint, key_function):
    taken, val = greedy(items, constraint, key_function)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)

def test_greedys(foods, max_units):
    print('Use greedy by value to allocate', max_units,
          'calories')
    test_greedy(foods, max_units, Food.get_value)
    print('\nUse greedy by cost to allocate', max_units,
          'calories')
    test_greedy(foods, max_units,
               lambda x: 1/Food.get_cost(x))
    print('\nUse greedy by density to allocate', max_units,
          'calories')
    test_greedy(foods, max_units, Food.density)


names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = build_menu(names, values, calories)
test_greedys(foods, 1000)
