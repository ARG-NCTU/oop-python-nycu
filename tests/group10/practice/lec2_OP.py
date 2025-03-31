
class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'

def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu

def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        return (0, ())

    elif toConsider[0].getCost() > avail:
        return maxVal(toConsider[1:], avail)

    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:],
                                      avail - nextItem.getCost())
        withVal += nextItem.getValue()

        withoutVal, withoutToTake = maxVal(toConsider[1:],
                                           avail)

        if withVal > withoutVal:
            return (withVal, withToTake + (nextItem,))
        else:
            return (withoutVal, withoutToTake)
        
def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)


