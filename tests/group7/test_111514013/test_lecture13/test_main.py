from passenger import buildTitanicExamples
from knn import KNearestClassify
from metrics import getStats

examples = buildTitanicExamples('TitanicPassengers.txt')
def test_main():
    # Example usage of KNN
    truePos, falsePos, trueNeg, falseNeg = KNearestClassify(examples, examples, 'Survived', 3)
    getStats(truePos, falsePos, trueNeg, falseNeg)