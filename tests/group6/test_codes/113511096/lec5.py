import random
import matplotlib.pyplot as plt
import pytest


# ----------------- Configuration -----------------

plt.rcParams['lines.linewidth'] = 6
plt.rcParams['axes.titlesize'] = 30

plt.rcParams['axes.labelsize'] = 30

plt.rcParams['xtick.labelsize'] = 24

plt.rcParams['ytick.labelsize'] = 24
# set size of ticks on x-axis
plt.rcParams['xtick.major.size'] = 10
# set size of ticks on y-axis
plt.rcParams['ytick.major.size'] = 10
# set numpoints for legend
plt.rcParams['legend.numpoints'] = 1


# ----------------- Classes -----------------
class Location:
    def __init__(self, x, y):
        """x and y are numbers"""
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        """delta_x and delta_y are numbers"""
        return Location(self.x + delta_x, self.y + delta_y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def dist_from(self, other):
        x_dist = self.x - other.get_x()
        y_dist = self.y - other.get_y()
        return (x_dist ** 2 + y_dist ** 2) ** 0.5

    def __str__(self):
        return f"<{self.x}, {self.y}>"


class Field:
    def __init__(self):
        self.drunks = {}

    def add_drunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def move_drunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        x_dist, y_dist = drunk.take_step()
        # use move method of Location to get new location
        self.drunks[drunk] = self.drunks[drunk].move(x_dist, y_dist)

    def get_loc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


class Drunk:
    def __init__(self, name=None):
        """Assumes name is a str"""
        self.name = name

    def __str__(self):
        if self is not None:
            return self.name
        return 'Anonymous'


class UsualDrunk(Drunk):
    def take_step(self):
        step_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(step_choices)


class MasochistDrunk(Drunk):
    def take_step(self):
        # Biased movement: tries to move North (1.1) but slips back South (-0.9) more easily
        step_choices = [(0.0, 1.1), (0.0, -0.9),
                        (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)


class StyleIterator:
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def next_style(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result


# ----------------- Simulation Logic -----------------

def walk(f, d, num_steps):
    """
    Assumes: f a Field, d a Drunk in f, and num_steps an int >= 0.
    Moves d num_steps times, and returns the distance between
    the final location and the location at the start of the walk.
    """
    start = f.get_loc(d)
    for s in range(num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))


def sim_walks(num_steps, num_trials, d_class):
    """
    Assumes num_steps an int >= 0, num_trials an int > 0,
    d_class a subclass of Drunk.
    Simulates num_trials walks of num_steps steps each.
    Returns a list of the final distances for each trial.
    """
    homer = d_class('Homer')
    origin = Location(0, 0)
    distances = []
    
    for t in range(num_trials):
        f = Field()
        f.add_drunk(homer, origin)
        distances.append(round(walk(f, homer, num_steps), 1))
    return distances


def get_mean_distances(num_trials, d_class, walk_lengths):
    """
    Calculates mean distances for a specific drunk class over various step counts.
    """
    mean_distances = []
    for num_steps in walk_lengths:
        print(f'   Simulating {d_class.__name__} walk of {num_steps} steps')
        trials = sim_walks(num_steps, num_trials, d_class)
        mean = sum(trials) / len(trials)
        mean_distances.append(mean)
    return mean_distances


def plot_drunk_sim(drunk_kinds, walk_lengths, num_trials):
    """
    Runs simulations for provided drunk classes and plots the results.
    """
    style_iter = StyleIterator(['k-', 'r:', 'b--', 'g-.'])
    
    print(f"Starting Simulation ({num_trials} trials per point)...")
    
    for d_class in drunk_kinds:
        means = get_mean_distances(num_trials, d_class, walk_lengths)
        cur_style = style_iter.next_style()
        plt.plot(walk_lengths, means, cur_style, label=d_class.__name__)
    
    plt.title(f'Mean Distance from Origin ({num_trials} trials)')
    plt.xlabel('Number of Steps')
    plt.ylabel('Distance from Origin')
    plt.legend(loc='best')
    plt.grid(True)
    
    print("Plot generated.")
    plt.show()

# ----------------- Main Execution -----------------

if __name__ == "__main__":
    # Define the range of steps to test (e.g., 10, 100, 1000, 10000)
    steps_to_test = [10, 100, 1000, 10000]
    
    # Define which drunk classes to compare
    drunks_to_test = [UsualDrunk, MasochistDrunk]
    
    # Run simulation and plot
    plot_drunk_sim(drunks_to_test, steps_to_test, 100)