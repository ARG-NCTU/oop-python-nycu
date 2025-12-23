import math

# 1. 反轉串列 rev_list
def rev_list(L):
  for i in range(len(L) // 2):
    j = len(L) - i - 1
    temp = L[i]
    L[i] = L[j]
    L[j] = temp
# 2. primes_list(generating primes)
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
# 3. get_ratios - (calcilating the ratio)
def get_ratios(L1, L2):
  """
  假設 L1 和 L2 是長度相等的數字列表。
  返回一個包含 L1[i]/L2[i] 的列表。
  """
  if len(L1) != len(L2):
    raise ValueError('get_ratios called with lists of different lengths')

  ratios = []
  for i in range(len(L1)):
    try:
      ratios.append(L1[i] / L2[i])
    except ZeroDivisionError:
      ratios.append(float('nan'))
    except TypeError:
      raise ValueError('get_ratios called with bad argument type')
    else:
      pass
    finally:
      pass

  return ratios
# 4. avg —（calculating average）
def avg(grades):
  try:
    return sum(grades) / len(grades)
  except ZeroDivisionError:
    return 0.0
# 5. get_stats — (return the average grade)
def get_stats(class_list):
  new_stats = []
  for person in class_list:
    name = person[0]
    grades = person[1]
    new_stats.append([name, grades, avg(grades)])
  return new_stats

