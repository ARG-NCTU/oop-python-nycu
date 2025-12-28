import random
# from add_path import add_path
# add_path()

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
        return f"animal:{self.name}:{self.age}"


#################################
## Cat inherits from Animal
#################################

class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return f"cat:{self.name}:{self.age}"


#################################
## Person inherits from Animal
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
        diff = abs(self.age - other.age)
        print(diff, "year difference")

    def __str__(self):
        return f"person:{self.name}:{self.age}"


#################################
## Student inherits from Person
#################################

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
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


#################################
## Rabbit uses class variable & operator overloading
#################################

class Rabbit(Animal):
    tag = 1  # class variable

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
        # If same exact object, automatically equal
        if self is other:
            return True

        # If any parent is None, cannot compare family lines
        if (self.parent1 is None or self.parent2 is None or
            other.parent1 is None or other.parent2 is None):
            return False

        # Check parents same order
        parents_same = (self.parent1.rid == other.parent1.rid and
                        self.parent2.rid == other.parent2.rid)

        # Check parents reversed order
        parents_swapped = (self.parent1.rid == other.parent2.rid and
                           self.parent2.rid == other.parent1.rid)

        return parents_same or parents_swapped

    def __str__(self):
        return "rabbit:" + self.get_rid()
