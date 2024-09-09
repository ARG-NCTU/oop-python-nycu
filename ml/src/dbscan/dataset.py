from abc import ABC, abstractmethod

import dbscan.plot_utils as plot_utils
import numpy as np
from sklearn import datasets


class Dataset(ABC):
    """
    Abstract base class for datasets.

    Attributes:
        data (numpy.ndarray): The data points.
        label (numpy.ndarray): Labels corresponding to the data points.
        parameters (dict): Parameters related to the dataset.
        seed (int): Seed for random operations to ensure reproducibility.
    """

    def __init__(self, seed=0):
        """
        Initializes the Dataset object.

        Args:
            seed (int, optional): Seed for random operations. Defaults to 0.
        """
        self.data = None
        self.label = None
        self.parameters = {}
        self.seed = seed
        np.random.seed(self.seed)

    @abstractmethod
    def generate_data(self, **kwargs):
        """
        Abstract method to generate data. Implementation should be provided in derived classes.
        """
        pass

    def visualize(
        self,
        save=False,
        save_name=None,
        figure_size=(4, 4),
        point_size=2,
        edge_blank=0.5,
        **kwargs,
    ):
        """
        Visualizes the data points using a scatter plot.

        Args:
            save (bool, optional): Whether to save the generated plot. Defaults to False.
            save_name (str, optional): Name of the file to save the plot. If not provided, uses the name of the class. Defaults to None.
            figure_size (tuple, optional): Size of the generated figure. Defaults to (4, 4).
            point_size (int, optional): Size of each data point in the scatter plot. Defaults to 2.
            edge_blank (float, optional): Margin space around the data points. Defaults to 0.5.

        Returns:
            None
        """
        prefix = "dataset"
        if save_name is None:
            save_name = self.__class__.__name__.lower()
        save_name = f"{prefix}_{save_name}"
        plot_utils.plot_scatter(
            self.data,
            self.label,
            save=save,
            save_name=save_name,
            figure_size=figure_size,
            title=self.__class__.__name__,
            point_size=point_size,
            edge_blank=edge_blank,
            **kwargs,
        )

    def set_parameters(self, **kwargs):
        """_summary_
        """
        self.parameters.update(kwargs)

    def get_parameters(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.parameters


class GaussianMixture(Dataset):
    """
    Gaussian Mixture dataset, derived from the Dataset abstract base class.
    """

    def generate_data(
        self, num_samples=1000, num_classes=2, noise=0.05, **kwargs
    ):
        """
        Generates data based on a Gaussian mixture model.

        Args:
            num_samples (int, optional): Total number of samples to generate. Defaults to 1000.
            num_classes (int, optional): Number of Gaussian mixtures (or clusters). Defaults to 2.
            noise (float, optional): Standard deviation of the clusters. Defaults to 0.05.
        """
        self.set_parameters(
            num_samples=num_samples,
            num_classes=num_classes,
            noise=noise,
            **kwargs,
        )

        self.data, self.label, self.centers = datasets.make_blobs(
            n_samples=num_samples,
            n_features=2,
            centers=num_classes,
            cluster_std=noise,
            random_state=self.seed,
            return_centers=True,
        )

    def visualize(
        self,
        center=False,
        save=False,
        save_name=None,
        figure_size=(4, 4),
        point_size=2,
        center_size=50,
        edge_blank=1.0,
        **kwargs,
    ):
        """
        Visualizes the Gaussian Mixture data points. Optionally plots the centers.

        Args:
            center (bool, optional): Whether to plot the centers of the Gaussian clusters. Defaults to False.
            save (bool, optional): Whether to save the generated plot. Defaults to False.
            save_name (str, optional): Name of the file to save the plot. If not provided, uses the name of the class. Defaults to None.
            figure_size (tuple, optional): Size of the generated figure. Defaults to (4, 4).
            point_size (int, optional): Size of each data point in the scatter plot. Defaults to 2.
            center_size (int, optional): Size of the center points in the scatter plot. Defaults to 50.
            edge_blank (float, optional): Margin space around the data points. Defaults to 1.0.

        Returns:
            None
        """
        if center:
            prefix = "dataset"
            if save_name is None:
                save_name = self.__class__.__name__.lower()
            save_name = f"{prefix}_{save_name}"

            plot_utils.plot_scatter_center(
                self.data,
                self.centers,
                self.label,
                save=save,
                save_name=save_name,
                figure_size=figure_size,
                title=self.__class__.__name__,
                point_size=point_size,
                center_size=center_size,
                edge_blank=edge_blank,
                **kwargs,
            )
        else:
            super().visualize(
                save=save,
                save_name=save_name,
                figure_size=figure_size,
                point_size=point_size,
                edge_blank=edge_blank,
                **kwargs,
            )


class TwoMoon(Dataset):
    """
    Two Moon dataset, derived from the Dataset abstract base class.
    """
    def generate_data(self, num_samples=1000, noise=0.05, **kwargs):
        """
        Generates data based on the two moon shapes.

        Args:
            num_samples (int, optional): Total number of samples to generate. Defaults to 1000.
            noise (float, optional): Amount of noise to add to the moon shapes. Defaults to 0.05.
        """
        self.set_parameters(num_samples=num_samples, noise=noise, **kwargs)

        self.data, self.label = datasets.make_moons(
            n_samples=num_samples, noise=noise, random_state=self.seed
        )


class ConcentricCircle(Dataset):
    """
    Concentric Circle dataset, derived from the Dataset abstract base class.
    """
    def generate_data(
        self,
        num_samples=1000,
        num_classes=2,
        radius_m=1,
        radius_b=0.5,
        noise=0.05,
        **kwargs,
    ):
        """
        Generates data based on concentric circle shapes.

        Args:
            num_samples (int, optional): Total number of samples to generate per class. Defaults to 1000.
            num_classes (int, optional): Number of concentric circles. Defaults to 2.
            radius_m (int, optional): Multiplier for the radius of each concentric circle. Defaults to 1.
            radius_b (float, optional): Base radius for the innermost circle. Defaults to 0.5.
            noise (float, optional): Amount of noise to add to the circles. Defaults to 0.05.
        """
        self.set_parameters(
            num_samples=num_samples,
            num_classes=num_classes,
            radius_m=radius_m,
            radius_b=radius_b,
            noise=noise,
            **kwargs,
        )

        data_list = []
        label_list = []

        for i in range(num_classes):
            radius = radius_m * i + radius_b
            theta = np.linspace(0, 2 * np.pi, num_samples, endpoint=False)
            x = radius * np.cos(theta) + np.random.normal(0, noise, num_samples)
            y = radius * np.sin(theta) + np.random.normal(0, noise, num_samples)
            data_list.append(np.column_stack([x, y]))
            label_list.extend([i] * num_samples)

        self.data = np.vstack(data_list)
        self.label = np.array(label_list)
