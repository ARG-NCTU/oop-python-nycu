class Animal:
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
        return "animal:" + str(self.name) + ":" + str(self.age)


def test_animal_basic():
    a = Animal(3)
    a.set_name("Fluffy")
    assert a.get_age() == 3
    assert a.get_name() == "Fluffy"
    assert str(a) == "animal:Fluffy:3"

def test_animal_set_name_default():
    a = Animal(1)
    a.set_name()
    assert a.get_name() == ""

class Cat(Animal):
    def speak(self):
        return "meow"

    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)


def test_cat_behavior():
    c = Cat(5)
    c.set_name("Mittens")
    assert str(c) == "cat:Mittens:5"
    assert c.speak() == "meow"

class Person(Animal):
    def __init__(self, name, age):
        super().__init__(age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def speak(self):
        return "hello"

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def age_diff(self, other):
        return abs(self.age - other.age)

    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)

def test_person_behavior():
    p = Person("Jack", 30)
    assert p.get_name() == "Jack"
    assert p.get_age() == 30
    assert p.speak() == "hello"
    assert str(p) == "person:Jack:30"

def test_add_and_get_friends():
    p = Person("Alice", 20)
    p.add_friend("Bob")
    p.add_friend("Bob")  # 測試不重複
    p.add_friend("Carol")
    assert p.get_friends() == ["Bob", "Carol"]

def test_age_diff():
    p1 = Person("A", 25)
    p2 = Person("B", 20)
    assert p1.age_diff(p2) == 5
    assert p2.age_diff(p1) == 5

class Student(Person):
    def __init__(self, name, age, major=None):
        super().__init__(name, age)
        self.major = major

    def __str__(self):
        return "student:" + str(self.name) + ":" + str(self.age) + ":" + str(self.major)

def test_student_behavior():
    s = Student("Lily", 21, "CS")
    assert s.get_name() == "Lily"
    assert s.get_age() == 21
    assert s.major == "CS"
    assert str(s) == "student:Lily:21:CS"

def test_student_inherits_person():
    s = Student("Tom", 22)
    s.add_friend("Jerry")
    assert s.get_friends() == ["Jerry"]
    assert s.speak() == "hello"