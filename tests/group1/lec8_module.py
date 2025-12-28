import numpy as np
import random
import matplotlib.pyplot as plt
from add_path import add_path
add_path()


def make_hist(data, title, xlabel, ylabel, bins=20):
    """Create and display histogram using Matplotlib.
    
    Args:
        data: List of numeric values to histogram
        title: Title for the histogram
        xlabel: Label for x-axis
        ylabel: Label for y-axis
        bins: Number of bins (default: 20)
    
    Raises:
        ValueError: If data is empty or bins <= 0
    """
    if not data:
        raise ValueError("data cannot be empty")
    if bins <= 0:
        raise ValueError(f"bins must be positive, got {bins}")
    
    plt.hist(data, bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(alpha=0.3)
    plt.show()

def get_highs():
    """Read daily high temperatures (Celsius) from 'temperatures.csv' file.
    
    File format: CSV with temperature value in second column
    Invalid lines are skipped.
    
    Returns:
        List of float temperature values (Celsius)
    
    Raises:
        FileNotFoundError: If temperatures.csv not found
    """
    try:
        with open('temperatures.csv') as inFile:
            population = []
            for l in inFile:
                try:
                    tempC = float(l.split(',')[1])
                    population.append(tempC)
                except (ValueError, IndexError):
                    # Skip lines that can't be parsed
                    continue
            return population
    except FileNotFoundError:
        raise FileNotFoundError("temperatures.csv not found in current directory")

def get_means_and_sds(population, sample, verbose=False):
    """Calculate and optionally display population and sample statistics.
    
    Args:
        population: Full population list of numeric values
        sample: Sample list of numeric values
        verbose: If True, display histograms and statistics (default: False)
    
    Returns:
        Tuple (pop_mean, sample_mean, pop_sd, sample_sd)
    
    Raises:
        ValueError: If population or sample is empty
    """
    if not population or not sample:
        raise ValueError("population and sample must be non-empty")
    
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
    """Randomly sample N items from the population.
    
    Args:
        population: List to sample from
        sample_size: Number of items to sample (int > 0)
    
    Returns:
        Random sample of specified size (without replacement)
    
    Raises:
        ValueError: If sample_size > population size or sample_size <= 0
    """
    if sample_size <= 0:
        raise ValueError(f"sample_size must be positive, got {sample_size}")
    if sample_size > len(population):
        raise ValueError(f"sample_size ({sample_size}) cannot exceed population size ({len(population)})")
    
    return random.sample(population, sample_size)

def main():
    """Main program to demonstrate sampling statistics."""
    try:
        # Read full population data
        population = get_highs()
        if not population:
            print("ERROR: No temperature data loaded from temperatures.csv")
            return
        
        print(f"Loaded {len(population)} temperature records.")

        # Decide sample size
        sample_size = 200
        if sample_size > len(population):
            sample_size = len(population) // 2
            print(f"Sample size adjusted to {sample_size}")
        
        sample = get_random_sample(population, sample_size)

        # Compute statistics
        pop_mean, sample_mean, pop_sd, sample_sd = get_means_and_sds(
            population, sample, verbose=True)

        print("\n=== RESULTS ===")
        print(f"Population Mean: {pop_mean:.4f}")
        print(f"Sample Mean:     {sample_mean:.4f}")
        print(f"Population SD:   {pop_sd:.4f}")
        print(f"Sample SD:       {sample_sd:.4f}")
        print(f"Mean Difference: {abs(pop_mean - sample_mean):.4f}")
        
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
    except ValueError as e:
        print(f"ERROR: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
