import numpy as np
import random
import matplotlib.pyplot as plt
import os

# NOTE: Commented out local dependency to ensure script runs standalone.
# from add_path import add_path
# add_path()

# ==============================================================================
# Helper: Generate Dummy Data (If CSV is missing)
# ==============================================================================
def create_dummy_csv(filename='temperatures.csv'):
    """Generates a synthetic temperature dataset if file is missing."""
    print(f"⚠️ '{filename}' not found. Generating synthetic data...")
    # Generate 10 years of daily temps with seasonal variation + noise
    days = np.arange(365 * 10)
    temps = 20 + 10 * np.sin(2 * np.pi * days / 365) + np.random.normal(0, 3, len(days))
    
    with open(filename, 'w') as f:
        f.write("Date,Temperature\n")
        for i, t in enumerate(temps):
            f.write(f"Day{i},{t:.1f}\n")
    print("✅ Dummy data created.\n")

# ==============================================================================
# Plotting
# ==============================================================================
def plot_comparison(population, sample, pop_mean, sample_mean):
    """
    Plots Population vs Sample histograms side-by-side.
    """
    plt.style.use('ggplot') # Use a nicer plotting style
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Plot 1: Population
    ax1.hist(population, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    ax1.axvline(pop_mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {pop_mean:.1f}')
    ax1.set_title(f'Population (N={len(population)})')
    ax1.set_xlabel('Degrees C')
    ax1.set_ylabel('Frequency')
    ax1.legend()

    # Plot 2: Sample
    ax2.hist(sample, bins=20, color='salmon', edgecolor='black', alpha=0.7)
    ax2.axvline(sample_mean, color='blue', linestyle='dashed', linewidth=2, label=f'Mean: {sample_mean:.1f}')
    ax2.set_title(f'Random Sample (N={len(sample)})')
    ax2.set_xlabel('Degrees C')
    ax2.legend()

    plt.tight_layout()
    plt.show()

# ==============================================================================
# Data Processing
# ==============================================================================
def get_highs(filename='temperatures.csv'):
    """Read daily high temperatures (Celsius) from a CSV file."""
    if not os.path.exists(filename):
        create_dummy_csv(filename)

    population = []
    with open(filename) as inFile:
        next(inFile, None) # Skip header if it exists
        for line in inFile:
            try:
                # Assuming format: Date,Temperature
                parts = line.split(',')
                if len(parts) >= 2:
                    tempC = float(parts[1])
                    population.append(tempC)
            except ValueError:
                continue
    return population

def get_stats(data):
    """Return mean and standard deviation of a dataset."""
    return np.mean(data), np.std(data)

# ==============================================================================
# Main
# ==============================================================================
def main():
    # 1. Load Data
    population = get_highs()
    if not population:
        print("Error: No data loaded.")
        return
        
    print(f"Loaded {len(population)} temperature records.")

    # 2. Take a Random Sample
    sample_size = 272
    if sample_size > len(population):
        sample_size = len(population)
        
    # Use numpy for potentially faster sampling if list is huge, 
    # but random.sample is fine for standard lists.
    sample = random.sample(population, sample_size)

    # 3. Compute Statistics
    pop_mean, pop_sd = get_stats(population)
    sample_mean, sample_sd = get_stats(sample)

    # 4. Output Text Results
    print("-" * 30)
    print(f"{'Metric':<15} | {'Population':<10} | {'Sample':<10}")
    print("-" * 30)
    print(f"{'Mean':<15} | {pop_mean:<10.2f} | {sample_mean:<10.2f}")
    print(f"{'Std Dev':<15} | {pop_sd:<10.2f} | {sample_sd:<10.2f}")
    print("-" * 30)
    
    # 5. Visual Comparison
    

[Image of normal distribution histogram]

    print("Displaying histograms...")
    plot_comparison(population, sample, pop_mean, sample_mean)

if __name__ == "__main__":
    main()