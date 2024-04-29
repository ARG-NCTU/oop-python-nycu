import unittest
import matplotlib.pyplot as plt
import numpy as np

class TestPlot(unittest.TestCase):
    def test_plot(self):
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        self.assertTrue(isinstance(ax, plt.Axes))

if __name__ == '__main__':
    unittest.main()

x_vals = [1, 2, 3, 4]
y_vals_1 = [1, 2, 3, 4]
plt.plot(x_vals, y_vals_1, 'b-', label='first')
y_vals_2 = [1, 7, 3, 5]
plt.plot(x_vals, y_vals_2, 'r--', label='second')
plt.legend()
plt.show()
