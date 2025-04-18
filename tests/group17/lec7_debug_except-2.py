# Reverses a list in-place
def reverse_list_in_place(data):
    mid = len(data) // 2
    for idx in range(mid):
        opp = len(data) - idx - 1
        tmp = data[idx]
        data[idx] = data[opp]
        data[opp] = tmp

values = [1, 2, 3, 4]
reverse_list_in_place(values)
print(values)

# Returns all primes up to n
def generate_primes(n):
    if n < 2:
        return []
    primes = [2]
    for val in range(3, n + 1):
        divisible = False
        for prime in primes:
            if val % prime == 0:
                divisible = True
                break
        if not divisible:
            primes.append(val)
    return primes

print(generate_primes(2))
print(generate_primes(15))

# Try input and handle common errors
try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print("a / b = ", a / b)
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception:
    print("Error occurred.")

# Calculate element-wise ratios of two lists
def get_element_ratios(L1, L2):
    results = []
    for idx in range(len(L1)):
        try:
            results.append(L1[idx] / L2[idx])
        except ZeroDivisionError:
            results.append(float('nan'))
        except Exception:
            raise ValueError("Invalid parameters")
        finally:
            print("Processed pair", idx)
    return results

print(get_element_ratios([1, 4], [2, 4]))

# Average calculation with assert
def safe_avg(grades):
    assert len(grades) > 0, "Grades list is empty"
    return sum(grades) / len(grades)

# Process grades
def compute_class_stats(class_data):
    summary = []
    for entry in class_data:
        summary.append([entry[0], entry[1], safe_avg(entry[1])])
    return summary

grades_data = [
    [['peter', 'parker'], [80, 70, 85]],
    [['bruce', 'wayne'], [100, 80, 74]],
    [['captain', 'america'], [80, 70, 96]],
    [['deadpool'], []]
]

# print(compute_class_stats(grades_data))

