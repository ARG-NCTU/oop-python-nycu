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


   
        