# -*- coding: utf-8 -*-
"""
Lecture Code整理版 - List操作、例外處理、錯誤修正
"""

# ======================================
# Example 1: Reverse a List
# ======================================

def test_rev_list(L):
    """將列表L原地反轉"""
    for i in range(len(L)//2):
        j = len(L) - i - 1
        temp = L[i]
        L[i] = L[j]
        L[j] = temp


def test_test_rev_list():
    L = [1, 2, 3, 4]
    test_rev_list(L)
    assert L == [4, 3, 2, 1]


# ======================================
# Example 2: Get List of Primes
# ======================================

def test_primes_list(n):
    """回傳2到n之間所有質數"""
    if n < 2:
        return []
    primes = [2]
    for j in range(3, n+1):
        is_div = False
        for p in primes:
            if j % p == 0:
                is_div = True
                break
        if not is_div:
            primes.append(j)
    return primes


def test_test_primes_list():
    assert test_primes_list(2) == [2]
    assert test_primes_list(15) == [2, 3, 5, 7, 11, 13]
    assert test_primes_list(1) == []


# ======================================
# Example 3: Handle Input Exceptions
# ======================================

def test_safe_divide(a, b):
    """安全除法，捕捉除零或輸入錯誤"""
    try:
        return a / b
    except ValueError:
        return "Could not convert to a number."
    except ZeroDivisionError:
        return "Can't divide by zero"
    except:
        return "Something went very wrong."


def test_test_safe_divide():
    assert test_safe_divide(6, 2) == 3
    assert test_safe_divide(6, 0) == "Can't divide by zero"


# ======================================
# Example 4: Raising Your Own Exceptions
# ======================================

def test_get_ratios(L1, L2):
    """兩個列表對應元素相除，處理除零或錯誤型別"""
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('test_get_ratios called with bad arg')
    return ratios


def test_test_get_ratios():
    assert test_get_ratios([1, 4], [2, 4]) == [0.5, 1.0]


# ======================================
# Example 5: List Stats and Average with Assertion
# ======================================

def test_avg(grades):
    """計算grades平均值，若為空則引發assert"""
    assert len(grades) != 0, 'warning: no grades data'
    return sum(grades) / len(grades)


def test_get_stats(class_list):
    """回傳每個學生的成績列表與平均值"""
    new_stats = []
    for person in class_list:
        name = person[0]
        grades = person[1]
        avg_grade = test_avg(grades) if grades else 0.0
        new_stats.append([name, grades, avg_grade])
    return new_stats


def test_test_get_stats():
    test_grades = [
        [['peter', 'parker'], [80.0, 70.0, 85.0]],
        [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
        [['captain', 'america'], [80.0, 70.0, 96.0]],
        [['deadpool'], []]
    ]
    result = test_get_stats(test_grades)
    assert result[0][2] == 78.33333333333333  # Peter Parker avg
    assert result[1][2] == 84.66666666666667  # Bruce Wayne avg
    assert result[3][2] == 0.0                # Deadpool無成績


# ======================================
# Example: if __name__ == "__main__" 測試手動執行
# ======================================

if __name__ == "__main__":
    test_test_rev_list()
    test_test_primes_list()
    test_test_safe_divide()
    test_test_get_ratios()
    test_test_get_stats()
    print("All manual tests passed.")
