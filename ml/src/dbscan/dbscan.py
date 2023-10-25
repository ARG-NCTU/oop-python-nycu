import package.plot_utils as plot_utils
from sklearn import cluster, metrics


class DBSCAN:
    """A wrapper class for the DBSCAN clustering algorithm, providing easy visualization and evaluation.

    Attributes:
        eps (float): The maximum distance between two samples for one to be considered as in the neighborhood of the other.
        min_samples (int): The number of samples in a neighborhood for a data point to be considered as a core point.
        cluster (DBSCAN object): Fitted DBSCAN cluster object.
        dataset (object): Dataset to be clustered.
    """
    def __init__(self, eps=0.5, min_samples=5):
        """
        Initializes the DBSCAN class with specified parameters.

        Args:
            eps (float, optional): The maximum distance between two samples for clustering. Defaults to 0.5.
            min_samples (int, optional): The number of samples in a neighborhood required for a data point to be considered as a core point. Defaults to 5.
        """
        self.eps = eps
        self.min_samples = min_samples
        self.cluster = None
        self.dataset = None

    def set_dataset(self, dataset):
        """
        Sets the dataset for clustering.

        Args:
            dataset (object): Dataset object containing data and labels.
        """
        self.dataset = dataset

    def fit(self, dataset=None):
        """
        Fits the DBSCAN clustering on the provided dataset.

        Args:
            dataset (object, optional): Dataset object to be clustered. If not provided, uses previously set dataset. Defaults to None.
        """
        if dataset is not None:
            self.set_dataset(dataset)
        self.cluster = cluster.DBSCAN(
            eps=self.eps, min_samples=self.min_samples
        ).fit(self.dataset.data)

    def evaluate(self):
        """
        Evaluates the clustering performance using Adjusted Mutual Information (AMI) score between true labels and predicted labels.

        Returns:
            float: AMI score.
        """
        return metrics.adjusted_mutual_info_score(
            self.dataset.label, self.cluster.labels_
        )

    def visualize(
        self,
        ground_truth=False,
        save=False,
        save_name=None,
        figure_size=(4, 4),
        point_size=10,
        edge_blank=1.0,
        **kwargs,
    ):
        """
        Visualizes the clustering results. If ground_truth is True, it also visualizes the true labels.

        Args:
            ground_truth (bool, optional): Whether to plot the true labels of the dataset. Defaults to False.
            save (bool, optional): Whether to save the generated plot. Defaults to False.
            save_name (str, optional): Name of the file to save the plot. If not provided, uses the name of the class. Defaults to None.
            figure_size (tuple, optional): Size of the generated figure. Defaults to (4, 4).
            point_size (int, optional): Size of each data point in the scatter plot. Defaults to 10.
            edge_blank (float, optional): Margin space around the data points. Defaults to 1.0.
        """
        prefix = "dbscan"
        if save_name is None:
            save_name = self.__class__.__name__.lower()
        save_name = f"{prefix}_{save_name}"
        
        plot_utils.plot_scatter(
            self.dataset.data,
            self.cluster.labels_,
            title=self.dataset.__class__.__name__ + " Cluster Result",
            edge_blank=edge_blank,
            save=save,
            save_name=save_name,
            figure_size=figure_size,
            point_size=point_size,
            **kwargs,
        )
        
        if ground_truth:
            plot_utils.plot_scatter(
                self.dataset.data,
                self.dataset.label,
                title=self.dataset.__class__.__name__ + " Ground Truth",
                edge_blank=edge_blank,
                save=save,
                save_name=save_name + "_ground_truth",
                figure_size=figure_size,
                point_size=point_size,
                **kwargs,
            )
