import random
import matplotlib.pyplot as plt
import numpy

import cluster

import pytest

@pytest.fixture(scope="module")
def patients():
    """提供給 pytest 使用的 patients fixture"""
    print("\n正在載入心臟病患資料（pytest fixture）...")
    return getData(toScale=False)

class Patient(cluster.Example):
    pass

def scaleAttrs(vals):
    vals = numpy.array(vals)
    mean = sum(vals)/len(vals)
    sd = numpy.std(vals)
    vals = vals - mean
    return vals/sd

import os

def getData(toScale=False):
    # 萬能找檔案法：不管你在哪裡執行，都能找到 cardiacData.txt
    possible_paths = [
        'cardiacData.txt',                                          # 正常情況
        'data_science/lecture12/cardiacData.txt',                   # 你自己跑的時候
        'tests/group7/test_111514025/data_science/lecture12/cardiacData.txt',  # 助教測資路徑
        os.path.join(os.path.dirname(__file__), 'cardiacData.txt'), # 相對於.py檔
    ]
    
    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = path
            break
    
    if file_path is None:
        print("錯誤：找不到 cardiacData.txt")
        print("我試過這些路徑都找不到：")
        for p in possible_paths:
            print("  ", p, "→", os.path.exists(p))
        print("目前工作目錄：", os.getcwd())
        raise FileNotFoundError("cardiacData.txt 不見了！")
    
    print(f"找到資料檔：{file_path}")
    
    hrList, stElevList, ageList, prevACSList, classList = [], [], [], [], []
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip() == '':
                continue
            vals = line.strip().split(',')
            hrList.append(int(vals[0]))
            stElevList.append(int(vals[1]))
            ageList.append(int(vals[2]))
            prevACSList.append(int(vals[3]))
            classList.append(int(vals[4]))
    
    # 後面不變
    points = []
    for i in range(len(hrList)):
        features = numpy.array([hrList[i], prevACSList[i], stElevList[i], ageList[i]])
        points.append(Patient('P'+str(i), features, classList[i]))
    
    print(f"成功載入 {len(points)} 筆資料")
    return points
    
def kmeans(examples, k, verbose = False):
    #Get k randomly chosen initial centroids, create cluster for each
    initialCentroids = random.sample(examples, k)
    clusters = []
    for e in initialCentroids:
        clusters.append(cluster.Cluster([e]))
        
    #Iterate until centroids do not change
    converged = False
    numIterations = 0
    while not converged:
        numIterations += 1
        #Create a list containing k distinct empty lists
        newClusters = []
        for i in range(k):
            newClusters.append([])
            
        #Associate each example with closest centroid
        for e in examples:
            #Find the centroid closest to e
            smallestDistance = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            #Add e to the list of examples for appropriate cluster
            newClusters[index].append(e)
            
        for c in newClusters: #Avoid having empty clusters
            if len(c) == 0:
                raise ValueError('Empty Cluster')
        
        #Update each cluster; check if a centroid has changed
        converged = True
        for i in range(k):
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False
        if verbose:
            print('Iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print('') #add blank line
    return clusters

def trykmeans(examples, numClusters, numTrials, verbose = False):
    """Calls kmeans numTrials times and returns the result with the
          lowest dissimilarity"""
    best = kmeans(examples, numClusters, verbose)
    minDissimilarity = cluster.dissimilarity(best)
    trial = 1
    while trial < numTrials:
        try:
            clusters = kmeans(examples, numClusters, verbose)
        except ValueError:
            continue #If failed, try again
        currDissimilarity = cluster.dissimilarity(clusters)
        if currDissimilarity < minDissimilarity:
            best = clusters
            minDissimilarity = currDissimilarity
        trial += 1
    return best

def printClustering(clustering):
    """Assumes: clustering is a sequence of clusters
       Prints information about each cluster
       Returns list of fraction of pos cases in each cluster"""
    posFracs = []
    for c in clustering:
        numPts = 0
        numPos = 0
        for p in c.members():
            numPts += 1
            if p.getLabel() == 1:
                numPos += 1
        fracPos = numPos/numPts
        posFracs.append(fracPos)
        print('Cluster of size', numPts, 'with fraction of positives =',
              round(fracPos, 4))
    return numpy.array(posFracs)

def testClustering(patients, numClusters, seed = 0, numTrials = 5):
    random.seed(seed)
    bestClustering = trykmeans(patients, numClusters, numTrials)
    posFracs = printClustering(bestClustering)
    return posFracs

patients = getData()
for k in (2,):
    print('Test k-means (k = ' + str(k) + ')')
    posFracs = testClustering(patients, k, 2)

#numPos = 0
#for p in patients:
#    if p.getLabel() == 1:
#        numPos += 1
#print('Total number of positive patients =', numPos)
