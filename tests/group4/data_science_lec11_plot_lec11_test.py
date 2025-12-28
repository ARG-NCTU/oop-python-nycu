# import sys, os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/mit_ocw_data_science/lec11")))

# import add_path
# import numpy as np
# import matplotlib
# matplotlib.use("Agg") 

# import matplotlib.pyplot as plt
# from plot_lec11 import compareAnimals
# from lec11_module import Animal
# import plot_lec11

# import warnings
# warnings.filterwarnings("ignore", category=UserWarning, message=".*non-GUI backend.*")

# def test_compareAnimals(monkeypatch):
#     animal1 = Animal("Dog", [10, 20, 30])
#     animal2 = Animal("Cat", [1, 2, 3])
#     animal3 = Animal("Mouse", [5, 15, 25])
#     animals = [animal1, animal2, animal3]

#     plt.close("all")  

#     monkeypatch.setattr(plot_lec11.plt, "show", lambda: None)

#     compareAnimals(animals, precision=2)

#     assert len(plt.get_fignums()) > 0

#     fig = plt.gcf()
#     has_table = any(isinstance(child, matplotlib.table.Table) for child in fig.axes[0].get_children())
#     assert has_table
