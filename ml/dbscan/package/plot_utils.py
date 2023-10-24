import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Handle the image saving path
module_path = Path(__file__).absolute()
data_path = module_path.parent.parent / "images"
if not os.path.exists(data_path):
    os.makedirs(data_path)


def plot_scatter(
    data,
    label,
    save=False,
    save_name="scatter_plot",
    figure_size=(4, 4),
    title="",
    point_size=2,
    edge_blank=0.5,
    *args,
    **kwargs,
):
    """
    Plots a scatter graph of the provided data.

    Args:
        data (numpy.ndarray): The data points to be plotted.
        label (numpy.ndarray): The labels for the data points.
        save (bool, optional): If True, saves the plot to a file. Otherwise, displays the plot. Defaults to False.
        save_name (str, optional): Name of the file where the plot will be saved. Defaults to "scatter_plot".
        figure_size (tuple, optional): Size of the displayed or saved figure. Defaults to (4, 4).
        title (str, optional): Title of the plot. Defaults to "".
        point_size (int, optional): Size of each data point in the scatter plot. Defaults to 2.
        edge_blank (float, optional): Gap between the data points and the plot edges. Defaults to 0.5.
    """
    plt.figure(figsize=figure_size)
    plt.xlim(np.min(data[:, 0]) - edge_blank, np.max(data[:, 0]) + edge_blank)
    plt.ylim(np.min(data[:, 1]) - edge_blank, np.max(data[:, 1]) + edge_blank)
    plt.scatter(data[:, 0], data[:, 1], c=label.squeeze(), s=point_size, *args, **kwargs)
    plt.title(title)
    if save:
        plt.savefig(f"{data_path}/{save_name}.png", dpi=600)
    else:
        plt.show()


def plot_scatter_center(
    data,
    center,
    label,
    save=False,
    save_name="scatter_plot",
    figure_size=(4, 4),
    title="",
    point_size=2,
    center_size=50,
    edge_blank=0.5,
    *args,
    **kwargs,
):
    """
    Plots a scatter graph of the provided data and centers.

    Args:
        data (numpy.ndarray): The data points to be plotted.
        center (numpy.ndarray): The center points to be plotted.
        label (numpy.ndarray): The labels for the data points.
        save (bool, optional): If True, saves the plot to a file. Otherwise, displays the plot. Defaults to False.
        save_name (str, optional): Name of the file where the plot will be saved. Defaults to "scatter_plot".
        figure_size (tuple, optional): Size of the displayed or saved figure. Defaults to (4, 4).
        title (str, optional): Title of the plot. Defaults to "".
        point_size (int, optional): Size of each data point in the scatter plot. Defaults to 2.
        center_size (int, optional): Size of the center points in the scatter plot. Defaults to 50.
        edge_blank (float, optional): Gap between the data points/centers and the plot edges. Defaults to 0.5.
    """
    plt.figure(figsize=figure_size)
    plt.xlim(np.min(data[:, 0]) - edge_blank, np.max(data[:, 0]) + edge_blank)
    plt.ylim(np.min(data[:, 1]) - edge_blank, np.max(data[:, 1]) + edge_blank)
    plt.scatter(data[:, 0], data[:, 1], c=label.squeeze(), s=point_size, *args, **kwargs)
    plt.scatter(
        center[:, 0],
        center[:, 1],
        edgecolors="red",
        facecolor="None",
        s=center_size,
        *args,
        **kwargs,
    )
    plt.title(title)
    if save:
        plt.savefig(f"{data_path}/{save_name}.png", dpi=600)
    else:
        plt.show()
