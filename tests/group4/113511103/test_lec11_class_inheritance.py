class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"My name is {self.name}"

class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def speak(self):
        return f"I'm {self.name} and I study {self.major}"

# 測試區段

def test_person_speak():
    p = Person("Alice")
    assert p.speak() == "My name is Alice"

def test_student_speak():
    s = Student("Bob", "CS")
    assert isinstance(s, Person)
    assert s.name == "Bob"
    assert s.major == "CS"
    assert s.speak() == "I'm Bob and I study CS"
