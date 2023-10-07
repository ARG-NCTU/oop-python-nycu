import matplotlib.pyplot as plt
import time

from lec11_complexity_part2 import genSubsets
testSet = []
for i in range(20):
    testSet.append(i)

n_values = []
times = []

for n in range(1, len(testSet)+1):
    start_time = time.time()
    genSubsets(testSet[:n])
    end_time = time.time()
    n_values.append(n)
    times.append(end_time - start_time)

plt.plot(n_values, times)
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Time Complexity of genSubsets')
plt.savefig('complexity of exponential.png')