import pytest
import random
from lec5_tuples_lists import quotient_and_remainder, get_data, sum_elem_method1, sum_elem_method2, remove_dups, remove_dups_new

def test_quotient_and_remainder(capsys):
    res = quotient_and_remainder(5, 3)
    assert res == (1, 2)
    print(res[0])
    print(res[1])
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["1", "2"]

def test_get_data(capsys):
    test_data = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    res = get_data(test_data)
    assert res == (1, 7, 2)
    print("a:", res[0], "b:", res[1], "c:", res[2])
    captured = capsys.readouterr().out.strip()
    assert "a:" in captured
    tswift = ((2014, "Katy"), (2014, "Harry"), (2012, "Jake"), (2010, "Taylor"), (2008, "Joe"))
    res2 = get_data(tswift)
    assert res2 == (2008, 2014, 5)
    print("From", res2[0], "to", res2[1], "Taylor Swift wrote songs about", res2[2], "people!")
    captured = capsys.readouterr().out.strip()
    assert "Taylor Swift" in captured

def test_sum_elem_methods():
    assert sum_elem_method1([1, 2, 3, 4]) == 10
    assert sum_elem_method2([1, 2, 3, 4]) == 10

def test_list_operations(capsys):
    L1 = [2, 1, 3]
    L2 = [4, 5, 6]
    L3 = L1 + L2
    L1.extend([0, 6])
    L = [2, 1, 3, 6, 3, 7, 0]
    L.remove(2)
    L.remove(3)
    del(L[1])
    print(L.pop())
    s = "I<3 cs"
    print(list(s))
    print(s.split('<'))
    L = ['a', 'b', 'c']
    print(''.join(L))
    print('_'.join(L))
    L = [9, 6, 0, 3]
    print(sorted(L))
    L.sort()
    L.reverse()
    captured = capsys.readouterr().out.strip().splitlines()
    expected = [
        "0",
        "['I', '<', '3', ' ', 'c', 's']",
        "['I', '3 cs']",
        "abc",
        "a_b_c",
        "[0, 3, 6, 9]"
    ]
    assert captured == expected

def test_aliasing(capsys):
    a = 1
    b = a
    print(a)
    print(b)
    warm = ['red', 'yellow', 'orange']
    hot = warm
    hot.append('pink')
    print(hot)
    print(warm)
    captured = capsys.readouterr().out.strip().splitlines()
    expected = [
        "1",
        "1",
        "['red', 'yellow', 'orange', 'pink']",
        "['red', 'yellow', 'orange', 'pink']"
    ]
    assert captured == expected

def test_cloning(capsys):
    cool = ['blue', 'green', 'grey']
    chill = cool[:]
    chill.append('black')
    print(chill)
    print(cool)
    captured = capsys.readouterr().out.strip().splitlines()
    expected = [
        "['blue', 'green', 'grey', 'black']",
        "['blue', 'green', 'grey']"
    ]
    assert captured == expected

def test_sorting(capsys):
    warm = ['red', 'yellow', 'orange']
    sortedwarm = warm.sort()
    print(warm)
    print(sortedwarm)
    cool = ['grey', 'green', 'blue']
    sortedcool = sorted(cool)
    print(cool)
    print(sortedcool)
    captured = capsys.readouterr().out.strip().splitlines()
    expected = [
        "['orange', 'red', 'yellow']",
        "None",
        "['grey', 'green', 'blue']",
        "['blue', 'green', 'grey']"
    ]
    assert captured == expected

def test_list_of_lists(capsys):
    warm = ['yellow', 'orange']
    hot = ['red']
    brightcolors = [warm]
    brightcolors.append(hot)
    print(brightcolors)
    hot.append('pink')
    print(hot)
    print(brightcolors)
    captured = capsys.readouterr().out.strip().splitlines()
    expected = [
        "[['yellow', 'orange'], ['red']]",
        "['red', 'pink']",
        "[['yellow', 'orange'], ['red', 'pink']]"
    ]
    assert captured == expected

def test_remove_dups(capsys):
    def remove_dups(L1, L2):
        for e in L1:
            if e in L2:
                L1.remove(e)
    def remove_dups_new(L1, L2):
        L1_copy = L1[:]
        for e in L1_copy:
            if e in L2:
                L1.remove(e)
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    remove_dups(L1, L2)
    print(L1, L2)
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    remove_dups_new(L1, L2)
    print(L1, L2)
    captured = capsys.readouterr().out.strip().splitlines()
    expected = [
        "[2, 3, 4] [1, 2, 5, 6]",
        "[3, 4] [1, 2, 5, 6]"
    ]
    assert captured == expected

def test_exercise(capsys):
    cool = ['blue', 'green']
    warm = ['red', 'yellow', 'orange']
    print(cool)
    print(warm)
    colors1 = [cool]
    print(colors1)
    colors1.append(warm)
    print('colors1 = ', colors1)
    colors2 = [['blue', 'green'], ['red', 'yellow', 'orange']]
    print('colors2 =', colors2)
    warm.remove('red')
    print('colors1 = ', colors1)
    print('colors2 =', colors2)
    for e in colors1:
        print('e =', e)
    for e in colors1:
        if type(e) == list:
            for e1 in e:
                print(e1)
        else:
            print(e)
    flat = cool + warm
    print('flat =', flat)
    print(flat.sort())
    print('flat =', flat)
    new_flat = sorted(flat, reverse=True)
    print('flat =', flat)
    print('new_flat =', new_flat)
    cool[1] = 'black'
    print(cool)
    print(colors1)
    captured = capsys.readouterr().out.strip().splitlines()
    expected = [
        "['blue', 'green']",
        "['red', 'yellow', 'orange']",
        "[['blue', 'green']]",
        "colors1 =  [['blue', 'green'], ['red', 'yellow', 'orange']]",
        "colors2 = [['blue', 'green'], ['red', 'yellow', 'orange']]",
        "colors1 =  [['blue', 'green'], ['yellow', 'orange']]",
        "colors2 = [['blue', 'green'], ['red', 'yellow', 'orange']]",
        "e = ['blue', 'green']",
        "e = ['yellow', 'orange']",
        "blue",
        "green",
        "yellow",
        "orange",
        "flat = ['blue', 'green', 'yellow', 'orange']",
        "None",
        "flat = ['blue', 'green', 'orange', 'yellow']",
        "flat = ['blue', 'green', 'orange', 'yellow']",
        "new_flat = ['yellow', 'orange', 'green', 'blue']",
        "['blue', 'black']",
        "[['blue', 'black'], ['yellow', 'orange']]"
    ]
    assert captured == expected
