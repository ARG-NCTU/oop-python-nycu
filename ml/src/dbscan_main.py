from package.dataset import ConcentricCircle, GaussianMixture, TwoMoon

from package.dbscan import DBSCAN

###
# Gaussian Mixture
###
gaussian_mixture = GaussianMixture(seed=0)
gaussian_mixture.generate_data(num_samples=5000, num_classes=4, noise=0.5)
print(gaussian_mixture.get_parameters())
gaussian_mixture.visualize(
    save=True,
    center=True,
    save_name="gaussian_mixture",
    figure_size=(4, 4),
    point_size=2,
    center_size=50,
    edge_blank=0.5,
)

dbscan_cluster = DBSCAN(eps=0.6, min_samples=90)
dbscan_cluster.set_dataset(gaussian_mixture)
dbscan_cluster.fit()
dbscan_cluster.visualize(
    ground_truth=False,
    save=True,
    save_name="gaussian_mixture",
    figure_size=(4, 4),
    point_size=2,
    edge_blank=0.5,
)
print("Adjusted Mutual Information Score: {:.3f}\n\n".format(dbscan_cluster.evaluate()))

###
# Two Moon
###
two_moon = TwoMoon(seed=0)
two_moon.generate_data(num_samples=5000, noise=0.1)
print(two_moon.get_parameters())
two_moon.visualize(
    save=True,
    save_name="two_moon",
    figure_size=(4, 4),
    point_size=2,
    edge_blank=0.5,
)

dbscan_cluster = DBSCAN(eps=0.2, min_samples=120)
dbscan_cluster.set_dataset(two_moon)
dbscan_cluster.fit()
dbscan_cluster.visualize(
    ground_truth=False,
    save=True,
    save_name="two_moon",
    figure_size=(4, 4),
    point_size=2,
    edge_blank=0.5,
)
print("Adjusted Mutual Information Score: {:.3f}\n\n".format(dbscan_cluster.evaluate()))

###
# Concentric Circle
###
concentric_circle = ConcentricCircle(seed=0)
concentric_circle.generate_data(num_samples=5000, noise=0.1)
print(concentric_circle.get_parameters())
concentric_circle.visualize(
    save=True,
    save_name="concentric_circle",
    figure_size=(4, 4),
    point_size=2,
    edge_blank=0.5,
)

dbscan_cluster = DBSCAN(eps=0.2, min_samples=120)
dbscan_cluster.set_dataset(concentric_circle)
dbscan_cluster.fit()
dbscan_cluster.visualize(
    ground_truth=False,
    save=True,
    save_name="concentric_circle",
    figure_size=(4, 4),
    point_size=2,
    edge_blank=0.5,
)


print("Adjusted Mutual Information Score: {:.3f}\n\n".format(dbscan_cluster.evaluate()))
