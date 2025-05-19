import random
#################################
## Animal abstract data type
#################################
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

def test_Animal():
    a = Animal(4)
    assert str(a) == "animal:None:4"
    assert a.get_age() == 4
    a.set_name("fluffy")
    assert str(a) == "animal:fluffy:4"
    a.set_name()
    assert str(a) == "animal::4"

#################################
## Inheritance example
#################################
class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)

def test_Cat():
    c = Cat(5)
    c.set_name("fluffy")
    assert str(c) == "cat:fluffy:5"
    c.speak()
    assert c.get_age() == 5

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
    def __str__(self): # print / 使用字串都會呼叫此函式
        return "person:"+str(self.name)+":"+str(self.age)

def test_Person():
    p1 = Person("jack", 30)
    p2 = Person("jill", 25)
    assert p1.get_name() == "jack"
    assert p1.get_age() == 30
    assert p2.get_name() == "jill"
    assert p2.get_age() == 25
    assert str(p1) == "person:jack:30"

#################################
## Inheritance example
#################################
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
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

def test_Student():
    s1 = Student("alice", 20, "CS")
    s2 = Student("bob", 18)
    assert str(s1) == "student:alice:20:CS"
    assert str(s2) == "student:bob:18:None"
    s1.change_major("Math")
    assert str(s1) == "student:alice:20:Math"
    s1.speak()
    s2.speak()

#################################
## Use of class variables
#################################
class Rabbit(Animal):
    # a class variable, tag, shared across all instances
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        # zfill used to add leading zeroes 001 instead of 1
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)
    def __eq__(self, other):
        if self.parent1 is None or self.parent2 is None or other.parent1 is None or other.parent2 is None:
            return False
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
                           and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite
    def __str__(self):
        return "rabbit:"+ self.get_rid()

def test_creating_rabbits():
    r1 = Rabbit(3) # tag = 1
    r2 = Rabbit(4) # tag = 2
    r3 = Rabbit(5) # tag = 3
    assert str(r1) == "rabbit:001"
    assert str(r2) == "rabbit:002"
    assert str(r3) == "rabbit:003"
    assert r1.get_parent1() == None

def test_rabbit_addition():
    r1 = Rabbit(3) # 跟前面不同function，但如果都會執行，tag的累加會接續而不會重新從1開始, tag = 4
    r2 = Rabbit(4) # tag = 5
    r3 = Rabbit(5) # tag = 6
    r4 = r1 + r2 # r4.age = 0, parent1 = r1, parent2 = r2, tag = 7
    assert str(r4) == "rabbit:007"
    assert str(r4.get_parent1()) == str(r1)
    assert str(r4.get_parent2()) == str(r2)
    r5 = r3 + r4
    r6 = r4 + r3
    assert str(r3) == "rabbit:006"
    assert str(r4) == "rabbit:007"
    assert str(r5) == "rabbit:008"
    assert str(r6) == "rabbit:009"
    assert str(r5.get_parent1()) == str(r3)
    assert str(r5.get_parent2()) == str(r4)
    assert str(r6.get_parent1()) == str(r4)
    assert str(r6.get_parent2()) == str(r3)
