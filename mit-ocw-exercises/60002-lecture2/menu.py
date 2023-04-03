import random

class Food(object):
    """
    A food item with a name, value, and calories
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
        return self.get_value() / self.get_cost()

    def __str__(self):
        return (
            self.name + ': <' + str(self.value) +
            ', ' + str(self.calories) + '>'
        )

class Menu(object):
    """
    A menu of food items
    """
    def __init__(self, names, values, calories):
        self.foods = []
        for i in range(len(values)):
            self.foods.append(Food(names[i], values[i],
                              calories[i]))
    
    def get_foods(self):
        return self.foods

    @staticmethod
    def get_foods_str(foods):
        foods_str = ""
        for item in foods:
            foods_str += str(item) + '; '
        return foods_str
    
    def __str__(self):
        return Menu.get_foods_str(self.foods)


def greedy(items, max_cost, key_function):
    """Assumes items a list, max_cost >= 0,
    key_function maps elements of items to numbers"""
    items_copy = sorted(items, key=key_function, reverse=True)
    result = []
    total_value, total_cost = 0.0, 0.0
    for i in range(len(items_copy)):
        if (total_cost + items_copy[i].get_cost()) <= max_cost:
            result.append(items_copy[i])
            total_cost += items_copy[i].get_cost()
            total_value += items_copy[i].get_value()
    return (result, total_value)


#def maxVal(toConsider, avail):
#    """Assumes toConsider a list of items, avail a weight
#       Returns a tuple of the total value of a solution to the
#         0/1 knapsack problem and the items of that solution"""
#    if toConsider == [] or avail == 0:
#        result = (0, ())
#    elif toConsider[0].getCost() > avail:
#        #Explore right branch only
#        result = maxVal(toConsider[1:], avail)
#    else:
#        nextItem = toConsider[0]
#        #Explore left branch
#        withVal, withToTake = maxVal(toConsider[1:],
#                                     avail - nextItem.getCost())
#        withVal += nextItem.getValue()
#        #Explore right branch
#        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
#        #Choose better branch
#        if withVal > withoutVal:
#            result = (withVal, withToTake + (nextItem,))
#        else:
#            result = (withoutVal, withoutToTake)
#    return result
#
#def buildLargeMenu(numItems, maxVal, maxCost):
#    items = []
#    for i in range(numItems):
#        items.append(Food(str(i),
#                          random.randint(1, maxVal),
#                          random.randint(1, maxCost)))
#    return items
#
#def fastMaxVal(toConsider, avail, memo = {}):
#    """Assumes toConsider a list of subjects, avail a weight
#         memo supplied by recursive calls
#       Returns a tuple of the total value of a solution to the
#         0/1 knapsack problem and the subjects of that solution"""
#    if (len(toConsider), avail) in memo:
#        result = memo[(len(toConsider), avail)]
#    elif toConsider == [] or avail == 0:
#        result = (0, ())
#    elif toConsider[0].getCost() > avail:
#        #Explore right branch only
#        result = fastMaxVal(toConsider[1:], avail, memo)
#    else:
#        nextItem = toConsider[0]
#        #Explore left branch
#        withVal, withToTake =\
#                 fastMaxVal(toConsider[1:],
#                            avail - nextItem.getCost(), memo)
#        withVal += nextItem.getValue()
#        #Explore right branch
#        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
#                                                avail, memo)
#        #Choose better branch
#        if withVal > withoutVal:
#            result = (withVal, withToTake + (nextItem,))
#        else:
#            result = (withoutVal, withoutToTake)
#    memo[(len(toConsider), avail)] = result
#    return result

