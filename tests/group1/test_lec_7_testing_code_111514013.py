######################################
# EXAMPLE: Exceptions and input
######################################
#a = int(input("Tell me one number: "))
#b = int(input("Tell me another number: "))
#print("a/b = ", a/b)
#print("a+b = ", a+b)

try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
    print("a+b = ", a+b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Something went very wrong.")



######################################
# EXAMPLE: Raising your own exceptions
######################################
def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    ratios = []
    try:
        assert len(L1) == len(L2)
    except:
        raise  ValueError('Diff length!!')
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('get_ratios called with bad arg')
        else:
            print("success")
        finally:
            print("executed no matter what!")
    return ratios
    
print(get_ratios([1, 4], [2, 4]))


#######################################
## EXAMPLE: Exceptions and lists
#######################################
import statistics

def avg(grades):
    """Calculate the average score of a list of grades"""
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print('Warning: no grades data')
        return 0.0

def get_stats(class_list):
    """Returns a list of stats for each student:
       Name, Average, Total, Max, Min, Standard Deviation"""
    
    new_stats = []
    
    for person in class_list:
        name = person[0]
        grades = person[1]
        
        # Calculate the required statistics
        average = avg(grades)
        total = sum(grades)
        max_score = max(grades) if grades else 0
        min_score = min(grades) if grades else 0
        std_dev = statistics.stdev(grades) if len(grades) > 1 else 0.0
        
        new_stats.append([name, average, total, max_score, min_score, std_dev])
    
    return new_stats

# Test Data
test_grades = [
    [['Pet', 'Park'], [80.0, 70.0, 85.0]], 
    [['Shin', 'Wayne'], [100.0, 80.0, 74.0]],
    [['Captain', 'Japan'], [80.0, 70.0, 96.0]],
    [['Deadmountain'], []]  # Empty grades to test for ZeroDivisionError
]

# Test the function
stats = get_stats(test_grades)

# Print the stats
for stat in stats:
    print(f"Name: {stat[0]}, Average: {stat[1]}, Total: {stat[2]}, Max: {stat[3]}, Min: {stat[4]}, Std Dev: {stat[5]}")
