import matplotlib.pyplot as plt  # type: ignore
import numpy as np

from typing import List
from dataclasses import dataclass

#import pylab

#set line width
plt.rcParams['lines.linewidth'] = 6
#set general font size 
plt.rcParams['font.size'] = 12
#set font size for labels on axes
plt.rcParams['axes.labelsize'] = 18
#set size of numbers on x-axis
plt.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
plt.rcParams['ytick.major.size'] = 5
#set size of markers
plt.rcParams['lines.markersize'] = 10

def minkowski_dist(v1: List[float], v2: List[float], p: float) -> float:
    #Assumes v1 and v2 are equal length arrays of numbers
    # Add doctest for the function
    """
    >>> minkowski_dist([0,0], [3,4], 2)
    5.0
    >>> minkowski_dist([1,2,3], [4,5,6], 1)
    9.0
    """
    dist = 0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)


@dataclass
class Sample:
    """
    Add doctest for the class
    >>> Sample('test', [1,2,3], 'test')
    Sample(name='test', features=[1, 2, 3], label='test')
    """
    name: str
    features: List[float]
    label: str

class Example(object):
    """
    Add doctest for the class
    >>> print(Example('test', [1,2,3], 'test'))
    test:[1, 2, 3]:test
    """
    def __init__(self, name, features, label = None):
        #Assumes features is an array of floats
        self.name = name
        self.features = features
        self.label = label
        
    def dimensionality(self):
        return len(self.features)
    
    def getFeatures(self):
        return self.features[:]
    
    def getLabel(self):
        return self.label
    
    def getName(self):
        return self.name
    
    def distance(self, other):
        return minkowski_dist(self.features, other.getFeatures(), 2)
    
    def __str__(self):
        return self.name +':'+ str(self.features) + ':'\
               + str(self.label)


@dataclass
class Cluster1:
    examples: List[Example]
    centroid: Example


class Cluster(object):
    """
    Add doctest for the class
    >>> print(Cluster([Example('test', [1,2,3], 'test')]))
    Cluster with centroid [1. 2. 3.] contains:
      test
    """
    def __init__(self, examples):
        """Assumes examples a non-empty list of Examples"""
        self.examples = examples
        self.centroid = self.computeCentroid()
        
    def update(self, examples):
        """Assume examples is a non-empty list of Examples
           Replace examples; return amount centroid has changed"""
        oldCentroid = self.centroid
        self.examples = examples
        self.centroid = self.computeCentroid()
        return oldCentroid.distance(self.centroid)
    
    def computeCentroid(self):
        vals = np.array([0.0]*self.examples[0].dimensionality())
        for e in self.examples: #compute mean
            vals += e.getFeatures()
        centroid = Example('centroid', vals/len(self.examples))
        return centroid

    def getCentroid(self):
        return self.centroid

    def variability(self):
        totDist = 0
        for e in self.examples:
            totDist += (e.distance(self.centroid))**2
        return totDist
        
    def members(self):
        for e in self.examples:
            yield e

    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.getName())
        names.sort()
        result = 'Cluster with centroid '\
               + str(self.centroid.getFeatures()) + ' contains:\n  '
        for e in names:
            result = result + e + ', '
        return result[:-2] #remove trailing comma and space    
        
def dissimilarity(clusters):
    """Assumes clusters a list of clusters
       Returns a measure of the total dissimilarity of the
       clusters in the list"""
    totDist = 0
    for c in clusters:
        totDist += c.variability()
    return totDist

