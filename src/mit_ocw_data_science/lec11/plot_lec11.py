import matplotlib.pyplot as plt
import random
#import pylab

from lec11_module import *
#from test_hypothesis import *

#set line width
# replace pylab with plt
plt.rcParams['lines.linewidth'] = 4
#set font size for titles
plt.rcParams['axes.titlesize'] = 18
#set font size for labels on axes
plt.rcParams['axes.labelsize'] = 18
#set size of numbers on x-axis
plt.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
plt.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
plt.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
plt.rcParams['ytick.major.size'] = 7
#set size of markers
plt.rcParams['lines.markersize'] = 10

# pylab.rcParams['lines.linewidth'] = 4
# #set font size for titles 
# pylab.rcParams['axes.titlesize'] = 18
# #set font size for labels on axes
# pylab.rcParams['axes.labelsize'] = 18
# #set size of numbers on x-axis
# pylab.rcParams['xtick.labelsize'] = 16
# #set size of numbers on y-axis
# pylab.rcParams['ytick.labelsize'] = 16
# #set size of ticks on x-axis
# pylab.rcParams['xtick.major.size'] = 7
# #set size of ticks on y-axis
# pylab.rcParams['ytick.major.size'] = 7
# #set size of markers
# pylab.rcParams['lines.markersize'] = 10

def compareAnimals(animals, precision):
    """Assumes animals is a list of animals, precision an int >= 0
       Builds a table of Euclidean distance between each animal"""
    #Get labels for columns and rows
    columnLabels = []
    for a in animals:
        columnLabels.append(a.getName())
    rowLabels = columnLabels[:]
    tableVals = []
    #Get distances between pairs of animals
    #For each row
    for a1 in animals:
        row = []
        #For each column
        for a2 in animals:
            if a1 == a2:
                row.append('--')
            else:
                distance = a1.distance(a2)
                row.append(str(round(distance, precision)))
        tableVals.append(row)
    #Produce table
    table = plt.table(rowLabels = rowLabels,
                        colLabels = columnLabels,
                        cellText = tableVals,
                        cellLoc = 'center',
                        loc = 'center',
                        colWidths = [0.2]*len(animals))
    table.scale(1, 2.5)
    plt.title('Eucliedan Distance Between Animals')

rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
boa = Animal('boa\nconstrictor', [0,1,0,1,0])
dartFrog = Animal('dart frog', [1,0,1,0,4])
animals = [rattlesnake, boa, dartFrog]
compareAnimals(animals, 3)
plt.show()

#
#alligator = Animal('alligator', [1,1,0,1,4])
#animals.append(alligator)
#compareAnimals(animals, 3)

#rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
#boa = Animal('boa\nconstrictor', [0,1,0,1,0])
#dartFrog = Animal('dart frog', [1,0,1,0,1])
#alligator = Animal('alligator', [1,1,0,1,1])
#animals = [rattlesnake, boa, dartFrog, alligator]
#compareAnimals(animals, 3)
