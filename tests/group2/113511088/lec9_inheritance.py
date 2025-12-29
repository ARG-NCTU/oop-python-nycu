# -*- coding: utf-8 -*-
import random

#################################
## Animal abstract data type
#################################
class Animal(object):
    """Animal Class
    Attributes: age, name
    Methods: get_age, get_name, set_age, set_name, __str__
    """
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


#################################
## Inheritance example
#################################
class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)


#################################
## Inheritance example
#################################
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
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
        diff = self.age - other.age
        print(abs(diff), "year difference")

    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)


#################################
## Inheritance example
#################################
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def __str__(self):
        return "student:" + str(self.name) + ":" + str(self.age) + ":" + str(self.major)

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")


#################################
## Use of class variables
#################################
class Rabbit(Animal):
    tag = 1  # class variable shared across instances

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
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
        if (self.parent1 is None or self.parent2 is None or
            other.parent1 is None or other.parent2 is None):
            return False

        parents_same = (self.parent1.rid == other.parent1.rid and
                        self.parent2.rid == other.parent2.rid)
        parents_opposite = (self.parent2.rid == other.parent1.rid and
                            self.parent1.rid == other.parent2.rid)
        return parents_same or parents_opposite

    def __str__(self):
        return "rabbit:" + self.get_rid()


if __name__ == "__main__":
    # Demo (optional; pytest import won't run this)
    print("\n---- animal tests ----")
    a = Animal(4)
    print(a)
    print(a.get_age())
    a.set_name("fluffy")
    print(a)
    a.set_name()
    print(a)

    print("\n---- cat tests ----")
    c = Cat(5)
    c.set_name("fluffy")
    print(c)
    c.speak()
    print(c.get_age())

    print("\n---- person tests ----")
    p1 = Person("jack", 30)
    p2 = Person("jill", 25)
    print(p1.get_name())
    print(p1.get_age())
    print(p2.get_name())
    print(p2.get_age())
    print(p1)
    p1.speak()
    p1.age_diff(p2)

    print("\n---- student tests ----")
    s1 = Student('alice', 20, "CS")
    s2 = Student('beth', 18)
    print(s1)
    print(s2)
    print(s1.get_name(), "says:", end=" ")
    s1.speak()
    print(s2.get_name(), "says:", end=" ")
    s2.speak()

    print("\n---- rabbit tests ----")
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r4 = r1 + r2
    print(r1, r2, r4)
