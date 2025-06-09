import random

# === Animal 類別 ===
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
        return f"animal:{self.name}:{self.age}"


# === Cat 類別 ===
class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return f"cat:{self.name}:{self.age}"


# === Person 類別 ===
class Person(Animal):
    def __init__(self, name, age):
        super().__init__(age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def speak(self):
        print("hello")

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def age_diff(self, other):
        diff = abs(self.age - other.age)
        print(f"{diff} year difference")

    def __str__(self):
        return f"person:{self.name}:{self.age}"


# === Student 類別 ===
class Student(Person):
    def __init__(self, name, age, major=None):
        super().__init__(name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif r < 0.5:
            print("i need sleep")
        elif r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")

    def __str__(self):
        return f"student:{self.name}:{self.age}:{self.major}"


# === Rabbit 類別 ===
class Rabbit(Animal):
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        super().__init__(age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        return Rabbit(0, self, other)

    def __eq__(self, other):
        if None in (self.parent1, self.parent2, other.parent1, other.parent2):
            return False
        same = (self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid)
        oppo = (self.parent1.rid == other.parent2.rid and self.parent2.rid == other.parent1.rid)
        return same or oppo

    def __str__(self):
        return f"rabbit:{self.get_rid()}"

# === Tests ===
def test_animal():
    a = Animal(5)
    a.set_name("Generic Animal")
    assert a.get_age() == 5
    assert a.get_name() == "Generic Animal"
    assert str(a) == "animal:Generic Animal:5"

def test_cat():
    c = Cat(3)
    c.set_name("Whiskers")
    assert c.get_age() == 3
    assert c.get_name() == "Whiskers"
    assert str(c) == "cat:Whiskers:3"
    c.speak()  # Should print "meow"

def test_person():
    p = Person("Alice", 30)
    p.add_friend("Bob")
    p.add_friend("Charlie")
    assert p.get_age() == 30
    assert p.get_name() == "Alice"
    assert p.get_friends() == ["Bob", "Charlie"]
    assert str(p) == "person:Alice:30"
    p.speak()  # Should print "hello"
def test_student():
    s = Student("Dave", 20, "Computer Science")
    s.add_friend("Eve")
    assert s.get_age() == 20
    assert s.get_name() == "Dave"
    assert s.major == "Computer Science"
    assert s.get_friends() == ["Eve"]
    assert str(s) == "student:Dave:20:Computer Science"
    s.speak()  # Should print one of the random messages

 

def test_all():
    test_animal()
    test_cat()
    test_person()
    test_student()

