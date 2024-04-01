import menu as inh
import pytest

def test_menu():
    menu = inh.Menu(["apple", "banana", "cherry"],[100,200,300],[150,250,350])
    print(menu)
    #test build_large_menu
    num = 10
    max_val = 1000
    max_cost = 500
    menu2 = inh.Menu()
    menu2.build_large_menu(num, max_val, max_cost)
    print(menu2)
    foods = menu2.get_foods()
    assert len(foods) == num
    for i in range(num):
        assert foods[i].get_value() <= max_val
        assert foods[i].get_cost() <= max_cost
    
