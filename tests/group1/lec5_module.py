import random
import pylab

# set line width
pylab.rcParams['lines.linewidth'] = 4
# set font size for titles
pylab.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
# set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
# set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
# set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
# set size of markers, e.g., circles representing points
# set numpoints for legend
pylab.rcParams['legend.numpoints'] = 1


class Location:
    def __init__(self, x, y):
        """Initialize a location with x and y coordinates (numbers)."""
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError(f"Coordinates must be numbers, got x={type(x).__name__}, y={type(y).__name__}")
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        """Return new Location after moving by delta_x and delta_y (numbers)."""
        return Location(self.x + delta_x, self.y + delta_y)

    def get_x(self):
        """Return x coordinate."""
        return self.x

    def get_y(self):
        """Return y coordinate."""
        return self.y

    def dist_from(self, other):
        """Calculate Euclidean distance from another Location."""
        if not isinstance(other, Location):
            raise TypeError(f"Expected Location object, got {type(other).__name__}")
        x_dist = self.x - other.get_x()
        y_dist = self.y - other.get_y()
        return (x_dist ** 2 + y_dist ** 2) ** 0.5

    def __str__(self):
        return f"<{self.x}, {self.y}>"
    
    def __eq__(self, other):
        """Check if two locations are at the same coordinates."""
        if not isinstance(other, Location):
            return False
        return self.x == other.x and self.y == other.y


class Field:
    def __init__(self):
        """Initialize an empty field for drunk simulations."""
        self.drunks = {}

    def add_drunk(self, drunk, loc):
        """Add a drunk person at a specific location."""
        if drunk in self.drunks:
            raise ValueError(f'Duplicate drunk: {drunk}')
        if not isinstance(loc, Location):
            raise TypeError(f"Expected Location object, got {type(loc).__name__}")
        self.drunks[drunk] = loc

    def move_drunk(self, drunk):
        """Move a drunk person one step in a random direction."""
        if drunk not in self.drunks:
            raise ValueError(f'Drunk not in field: {drunk}')
        x_dist, y_dist = drunk.take_step()
        # use move method of Location to get new location
        self.drunks[drunk] = self.drunks[drunk].move(x_dist, y_dist)

    def get_loc(self, drunk):
        """Get the current location of a drunk person."""
        if drunk not in self.drunks:
            raise ValueError(f'Drunk not in field: {drunk}')
        return self.drunks[drunk]
    
    def num_drunks(self):
        """Return the number of drunks currently in the field."""
        return len(self.drunks)

class Drunk:
    def __init__(self, name=None):
        """Initialize a drunk person with an optional name (str)."""
        self.name = name

    def __str__(self):
        """Return the name of the drunk person."""
        if self.name is not None:
            return self.name
        return 'Anonymous'
    
    def take_step(self):
        """Return a tuple (x_dist, y_dist) representing one step.
           Subclasses must override this method."""
        raise NotImplementedError("Subclasses must implement take_step()")

class UsualDrunk(Drunk):
    """A drunk that takes random steps in cardinal directions (up, down, left, right)."""
    def take_step(self):
        """Return a random step: (0,1), (0,-1), (1,0), or (-1,0)."""
        step_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(step_choices)

class MasochistDrunk(Drunk):
    """A drunk that walks further up than down (biased random walk)."""
    def take_step(self):
        """Return a biased random step with stronger upward movement."""
        step_choices = [(0.0, 1.1), (0.0, -0.9),
                        (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)

def walk(f, d, num_steps):
    """Simulate a drunk's random walk.
    
    Args:
        f: A Field object containing the drunk
        d: A Drunk object to simulate
        num_steps: Number of steps to walk (int >= 0)
    
    Returns:
        The distance from starting location to ending location
    
    Raises:
        ValueError: If num_steps is negative
    """
    if num_steps < 0:
        raise ValueError(f"num_steps must be non-negative, got {num_steps}")
    start = f.get_loc(d)
    for s in range(num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))
    
def sim_walks(num_steps, num_trials, d_class):
    """Simulate multiple walks for a given drunk class.
    
    Args:
        num_steps: Number of steps in each walk (int >= 0)
        num_trials: Number of walks to simulate (int > 0)
        d_class: A subclass of Drunk to simulate
    
    Returns:
        List of final distances for each trial
    
    Raises:
        ValueError: If num_steps < 0 or num_trials <= 0
    """
    if num_steps < 0:
        raise ValueError(f"num_steps must be non-negative, got {num_steps}")
    if num_trials <= 0:
        raise ValueError(f"num_trials must be positive, got {num_trials}")
    
    Homer = d_class('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(num_trials):
        f = Field()
        f.add_drunk(Homer, origin)
        distances.append(round(walk(f, Homer, num_steps), 1))
    return distances

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

def sim_drunk(num_trials, d_class, walk_lengths):
    """Simulate walks of varying lengths for a drunk class.
    
    Args:
        num_trials: Number of trials for each walk length (int > 0)
        d_class: A subclass of Drunk to simulate
        walk_lengths: List of step counts to simulate
    
    Returns:
        List of mean distances for each walk length
    
    Raises:
        ValueError: If num_trials <= 0
    """
    if num_trials <= 0:
        raise ValueError(f"num_trials must be positive, got {num_trials}")
    
    mean_distances = []
    for num_steps in walk_lengths:
        print(f'Starting simulation of {num_steps} steps')
        trials = sim_walks(num_steps, num_trials, d_class)
        mean = sum(trials) / len(trials)
        mean_distances.append(mean)
    return mean_distances
