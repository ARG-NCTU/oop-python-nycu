def rev(L):
    """Reverse list in-place."""
    n = len(L)
    for i in range(n // 2):
        L[i], L[n - i - 1] = L[n - i - 1], L[i]

sample = [1, 2, 3, 4]
rev(sample)
print(sample)

def primes_upto(n):
    if n < 2: return []
    ps = [2]
    for j in range(3, n + 1):
        if all(j % p != 0 for p in ps):
            ps.append(j)
    return ps

print(primes_upto(2))
print(primes_upto(15))

try:
    x = int(input("Num 1: "))
    y = int(input("Num 2: "))
    print("x / y =", x / y)
except ZeroDivisionError:
    print("Division by 0")
except ValueError:
    print("Invalid number")
except:
    print("Unknown error")

def ratios(L1, L2):
    out = []
    for i in range(len(L1)):
        try:
            out.append(L1[i] / L2[i])
        except ZeroDivisionError:
            out.append(float('nan'))
        except:
            raise ValueError("Bad inputs")
        finally:
            print("Done", i)
    return out

print(ratios([1, 4], [2, 4]))

def avg(grades):
    assert grades, "Empty!"
    return sum(grades) / len(grades)

def stats(data):
    return [[name, g, avg(g)] for name, g in data]

data = [
    [['peter', 'parker'], [80, 70, 85]],
    [['bruce', 'wayne'], [100, 80, 74]],
    [['captain', 'america'], [80, 70, 96]],
    [['deadpool'], []]
]

# print(stats(data))

