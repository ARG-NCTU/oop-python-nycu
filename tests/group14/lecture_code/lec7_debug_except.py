"""
lec7_debug_except.py
提供給 lec7 測試使用的最小函式集合：
- rev_list(L)
- primes_list(n)
- get_ratios(L1, L2)
- avg(grades)
- get_stats(class_list)

此檔案放在測試目錄中，供測試以 `import lec7_debug_except as lec` 匯入。
不包含任何互動式輸入或在匯入時執行的示範程式碼。
"""

import math


def rev_list(L):
    """就地反轉列表 L（in-place）。"""
    for i in range(len(L)//2):
        j = len(L) - i - 1
        temp = L[i]
        L[i] = L[j]
        L[j] = temp


def primes_list(n):
    """回傳 2..n 的質數列表（若 n < 2 回傳 []）。"""
    if n < 2:
        return []
    primes = [2]
    for x in range(3, n+1):
        is_div = False
        for p in primes:
            if x % p == 0:
                is_div = True
                break
        if not is_div:
            primes.append(x)
    return primes


def get_ratios(L1, L2):
    """回傳 L1[i]/L2[i] 的列表。若長度不等或型別錯誤則拋出 ValueError。

    除以零的位置放 float('nan')。
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
    return ratios


def avg(grades):
    """計算平均。空列表回傳 0.0。"""
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        return 0.0


def get_stats(class_list):
    """對每位 student 回傳 [name_list, grades_list, average] 的列表。"""
    new_stats = []
    for person in class_list:
        new_stats.append([person[0], person[1], avg(person[1])])
    return new_stats

