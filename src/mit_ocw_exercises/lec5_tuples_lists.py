# src/mit_ocw_exercises/lec5_tuples_lists.py

from typing import Iterable, Tuple, List

def quotient_and_remainder(x: int, y: int) -> Tuple[int, int]:
    """
    Return (quotient, remainder) for integers x, y with y != 0.
    """
    if y == 0:
        raise ZeroDivisionError("y must not be zero")
    return (x // y, x % y)


def get_data(aTuple: Tuple[Tuple[int, str], ...]) -> Tuple[int, int, int]:
    """
    aTuple: tuple of (int, str)
    Returns (min_int, max_int, num_unique_strings).
    """
    if not aTuple:
        raise ValueError("aTuple must not be empty")
    nums: Tuple[int, ...] = ()
    words: Tuple[str, ...] = ()
    for t in aTuple:
        nums += (t[0],)
        if t[1] not in words:
            words += (t[1],)
    return (min(nums), max(nums), len(words))


def sum_elem_method1(L: Iterable[int]) -> int:
    total = 0
    for i, _ in enumerate(L):
        total += list(L)[i]
    return total


def sum_elem_method2(L: Iterable[int]) -> int:
    total = 0
    for v in L:
        total += v
    return total


def remove_dups(L1: List[int], L2: List[int]) -> None:
    """
    Mutates L1: remove any element that is also in L2.
    (正確版，避免邊走邊砍造成漏刪)
    """
    i = 0
    while i < len(L1):
        if L1[i] in L2:
            L1.pop(i)
        else:
            i += 1


def remove_dups_new(L1: List[int], L2: List[int]) -> None:
    """
    Mutates L1: safe version using a copy.
    """
    for e in L1[:]:
        if e in L2:
            L1.remove(e)

