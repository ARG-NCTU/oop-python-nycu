import add_path
import mit_ocw_exercises
import pytest
class Animal(object):
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
class Dog(Animal):
    def speak(self):
        return 'ruff ruff'
    def behave(self, doing="nothing"):
        return self.name + doing + '.'
    def set_type(self, t):
        self.type = t
    def get_type(self):
        return self.type
    def __str__(self):
        return "dog:"+str(self.name)+":"+str(self.age)

class Cat(Animal):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
    def speak(self):
        return self.name + ' says meow!'
class Person(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Person named ' + self.name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return self.name != other.name
    def __lt__(self, other):
        return self.name < other.name
    def __hash__(self):
        return self.name
    def speak(self):
        return self.name + ' says hello!'
class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign
    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        self.idNum = MITPerson.nextIdNum # MITPerson attribute: unique ID
        MITPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def speak(self):
        return self.name + ' says hi!'
    def __lt__(self, other):
        return self.idNum < other.idNum
    
ani = Animal(3)
print(ani)
ani.set_name("fluffy")
print(ani)
print(ani.get_name())
print(ani.get_age())

print("=========================================================")
dog = Dog(5)
dog.set_name("Lucky")
print(dog)
print(dog.speak())
print(dog.behave("bite biker"))
dog.set_type("pit bull")
print(dog.name, "is", dog.get_type())
print("=========================================================")
cat = Cat("fluffy", "me")
cat.set_age(4)
print(cat)
print(cat.speak())
print("=========================================================")
p1 = Person("joe")
p2 = Person("jane")
print(p1)
print(p1.say("hi")) # joe says: hi
print(p2.say("hello")) # jane says: hello
print(p1 == p2) # False
print(p1 != p2) # True
print(p1 < p2) # True
print("=========================================================")
m3 = MITPerson("Mark")
m4 = MITPerson("Mark")
print(m3)
print(m3.getIdNum())
print(m4.getIdNum())
print(m3 < m4)
print("=========================================================")
p1 = MITPerson("Eric")
p2 = MITPerson("John")
p3 = MITPerson("John")
p4 = Person("John")
print(p1)
print(p1.getIdNum())
print(p2.getIdNum())
print(p1 < p2)
print(p3 < p2)
print(p4 < p1)
print(p4 < p4)
print("=========================================================")

import pytest
# from your_module import Animal, Dog, Cat, Person, MITPerson  # 替換為你的模組名稱

def test_animal_basic():
    a = Animal(5)
    a.set_name("Fluffy")
    assert a.get_age() == 5
    assert a.get_name() == "Fluffy"
    assert str(a) == "animal:Fluffy:5"

def test_dog_behavior():
    d = Dog(3)
    d.set_name("Lucky")
    d.set_type("pit bull")
    assert d.get_type() == "pit bull"
    assert d.speak() == "ruff ruff"
    assert d.behave("chase tail") == "Luckychase tail."
    assert str(d) == "dog:Lucky:3"

def test_cat_behavior():
    c = Cat("Mimi", "Alice")
    c.set_age(2)
    assert c.name == "Mimi"
    assert c.owner == "Alice"
    assert c.get_age() == 2
    assert c.speak() == "Mimi says meow!"

def test_person_comparison():
    p1 = Person("Alice")
    p2 = Person("Bob")
    p3 = Person("Alice")
    assert p1 == p3
    assert p1 != p2
    assert p1 < p2
    assert p1.speak() == "Alice says hello!"

def test_mit_person_id_and_comparison():
    MITPerson.nextIdNum = 0  # reset for testing consistency
    m1 = MITPerson("Tom")
    m2 = MITPerson("Jerry")
    assert m1.getIdNum() == 0
    assert m2.getIdNum() == 1
    assert m1 < m2
    assert m1.speak() == "Tom says hi!"
