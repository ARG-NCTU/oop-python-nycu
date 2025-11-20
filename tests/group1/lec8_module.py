import numpy as np
import random
import matplotlib.pyplot as plt

def make_hist(data, title, xlabel, ylabel, bins=20):
    """Create histogram using Matplotlib."""
    plt.hist(data, bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(alpha=0.3)
    plt.show()

def get_highs():
    """Read daily high temperatures (Celsius) from a CSV file."""
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
    """Return population and sample mean and std."""
    pop_mean = np.sum(population) / len(population)
    sample_mean = np.sum(sample) / len(sample)
    
    if verbose:
        make_hist(population,
                  'Daily High 1961-2015, Population\n'
                  + '(mean = '  + str(round(pop_mean, 2)) + ')',
                  'Degrees C', 'Number of Days')
        plt.figure()
        make_hist(sample,
                  'Daily High 1961-2015, Sample\n'
                  + '(mean = ' + str(round(sample_mean, 2)) + ')',
                  'Degrees C', 'Number of Days')   
        
        print('Population mean =', pop_mean)
        print('Population std  =', np.std(population))
        print('Sample mean     =', sample_mean)
        print('Sample std      =', np.std(sample))
    
    return (pop_mean,
            sample_mean,
            np.std(population),
            np.std(sample))

def get_random_sample(population, sample_size):
    """Randomly sample N items from the population."""
    return random.sample(population, sample_size)

def main():
    # Read full population data
    population = get_highs()
    print(f"Loaded {len(population)} temperature records.")

    # Decide sample size
    sample_size = 200
    sample = get_random_sample(population, sample_size)

    # Compute statistics
    pop_mean, sample_mean, pop_sd, sample_sd = get_means_and_sds(
        population, sample, verbose=True)

    print("\n=== RESULTS ===")
    print("Population Mean:", pop_mean)
    print("Sample Mean:", sample_mean)
    print("Population SD:", pop_sd)
    print("Sample SD:", sample_sd)

if __name__ == "__main__":
    main()
