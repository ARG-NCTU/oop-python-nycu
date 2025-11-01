import random
from lec9_inheritance import Animal, Cat, Person, Student, Rabbit

# -----------------
# 測試 Animal
# -----------------
def test_animal():
    a = Animal(4)
    assert str(a) == "animal:None:4"
    assert a.get_age() == 4
    
    a.set_name("fluffy")
    assert str(a) == "animal:fluffy:4"
    assert a.get_name() == "fluffy"
    
    a.set_name() # 測試預設值
    assert str(a) == "animal::4"
    assert a.get_name() == ""

# -----------------
# 測試 Cat
# `capsys` 是 pytest 的一個內建工具，用來抓取 print() 的輸出
# -----------------
def test_cat(capsys):
    c = Cat(5)
    c.set_name("fluffy")
    assert str(c) == "cat:fluffy:5"
    assert c.get_age() == 5
    
    c.speak()
    captured = capsys.readouterr() # 抓取 print 內容
    assert captured.out == "meow\n"

# -----------------
# 測試 Person
# -----------------
def test_person(capsys):
    p1 = Person("jack", 30)
    p2 = Person("jill", 25)
    
    assert p1.get_name() == "jack"
    assert p1.get_age() == 30
    assert str(p1) == "person:jack:30"
    
    p1.speak()
    captured_speak = capsys.readouterr()
    assert captured_speak.out == "hello\n"
    
    p1.age_diff(p2)
    captured_diff = capsys.readouterr()
    assert captured_diff.out == "5 year difference\n"

def test_person_friends():
    p1 = Person("jack", 30)
    assert p1.get_friends() == []
    p1.add_friend("jill")
    assert p1.get_friends() == ["jill"]
    p1.add_friend("jill") # 測試重複加入
    assert p1.get_friends() == ["jill"]

# -----------------
# 測試 Student
# -----------------
def test_student_init():
    s1 = Student('alice', 20, "CS")
    s2 = Student('beth', 18)
    assert str(s1) == "student:alice:20:CS"
    assert str(s2) == "student:beth:18:None"

def test_student_change_major():
    s1 = Student('alice', 20, "CS")
    s1.change_major("History")
    assert s1.major == "History"
    assert str(s1) == "student:alice:20:History"

def test_student_speak(capsys):
    s1 = Student('alice', 20, "CS")
    
    # 為了讓 random() 的結果可預測，我們設定一個「種子」
    random.seed(42) # 播種
    
    # 第一次呼叫 random.random() (seed 42) 會回傳 0.639... (落在 "i should eat")
    s1.speak()
    captured = capsys.readouterr()
    assert captured.out == "i should eat\n"
    
    # 第二次呼叫會回傳 0.025... (落在 "i have homework")
    s1.speak()
    captured = capsys.readouterr()
    assert captured.out == "i have homework\n"

# -----------------
# 測試 Rabbit
# -----------------
def test_rabbit_creation():
    # 為了確保 ID 可預測，我們在每次測試時都重置 class 變數
    Rabbit.tag = 1 
    
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r3 = Rabbit(5)
    
    assert str(r1) == "rabbit:001"
    assert str(r2) == "rabbit:002"
    assert str(r3) == "rabbit:003"
    assert r1.get_rid() == "001"
    assert r1.get_parent1() is None
    assert r1.get_parent2() is None

def test_rabbit_addition():
    Rabbit.tag = 1 # 重置
    
    r1 = Rabbit(3) # ID 1
    r2 = Rabbit(4) # ID 2
    r4 = r1 + r2   # 應該會建立 ID 3 的新兔子
    
    assert str(r4) == "rabbit:003"
    assert r4.get_age() == 0
    assert r4.get_parent1() is r1
    assert r4.get_parent2() is r2
    assert str(r4.get_parent1()) == "rabbit:001"
    assert str(r4.get_parent2()) == "rabbit:002"

def test_rabbit_equality():
    Rabbit.tag = 1 # 重置
    
    r1 = Rabbit(3) # ID 1
    r2 = Rabbit(4) # ID 2
    r3 = Rabbit(5) # ID 3
    
    r4 = r1 + r2 # ID 4 (父母: r1, r2)
    r5 = r3 + r4 # ID 5 (父母: r3, r4)
    r6 = r4 + r3 # ID 6 (父母: r4, r3)
    
    # r5 和 r6 的父母相同，只是順序顛倒
    assert (r5 == r6) is True
    
    # 檢查和 r4 (父母是 r1, r2) 比較
    assert (r5 == r4) is False

def test_rabbit_equality_no_parents():
    Rabbit.tag = 1 # 重置
    
    r1 = Rabbit(3) # ID 1 (無父母)
    r2 = Rabbit(4) # ID 2 (無父母)
    
    # 根據 __eq__ 的定義，沒有父母的兔子彼此不相等
    assert (r1 == r2) is False