import numpy as np
import matplotlib.pyplot as plt
from tests.group8.hazel_113511170.Lab07.pyivp import *

# Function to plot the letters, returning the x and y coordinates for each letter.
def plot_letter(letter):
    if letter == "N":
        # Coordinates for letter N: two straight lines forming N
        x = [0, 0, 1, 1]
        y = [0, 1, 0, 1]
    elif letter == "Y":
        # Coordinates for letter Y: two lines forming Y
        x = [0, 0.5, 1]
        y = [1, 0.5, 1]
    elif letter == "C":
        # Coordinates for letter C: an arc
        theta = np.linspace(np.pi, 2 * np.pi, 100)
        x = np.cos(theta)
        y = np.sin(theta)
    elif letter == "U":
        # Coordinates for letter U: a rectangle with a rounded bottom
        x = [0, 0, 1, 1]
        y = [0, 1, 1, 0]
    
    return x, y

# Plotting the letters "NYCU"
fig, ax = plt.subplots()
for i, letter in enumerate("NYCU"):
    x, y = plot_letter(letter)
    ax.plot([xi + i * 2 for xi in x], y, label=letter)  # Shift each letter to the right

# Customize the plot
ax.set_aspect('equal', 'box')
ax.set_title("Drawing 'NYCU' with PyIVP")
ax.legend()
plt.show()
