class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)

class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)

class Person(Animal):
    def __init__(self, name, age):
        super().__init__(age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("hello")

    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")

    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)

class Student(Person):
    def __init__(self, name, age, major=None):
        super().__init__(name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        print("I am a student")

    def __str__(self):
        return "student:" + str(self.name) + ":" + str(self.age)

class Rabbit(Animal):
    tag = 27  # class variable for unique IDs

    def __init__(self, age, parent1=None, parent2=None):
        super().__init__(age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return f"{self.rid:03d}"

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        return Rabbit(0, self, other)

    def __eq__(self, other):
        # Check if same object (identity)
        if self is other:
            return True
        # If either rabbit has no parents, they can only be equal if they're the same object (checked above)
        if self.parent1 is None or self.parent2 is None or \
           other.parent1 is None or other.parent2 is None:
            return False
        # Check if parents match (in either order)
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent1.rid == other.parent2.rid and self.parent2.rid == other.parent1.rid
        return parents_same or parents_opposite

    def __str__(self):
        if self.name is not None:
            return "rabbit:" + str(self.name) + ":" + str(self.age)
        return "rabbit:" + self.get_rid()
