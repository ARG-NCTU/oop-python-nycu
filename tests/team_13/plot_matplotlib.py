import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return x ** 2 + (y - np.cbrt(x**2)) ** 2


x = np.linspace(-10, 11, 100)
y = np.linspace(-10, 11, 100)
x, y = np.meshgrid(x, y)
z = f(x, y+1)
plt.contour(x, y, z, levels=13)
plt.gca().xaxis.set_label_position('top') 
plt.xlabel("13 hearts", fontsize=40)
plt.show()
