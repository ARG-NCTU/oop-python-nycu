import numpy as np
import random, pytest
import matplotlib.pyplot as plt

def make_hist(data, title, xlabel, ylabel, bins=20):
    plt.hist(data, bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # plt.show() # Removed plt.show() for automated testing

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
    pop_std = np.std(population)
    sample_std = np.std(sample, ddof=1) # Calculate sample standard deviation
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
        print('Standard deviation of population =', pop_std)
        print('Sample mean =', sample_mean)
        print('Standard deviation of sample =', sample_std)
    return pop_mean, sample_mean, pop_std, sample_std


# Set line width
plt.rcParams['lines.linewidth'] = 4
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16
plt.rcParams['xtick.major.size'] = 7
plt.rcParams['ytick.major.size'] = 7
plt.rcParams['lines.markersize'] = 10
plt.rcParams['legend.numpoints'] = 1


population = get_highs()
sample = random.sample(population, 100)
pop_mean, sample_mean, pop_sd, sample_sd = \
    get_means_and_sds(population, sample, True)


def test_make_hist():
    data = [1, 2, 3, 4, 5]
    title = "Test Histogram"
    xlabel = "X-axis"
    ylabel = "Y-axis"
    bins = 5
    make_hist(data, title, xlabel, ylabel, bins)
    # To avoid plt.show() blocking tests, we simply call the function.
    # For more rigorous testing of plots, you'd typically save the plot
    # and then analyze the saved file or use libraries designed for
    # testing visualizations.

def test_get_highs():
    population = get_highs()
    assert len(population) > 0
    assert all(isinstance(temp, float) for temp in population)
    assert all(-50 <= temp <= 50 for temp in population)

def test_get_means_and_sds():
    population = [1, 2, 3, 4, 5]
    sample = [1, 2, 3]
    pop_mean, sample_mean, pop_sd, sample_sd = get_means_and_sds(population, sample)
    assert pop_mean == 3.0
    assert sample_mean == 2.0
    assert pop_sd == pytest.approx(np.std(population))
    assert sample_sd == pytest.approx(np.std(sample, ddof=1)) # Use ddof=1

def test_get_means_and_sds_verbose():
    population = [1, 2, 3, 4, 5]
    sample = [1, 2, 3]
    pop_mean, sample_mean, pop_sd, sample_sd = get_means_and_sds(population, sample, verbose=True)
    assert pop_mean == 3.0
    assert sample_mean == 2.0
    assert pop_sd == pytest.approx(np.std(population))
    assert sample_sd == pytest.approx(np.std(sample, ddof=1)) # Use ddof=1

# Run the tests using pytest from the terminal (recommended for proper test execution)
if __name__ == "__main__":
    test_make_hist()
    test_get_highs()
    test_get_means_and_sds()
    test_get_means_and_sds_verbose()
    print("All tests passed!")