import pytest
import numpy as np
import random
import matplotlib.pyplot as plt


def make_hist(data, title, xlabel, ylabel, bins=20):
    # Create histogram of data using Matplotlib
    plt.hist(data, bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def get_highs():
    with open('temperatures.csv') as inFile:
        population = []
        for l in inFile:
            try:
                tempC = float(l.split(',')[1])
                population.append(tempC)
            except:
                continue
        return population

def get_means_and_sds(population, sample, verbose=False):
    pop_mean = np.sum(population) / len(population)
    sample_mean = np.sum(sample) / len(sample)
    if verbose:
        make_hist(population,
                  'Daily High 1961-2015, Population\n' +\
                  '(mean = '  + str(round(pop_mean, 2)) + ')',
                  'Degrees C', 'Number Days')
        plt.figure()
        make_hist(sample, 'Daily High 1961-2015, Sample\n' +\
                  '(mean = ' + str(round(sample_mean, 2)) + ')',
                  'Degrees C', 'Number Days')   
        print('Population mean =', pop_mean)
        print('Standard deviation of population =',
              np.std(population))
        print('Sample mean =', sample_mean)
        print('Standard deviation of sample =',
              np.std(sample))
    return pop_mean, sample_mean,\
           np.std(population), np.std(sample)

@pytest.fixture
def sample_data():
    # Generate some sample data for testing
    random.seed(0)
    population = get_highs() 
    sample = random.sample(population, 100)
    return population, sample

def test_get_highs():
    # Test that get_highs returns the expected list of values
    population = get_highs()
    expected = [3.1, 0.55, 0.0] 
    assert population[0:3] == expected

def test_get_means_and_sds(sample_data):
    # Test that get_means_and_sds returns the expected values
    population, sample = sample_data
    pop_mean, sample_mean, pop_sd, sample_sd = \
        get_means_and_sds(population, sample)
    expected_pop_mean = np.mean(population)
    expected_sample_mean = np.mean(sample)
    expected_pop_sd = np.std(population)
    expected_sample_sd = np.std(sample)
    assert pop_mean == expected_pop_mean
    assert sample_mean == expected_sample_mean
    assert pop_sd == expected_pop_sd
    assert sample_sd == expected_sample_sd

