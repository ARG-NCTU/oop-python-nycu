from pyivp import XYPoint
import matplotlib.pyplot as plt

n_path = [
    XYPoint(0, 0), XYPoint(0, 5),
    XYPoint(0, 5), XYPoint(2, 0),
    XYPoint(2, 0), XYPoint(2, 5),
]

y_path = [
    XYPoint(3, 5), XYPoint(4, 3),
    XYPoint(5, 5), XYPoint(4, 3),
    XYPoint(4, 3), XYPoint(4, 0),
]
c_path = [
    XYPoint(6, 0), XYPoint(6, 5),
    XYPoint(6, 5), XYPoint(8, 5),
    XYPoint(8, 5), XYPoint(8, 4.5),
]

u_path = [
    XYPoint(9, 5), XYPoint(9, 1),
    XYPoint(9, 1), XYPoint(11, 1),
    XYPoint(11, 1), XYPoint(11, 5),
]

def plot_paths(*paths, labels=None):
    plt.figure(figsize=(8, 6))
    for idx, path in enumerate(paths):
        x = [p.x() for p in path]
        y = [p.y() for p in path]
        label = labels[idx] if labels else f"path {idx}"
        plt.plot(x, y, marker='o', label=label)
    plt.title("NYCU")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()
plot_paths(n_path, y_path, c_path, u_path, labels=["N", "Y", "C", "U"])

