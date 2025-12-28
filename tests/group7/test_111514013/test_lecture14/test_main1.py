from passenger import buildTitanicExamples
from knn import KNearestClassify
from metrics import getStats

examples = buildTitanicExamples('TitanicPassengers.txt')

# Example usage of KNN
def test_main1():
    truePos, falsePos, trueNeg, falseNeg = KNearestClassify(examples, examples, 'Survived', 3)
    getStats(truePos, falsePos, trueNeg, falseNeg)