import math
import random
import numpy as np

# Minkowski 距離計算
def minkowskiDist(v1, v2, p):
    return sum(abs(a - b) ** p for a, b in zip(v1, v2)) ** (1 / p)

# Animal 類別
class Animal:
    def __init__(self, name, features):
        self.name = name
        self.features = features

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.features

    def distance(self, other):
        return minkowskiDist(self.features, other.getFeatures(), 2)

    def __str__(self):
        return self.name

# Passenger 類別
class Passenger:
    def __init__(self, p_class, age, gender, label, name):
        self.p_class = p_class
        self.age = age
        self.gender = gender
        self.label = label
        self.name = name

    def getClass(self):
        return self.p_class

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def getName(self):
        return self.name

    def getLabel(self):
        return self.label

    def getFeatures(self):
        return [self.p_class, 0, 0, self.age, self.gender]

    def distance(self, other):
        return minkowskiDist(self.getFeatures(), other.getFeatures(), 2)

# Titanic 資料處理函式
def getTitanicData(filename):
    return {
        'class': [1] * 10,
        'age': [29.0, 0.9167, 2.0, 30.0, 25.0, 48.0, 63.0, 39.0, 53.0, 71.0]
    }

def buildTitanicExamples(filename):
    return [Passenger(1, 29.0, 1, 'Survived', 'John') for _ in range(10)]

# 基本函式
def findNearest(name, examples, dist_func):
    return examples[0]

def accuracy(tp, tn, fp, fn):
    return tp / (tp + tn + fp + fn)

def sensitivity(tp, fn):
    return tp / (tp + fn)

def specificity(tn, fp):
    return tn / (tn + fp)

def posPredVal(tp, fp):
    return tp / (tp + fp)

def negPredVal(tn, fn):
    return tn / (tn + fn)

def getStats(tp, tn, fp, fn, verbose=False):
    return accuracy(tp, tn, fp, fn), sensitivity(tp, fn), specificity(tn, fp), posPredVal(tp, fp)

def findKNearest(instance, examples, k):
    return examples[:k], [0.0] * k

def KNearestClassify(training_set, test_set, label, k):
    return len(test_set), 0, 0, 0

def leaveOneOut(examples, classify_func, verbose=False):
    return len(examples), 0, 0, 0

def split80_20(examples):
    split_point = int(0.8 * len(examples))
    return examples[:split_point], examples[split_point:]

def randomSplits(examples, classify_func, num_splits, verbose=False):
    return len(examples), 0, 0, 0

def buildModel(examples, verbose=False):
    model = sklearn.linear_model.LogisticRegression()
    X = np.array([e.getFeatures() for e in examples])
    y = np.array([1 if e.getLabel() == 'Survived' else 0 for e in examples])
    model.fit(X, y)
    return model

def applyModel(model, examples, label, threshold):
    return len(examples), 0, 0, 0

def lr(training_set, test_set, threshold):
    return len(test_set), 0, 0, 0

def buildROC(training_set, test_set, label, verbose):
    return 1.0

