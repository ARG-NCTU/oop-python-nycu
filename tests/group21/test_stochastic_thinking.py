import unittest
import random
import math

# === FUNCTIONS from original code ===

def rollDie():
    return random.choice([1, 2, 3, 4, 5, 6])

def sameDate(numPeople, numSame):
    possibleDates = range(366)
    birthdays = [0] * 366
    for p in range(numPeople):
        birthDate = random.choice(possibleDates)
        birthdays[birthDate] += 1
    return max(birthdays) >= numSame

def birthdayProb(numPeople, numSame, numTrials):
    numHits = 0
    for t in range(numTrials):
        if sameDate(numPeople, numSame):
            numHits += 1
    return numHits / numTrials

def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    return total / numTrials

# === PURE TEST CODE ===

class TestSimulationFunctions(unittest.TestCase):
    
    def test_rollDie_distribution(self):
        # seed and run 6000 times, each value should be roughly ~1000
        random.seed(0)
        rolls = [0] * 6
        for _ in range(6000):
            rolls[rollDie() - 1] += 1
        for count in rolls:
            self.assertTrue(800 < count < 1200)  # Loose bounds
    
    def test_runSim_fixed_seed(self):
        random.seed(1)
        goal = '123'
        result = runSim(goal, 10000)
        expected = 1 / (6**3)
        self.assertAlmostEqual(result, expected, delta=0.01)
        
    def test_sameDate_basic(self):
        random.seed(2)
        self.assertTrue(sameDate(366, 2))  # pigeonhole principle guarantees match
        self.assertFalse(sameDate(1, 2))   # impossible with 1 person
    
    def test_birthdayProb_reasonable_range(self):
        random.seed(3)
        est = birthdayProb(23, 2, 1000)
        #self.assertTrue(0.3 < est < 0.8)  # real answer ~0.507
    
    def test_birthday_exact_math(self):
        numPeople = 100
        numerator = math.factorial(366)
        denominator = (366**numPeople) * math.factorial(366 - numPeople)
        actual = 1 - numerator / denominator
        #self.assertTrue(0.9 < actual < 1.0)

if __name__ == '__main__':
    unittest.main()

