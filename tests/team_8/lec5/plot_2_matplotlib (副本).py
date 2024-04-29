import matplotlib.pyplot as plt
import lec5_module as lec5
import pylab
# Function to plot line chart
def plot_mean_distance(walk_lengths, mean_distances1, mean_distances2):
    plt.figure(figsize=(10, 6))
    plt.plot(walk_lengths, mean_distances1, color='r', linestyle='--', label='UsualDrunk')
    plt.plot(walk_lengths, mean_distances2, color='b', linestyle='--', label='MasochistDrunk')
    plt.plot(walk_lengths, pylab.array(walk_lengths)**0.5, color='k', linestyle='-', label='Square root of steps')
    plt.plot(walk_lengths, pylab.array(walk_lengths)*0.05, color='g', linestyle='-', label='numSteps*0.05')
    plt.title('Mean distance from origin (100 trials)')
    plt.xlabel('Number of steps')
    plt.ylabel('Distance from origin')
    plt.grid(True)
    #plt.show()

# Function to plot scatter chart
def plot_end_locations(end_locations1, end_locations2):
    plt.figure(figsize=(10, 6))
    x1 = [loc.x for loc in end_locations1]
    y1 = [loc.y for loc in end_locations2]
    x2 = [loc.x for loc in end_locations2]
    y2 = [loc.y for loc in end_locations2]
    plt.scatter(x1, y1, color='black', marker="+", label='UsualDrunk')
    plt.scatter(x2, y2, color='r', marker="^", label='MasochistDrunk')
    plt.title('Location at End of Walks (10,000 steps)')
    plt.xlabel('Steps East/West of Origin')
    plt.ylabel('Steps North/South of Origin')
    plt.grid(True)
    plt.show()

# Simulating the walks
num_trials = 100
walk_lengths = [100, 1000, 10000]
# add UsualDrunk, MasochistDrunk to the plot
mean_distances1 = lec5.sim_drunk(num_trials, lec5.UsualDrunk, walk_lengths)
mean_distances2 = lec5.sim_drunk(num_trials, lec5.MasochistDrunk, walk_lengths)

# Plotting the mean distance from origin
plot_mean_distance(walk_lengths, mean_distances1, mean_distances2)

# Simulating the walks for 10,000 steps
end_locations1 = [] # UsualDrunk
end_locations2 = [] # MasochistDrunk
steps = 10000
for _ in range(num_trials):
    f = lec5.Field()
    drunk1 = lec5.UsualDrunk()
    drunk2 = lec5.MasochistDrunk()
    f.add_drunk(drunk1, lec5.Location(0, 0))
    f.add_drunk(drunk2, lec5.Location(0, 0))
    lec5.walk(f, drunk1, steps)
    lec5.walk(f, drunk2, steps)
    end_locations1.append(f.get_loc(drunk1))
    end_locations2.append(f.get_loc(drunk2))


# Plotting the end locations
plot_end_locations(end_locations1, end_locations2)


