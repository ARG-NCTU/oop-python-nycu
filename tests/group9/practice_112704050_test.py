import pytest
from practice_112704050 import two_sum,roman_int,min_time_trip,sort_by_height,partition,min_max_diff,fib,reverse_list,remove_nodes,path_togo,path,find_path,num_of_province,min_score  # 如果有需要比較浮點數

### two_sum
def test_two_sum():
    assert two_sum([2,7,11,15], 9) == [0,1]
    assert two_sum([3,2,4], 6) == [1,2]
    assert two_sum([3,3], 6) == [0,1]

### roman_int
def test_roman_int():
    assert roman_int("III") == ([1,1,1], 3)
    assert roman_int("LVIII") == ([50,5,1,1,1], 58)
    assert roman_int("MCMXCIV") == ([1000,100,1000,10,100,1,5], 1994)

### min_time_trip
def test_min_time_trip():
    assert min_time_trip([1,1,2,3], 10) == 4
    assert min_time_trip([2], 1) == 2

### sort_by_height
def test_sort_by_height():
    assert sort_by_height(["M", "J", "E"], [180,165,170]) == ["M","E","J"]
    assert sort_by_height(["A", "B", "B", "C", "D", "E", "F", "G"], [122,133,124,190,190,192,194,192]) == ["F","G","E","D","C","B","B","A"]

### partition
def test_partition():
    assert partition([1,3,2,4]) == 1
    assert partition([100,10,1]) == 9

### min_max_diff
def test_min_max_diff():
    assert min_max_diff([10,1,2,7,4,1,8,11,12,12], 2) == 0

### fib
def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55

### reverse_list
def test_reverse_list():
    assert reverse_list([1,2,3,4,5]) == [5,4,3,2,1]
    assert reverse_list([1,2,3,5,3]) == [3,5,3,2,1]

### remove_nodes
def test_remove_nodes():
    assert remove_nodes([5,2,13,3,8]) == [13,8]
    assert remove_nodes([1,1,1,1]) == [1,1,1,1]

### path (number of enclaves)
def test_path():
    grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    assert path_togo(grid) == 3

### jump game 3
def test_jump_game3():
    assert path([4,2,3,0,3,1,2], 5) == True
    assert path([4,2,3,0,3,1,2], 0) == True
    assert path([3,0,2,1,2], 2) == False

### find_path
def test_find_path():
    assert find_path([[0,1],[1,2],[2,0]], 0, 2) == True
    assert find_path([[0,1],[0,2],[3,5],[5,4],[4,3]], 1, 6) == False

### num_of_province
def test_num_of_province():
    assert num_of_province([[1,1,0],[1,1,0],[0,0,1]]) == 2
    assert num_of_province([[1,0,0],[0,1,0],[0,0,1]]) == 3

### min_score
def test_min_score():
    assert min_score(4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]) == 5
    assert min_score(4, [[1,2,2],[1,3,4],[3,4,7]]) == 2
