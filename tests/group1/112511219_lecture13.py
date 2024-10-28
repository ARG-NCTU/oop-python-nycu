import pytest
import lecture13
import random
import sklearn.linear_model

def test_minkowskiDist():
    assert lecture13.minkowskiDist([1, 2], [4, 6], 2) == pytest.approx(5.0)

def test_animal_class():
    animal1 = lecture13.Animal('dog', [1, 2, 3])
    animal2 = lecture13.Animal('cat', [4, 5, 6])
    assert animal1.getName() == 'dog'
    assert (animal1.getFeatures() == [1, 2, 3]).all()
    assert animal1.distance(animal2) == pytest.approx(5.196152422706632)

def test_passenger_class():
    passenger = lecture13.Passenger(1, 29.0, 1, 'Survived', 'John Doe')
    assert passenger.getClass() == 1
    assert passenger.getAge() == 29.0
    assert passenger.getGender() == 1
    assert passenger.getName() == 'John Doe'
    assert passenger.getFeatures() == [1, 0, 0, 29.0, 1]
    assert passenger.getLabel() == 'Survived'

def test_getTitanicData():
    data = lecture13.getTitanicData('TitanicPassengers.txt')
    assert len(data['class']) > 0
    assert len(data['age']) > 0
    assert len(data['gender']) > 0
    assert len(data['survived']) > 0
    assert len(data['name']) > 0

def test_buildTitanicExamples():
    examples = lecture13.buildTitanicExamples('TitanicPassengers.txt')
    assert len(examples) > 0
    assert isinstance(examples[0], lecture13.Passenger)

def test_findNearest():
    examples = lecture13.buildTitanicExamples('TitanicPassengers.txt')
    nearest = lecture13.findNearest(examples[0].getName(), examples, lecture13.Passenger.distance)
    assert isinstance(nearest, lecture13.Passenger)

def test_accuracy():
    assert lecture13.accuracy(50, 10, 30, 10) == pytest.approx(0.8)

def test_sensitivity():
    assert lecture13.sensitivity(50, 10) == pytest.approx(0.8333333333333334)

def test_specificity():
    assert lecture13.specificity(30, 10) == pytest.approx(0.75)

def test_posPredVal():
    assert lecture13.posPredVal(50, 10) == pytest.approx(0.8333333333333334)

def test_negPredVal():
    assert lecture13.negPredVal(30, 10) == pytest.approx(0.75)

def test_getStats():
    stats = lecture13.getStats(50, 10, 30, 10, toPrint=False)
    assert stats == (0.8, 0.8333333333333334, 0.75, 0.8333333333333334)

def test_findKNearest():
    examples = lecture13.buildTitanicExamples('TitanicPassengers.txt')
    nearest, distances = lecture13.findKNearest(examples[0], examples, 3)
    assert len(nearest) == 3
    assert len(distances) == 3

def test_KNearestClassify():
    examples = lecture13.buildTitanicExamples('TitanicPassengers.txt')
    trainingSet, testSet = lecture13.split80_20(examples)
    results = lecture13.KNearestClassify(trainingSet, testSet, 'Survived', 3)
    assert len(results) == 4

def test_leaveOneOut():
    examples = lecture13.buildTitanicExamples('TitanicPassengers.txt')
    results = lecture13.leaveOneOut(examples, lecture13.knn, toPrint=False)
    assert len(results) == 4

def test_split80_20():
    examples = lecture13.buildTitanicExamples('TitanicPassengers.txt')
    trainingSet, testSet = lecture13.split80_20(examples)
    assert len(trainingSet) > 0
    assert len(testSet) > 0

def test_randomSplits():
    examples = lecture13.buildTitanicExamples('TitanicPassengers.txt')
    results = lecture13.randomSplits(examples, lecture13.knn, 10, toPrint=False)
    assert len(results) == 4

def test_buildModel():
    examples = lecture13.buildTitanicExamples('TitanicPassengers.txt')
    trainingSet, testSet = lecture13.split80_20(examples)
    model = lecture13.buildModel(trainingSet, toPrint=False)
    assert isinstance(model, sklearn.linear_model.LogisticRegression)

def test_applyModel():
    examples = lecture13.buildTitanicExamples('TitanicPassengers.txt')
    trainingSet, testSet = lecture13.split80_20(examples)
    model = lecture13.buildModel(trainingSet, toPrint=False)
    results = lecture13.applyModel(model, testSet, 'Survived', 0.5)
    assert len(results) == 4

def test_lr():
    examples = lecture13.buildTitanicExamples('TitanicPassengers.txt')
    trainingSet, testSet = lecture13.split80_20(examples)
    results = lecture13.lr(trainingSet, testSet, 0.5)
    assert len(results) == 4

def test_buildROC():
    examples = lecture13.buildTitanicExamples('TitanicPassengers.txt')
    trainingSet, testSet = lecture13.split80_20(examples)
    auroc = lecture13.buildROC(trainingSet, testSet, 'ROC Test', plot=False)
    assert 0 <= auroc <= 1
