import pytest
import random
class Person(object):
    '''Person Class 
    Attributes: name, age
    Methods: get_name, get_age, set_name, set_age, __str__
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self, newname=""):
        self.name = newname
    def set_age(self, newage):
        self.age = newage
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("hello")
        elif 0.25 <= r < 0.5:
            print("how are you?")
        elif 0.5 <= r < 0.75:
            print("goodbye")
        else:
            print("nice to meet you")
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

def test_student_initialization():
    student = Student("Alice", 20)
    assert student.get_name() == "Alice"
    assert student.get_age() == 20
    assert student.major is None
def test_student_with_major(): 
    student = Student("Bob", 22, "Computer Science")
    assert student.get_name() == "Bob"
    assert student.get_age() == 22
    assert student.major == "Computer Science"
def test_student_str():
    student = Student("Charlie", 21, "Mathematics")
    assert str(student) == "student:Charlie:21:Mathematics"
def test_student_change_major():
    student = Student("Dave", 23, "Physics")
    student.change_major("Chemistry")
    assert student.major == "Chemistry"
def test_student_speak():
    student = Student("Eve", 19)
    # Check that speak method runs without error
    student.speak()
def test_student_set_name():
    student = Student("Frank", 25)
    student.set_name("George")
    assert student.get_name() == "George"
def test_student_set_age():
    student = Student("Hannah", 24)
    student.set_age(26)
    assert student.get_age() == 26
def test_student_set_major():
    student = Student("Ivy", 18)
    student.change_major("Biology")
    assert student.major == "Biology"