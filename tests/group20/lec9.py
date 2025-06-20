import random

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

class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)

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

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, change_major(self, major):
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

class Rabbit(Animal):
    tag = 1
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
        if self.parent1 is None or self.parent2 is None or other.parent1 is None or other.parent2 is None:
            return False
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite
    def __str__(self):
        return "rabbit:" + self.get_rid()
</xArtifact>

**說明**：
- **保留**：`Animal`, `Cat`, `Person`, `Student`, `Rabbit` 的所有方法，原始邏輯和名稱不變。
- **移除**：所有範例程式碼（例如 `a = Animal(4)`, `r4 = r1 + r2`）。
- **依賴**：保留 `import random`。
- **命名**：檔案命名為 `lec9.py`，符合你的 `lecn.py` 慣例。
- **不調整**：未添加輸入驗證（例如 `set_age` 的負數檢查），因為無明確要求。

---

### 4. 測試程式碼：`test_lec9.py`
以下是測試所有類別和方法的程式碼，使用 `from lec9 import ...`，加入 `add_path` 確保路徑正確，涵蓋正常、邊界和異常情況。由於 `Student.speak` 使用隨機輸出，我會使用模擬（mocking）來控制測試。

<xaiArtifact artifact_id="acb0a0c3-7f7e-46b7-9061-b57bc7e5b435" artifact_version_id="a092f607-bcee-4067-a6d2-92acc86a89e3" title="test_lec9.py" contentType="text/python">
import pytest
import add_path  # Ensure module path is correct
from lec9 import Animal, Cat, Person, Student, Rabbit
from unittest.mock import patch

def test_animal():
    a = Animal(4)
    assert a.get_age() == 4
    assert a.get_name() is None
    a.set_name("fluffy")
    assert a.get_name() == "fluffy"
    a.set_age(5)
    assert a.get_age() == 5
    a.set_name()
    assert a.get_name() == ""
    assert str(a) == "animal::5"

def test_cat(capsys):
    c = Cat(5)
    c.set_name("fluffy")
    assert str(c) == "cat:fluffy:5"
    c.speak()
    captured = capsys.readouterr()
    assert captured.out == "meow\n"
    assert c.get_age() == 5
    assert c.get_name() == "fluffy"

def test_person(capsys):
    p1 = Person("jack", 30)
    p2 = Person("jill", 25)
    assert p1.get_name() == "jack"
    assert p1.get_age() == 30
    assert p2.get_name() == "jill"
    assert p2.get_age() == 25
    assert str(p1) == "person:jack:30"
    p1.speak()
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    p1.age_diff(p2)
    captured = capsys.readouterr()
    assert captured.out == "5 year difference\n"
    p1.add_friend("jill")
    assert p1.get_friends() == ["jill"]
    p1.add_friend("jill")  # Duplicate, no effect
    assert p1.get_friends() == ["jill"]

def test_student(capsys):
    s1 = Student("alice", 20, "CS")
    s2 = Student("beth", 18)
    assert str(s1) == "student:alice:20:CS"
    assert str(s2) == "student:beth:18:None"
    s1.change_major("Math")
    assert str(s1) == "student:alice:20:Math"
    with patch('random.random', side_effect=[0.1, 0.3, 0.6, 0.9]):
        s1.speak()
        captured = capsys.readouterr()
        assert captured.out == "i have homework\n"
        s1.speak()
        captured = capsys.readouterr()
        assert captured.out == "i need sleep\n"
        s1.speak()
        captured = capsys.readouterr()
        assert captured.out == "i should eat\n"
        s1.speak()
        captured = capsys.readouterr()
        assert captured.out == "i am watching tv\n"

def test_rabbit():
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r3 = Rabbit(5)
    assert str(r1) == "rabbit:001"
    assert str(r2) == "rabbit:002"
    assert str(r3) == "rabbit:003"
    assert r1.get_parent1() is None
    assert r1.get_parent2() is None
    r4 = r1 + r2
    assert str(r4) == "rabbit:004"
    assert r4.get_parent1() == r1
    assert r4.get_parent2() == r2
    assert r4.get_age() == 0
    r5 = r3 + r4
    r6 = r4 + r3
    assert r5 == r6  # Same parents (order swapped)
    assert r4 != r6  # Different parents
