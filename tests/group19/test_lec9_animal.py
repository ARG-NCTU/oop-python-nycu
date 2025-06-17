import pytest

class Animal(object):
    '''Animal Class 
    Attributes: age, name
    Methods: get_age, get_name, set_age, set_name, __str__
    '''
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
    
def test_animal_initialization():
    animal = Animal(5)
    assert animal.get_age() == 5
    assert animal.get_name() is None

def test_set_name():
    animal = Animal(3)
    animal.set_name("Buddy")
    assert animal.get_name() == "Buddy"

def test_set_age():
    animal = Animal(2)
    animal.set_age(4)
    assert animal.get_age() == 4

def test_str_representation():
    animal = Animal(7)
    animal.set_name("Charlie")
    assert str(animal) == "animal:Charlie:7"
    
    