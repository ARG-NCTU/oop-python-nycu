def rev_list(L):
    for i in range(len(L) // 2):
        j = len(L) - i - 1
        L[i], L[j] = L[j], L[i]
    return L  # 為了測試方便也 return

def primes_list(n):
    if n < 2:
        return []
    primes = [2]
    for j in range(3, n + 1):
        is_div = False
        for p in primes:
            if j % p == 0:
                is_div = True
                break
        if not is_div:
            primes.append(j)
    return primes

def get_ratios(L1, L2):
    ratios = []
    for i in range(len(L1)):
        try:
            ratios.append(L1[i] / L2[i])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError("get_ratios called with bad arg")
    return ratios

def avg(grades):
    assert len(grades) != 0, "warning: no grades data"
    return sum(grades) / len(grades)

def get_stats(class_list):
    new_stats = []
    for person in class_list:
        name, grades = person[0], person[1]
        try:
            average = avg(grades)
        except AssertionError as e:
            average = 0.0
        new_stats.append([name, grades, average])
    return new_stats
