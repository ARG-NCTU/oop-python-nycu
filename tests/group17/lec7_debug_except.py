# --- Reverse List Function ---
def reverse_items(lst):
    """In-place reverse of list."""
    for i in range(len(lst) // 2):
        j = len(lst) - i - 1
        lst[i], lst[j] = lst[j], lst[i]

nums = [1, 2, 3, 4]
reverse_items(nums)
print(nums)

# --- Generate Primes Function ---
def list_primes(limit):
    """Returns all prime numbers ≤ limit."""
    primes = [2]
    for num in range(3, limit + 1):
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
    return primes

print(list_primes(2))
print(list_primes(15))

# --- Exception Handling with Input ---
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another: "))
    print("a / b =", a / b)
except ZeroDivisionError:
    print("Division by zero error")
except ValueError:
    print("Not a valid number")
except:
    print("Unexpected error")

# --- Ratios with Exception Handling ---
def calc_ratios(a, b):
    result = []
    for i in range(len(a)):
        try:
            result.append(a[i] / b[i])
        except ZeroDivisionError:
            result.append(float('nan'))
        except:
            raise ValueError("Invalid inputs")
        else:
            print("Success")
        finally:
            print("Done with index", i)
    return result

print(calc_ratios([1, 4], [2, 4]))

# --- Average Function with Assert ---
def average(scores):
    assert scores, "Empty score list"
    return sum(scores) / len(scores)

# --- Class Stats ---
def class_averages(data):
    stats = []
    for person in data:
        stats.append([person[0], person[1], average(person[1])])
    return stats

students = [
    [['peter', 'parker'], [80, 70, 85]],
    [['bruce', 'wayne'], [100, 80, 74]],
    [['captain', 'america'], [80, 70, 96]],
    [['deadpool'], []]
]

# print(class_averages(students))

