import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import add_path
import numpy as np
from src.mit_ocw_data_science.lec8.lec8_module import make_hist, get_highs, get_means_and_sds

def test_make_hist():
    data = np.random.normal(loc=0.0, scale=1.0, size=1000)
    try:
        make_hist(data, 'Test Histogram', 'Value', 'Frequency', bins=30)
    except Exception as e:
        assert False, f"make_hist raised an exception: {e}"


"""
def test_get_highs():
    population = get_highs()
    assert isinstance(population, list), "get_highs should return a list"
    assert all(isinstance(temp, float) for temp in population), "All elements in the population should be floats"
    assert len(population) > 0, "Population should not be empty"
"""
"""
def test_get_means_and_sds():
    population = get_highs()
    sample = np.random.choice(population, size=100, replace=False).tolist()
    pop_mean, sample_mean, pop_sd, sample_sd = get_means_and_sds(population, sample, verbose=False)
    
    assert isinstance(pop_mean, float), "Population mean should be a float"
    assert isinstance(sample_mean, float), "Sample mean should be a float"
    assert isinstance(pop_sd, float), "Population standard deviation should be a float"
    assert isinstance(sample_sd, float), "Sample standard deviation should be a float"
    
    assert pop_mean != sample_mean or pop_sd != sample_sd, "Population and sample statistics should differ"

"""