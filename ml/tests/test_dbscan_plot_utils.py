import numpy as np
import pytest
from dbscan.plot_utils import plot_scatter, plot_scatter_center

# Sample data for testing
data = np.array([[1, 2], [3, 4], [5, 6]])
center = np.array([[1, 2], [5, 6]])
label = np.array([0, 1, 0])

# Tests for plot_scatter
def test_plot_scatter():
    plot_scatter(data, label, save=True, save_name="test_plot_scatter")

# Tests for plot_scatter_center
def test_plot_scatter_center():
    plot_scatter_center(data, center, label, save=True, save_name="test_plot_scatter_center")
