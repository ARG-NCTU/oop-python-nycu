import add_path
import pytest
import mit_ocw_data_science.lec2.menu as lec2
import random

def test_food():
    apple = lec2.Food("apple",10,100)
    assert apple.get_value() == 10
    assert apple.get_cost() == 100
    assert apple.density() == 0.1
    assert str(apple) == "apple: <10, 100>"
    
def test_menu():
    m = lec2.Menu(["apple", "banana"], [10, 20], [100, 200])
    assert len(m.get_foods()) == 2
    assert str(m) == "apple: <10, 100>; banana: <20, 200>; "

def test_greedy():
    items = [lec2.Food("apple",10,100), lec2.Food("banana",20,200)]
    max_cost = 150
    key_function = lambda x: -x.get_cost()
    result , val = lec2.greedy(items, max_cost, key_function)
    
    assert len(result) == 1
    assert result[0].get_value() == 10
    assert result[0].get_cost() == 100

def test_max_val():
    items = [lec2.Food("apple",10,100), lec2.Food("banana",20,200),lec2.Food("orange",30,150)]
    max_cost = 250
    result = lec2.max_val(items, max_cost)
    
    assert result[0] == 40


   
        