import numpy as np
import matplotlib.pyplot as plt

# Define a function to plot the letters
def plot_letter(letter):
    if letter == "N":
        # Coordinates for letter N
        x = [0, 0, 1, 1]
        y = [0, 1, 0, 1]
    elif letter == "Y":
        # Coordinates for letter Y
        x = [0, 0.5, 0.5,0.5,1]
        y = [1, 0.5, 0, 0.5,1]
    elif letter == "C":
        # Coordinates for letter C
        theta = np.linspace(np.pi, 2 * np.pi, 100)
        x = np.sin(theta)
        y = np.cos(theta)
    elif letter == "U":
        # Coordinates for letter U
        x = [0, 0, 1, 1]
        y = [0, -1, -1, 0]
    
    return x, y

# Plot the letters
fig, ax = plt.subplots()
for i, letter in enumerate("NYCU"):
    x, y = plot_letter(letter)
    ax.plot([xi + i * 2 for xi in x], [yi for yi in y], label=letter)  # Shift each letter to the right

# Customize plot
ax.set_aspect('equal', 'box')
ax.set_title("Drawing 'NYCU' with PyIVP")
ax.legend()
plt.show()
