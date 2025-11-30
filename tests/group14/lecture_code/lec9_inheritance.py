import random


"""
lec9_inheritance.py

示範繼承 (inheritance) 的多個例子：
- `Animal` 為基底類別，包含年齡與名稱屬性與基本存取與表示方法。
- `Cat`、`Person`、`Student`、`Rabbit` 等類別示範如何從 `Animal` 繼承並擴充行為。

注意：本檔包含許多示範用的 `print` 與即時測試程式片段，
這些會在模組被 import 時執行（例如在 pytest 匯入模組時），
若不希望匯入時執行示範程式，建議把示範程式碼放入
`if __name__ == "__main__":` 下。
"""


#################################
## Animal 抽象資料型別（基底類別）
#################################
class Animal(object):
    """Animal 基底類別

    屬性：
    - age: 年齡
    - name: 名稱（預設 None）

    方法：基本的存取器與字串表示，用於子類別繼承。
    """
    def __init__(self, age):
        # 建構子：設定年齡，名稱預設為 None
        self.age = age
        self.name = None
    def get_age(self):
        # 回傳年齡
        return self.age
    def get_name(self):
        # 回傳名稱（可能為 None 或空字串）
        return self.name
    def set_age(self, newage):
        # 設定年齡
        self.age = newage
    def set_name(self, newname=""):
        # 設定名稱（預設空字串）
        self.name = newname
    def __str__(self):
        # 字串表示，子類別通常會覆寫此方法
        return "animal:"+str(self.name)+":"+str(self.age)
        
print("\n---- animal tests ----")
a = Animal(4)
print(a)
print(a.get_age())
a.set_name("fluffy")
print(a)
a.set_name()
print(a)

#################################
## Inheritance example 
#################################
class Cat(Animal):
    """Cat 繼承自 Animal，示範簡單的覆寫與新增方法。"""
    def speak(self):
        # Cat 的行為：發出喵叫
        print("meow")
    def __str__(self):
        # 覆寫字串表示，顯示為 cat:name:age
        return "cat:"+str(self.name)+":"+str(self.age)
    
print("\n---- cat tests ----")
c = Cat(5)
c.set_name("fluffy")
print(c)
c.speak()
print(c.get_age())

#################################
## Inheritance example
#################################
class Person(Animal):
    """Person 也是從 Animal 繼承，並示範如何在子類別加入自己的屬性與方法。"""
    def __init__(self, name, age):
        # 呼叫基底類別的建構子來設定 age
        Animal.__init__(self, age)
        # 使用 set_name 初始化 name
        self.set_name(name)
        # Person 特有的欄位：朋友清單
        self.friends = []
    def get_friends(self):
        # 回傳朋友清單
        return self.friends
    def speak(self):
        # Person 的說話方式
        print("hello")
    def add_friend(self, fname):
        # 加入朋友（避免重複）
        if fname not in self.friends:
            self.friends.append(fname)
    def age_diff(self, other):
        # 計算年齡差並印出絕對值
        diff = self.age - other.age
        print(abs(diff), "year difference")
    def __str__(self):
        # 覆寫字串表示
        return "person:"+str(self.name)+":"+str(self.age)

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

#################################
## Inheritance example
#################################
class Student(Person):
    """Student 繼承自 Person，示範覆寫 __str__ 與新增屬性（major）。"""
    def __init__(self, name, age, major=None):
        # 呼叫 Person 的建構子設定 name 與 age
        Person.__init__(self, name, age)
        # Student 特有欄位：主修科目
        self.major = major
    def __str__(self):
        # 顯示 student:name:age:major
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
    def change_major(self, major):
        # 變更主修
        self.major = major
    def speak(self):
        # 覆寫 speak，使用隨機輸出做示範（教學用途）
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")

print("\n---- student tests ----")
s1 = Student('alice', 20, "CS")
s2 = Student('beth', 18)
print(s1)
print(s2)
print(s1.get_name(),"says:", end=" ")
s1.speak()
print(s2.get_name(),"says:", end=" ")
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
    # 在 Rabbit Class 中，一個更嚴謹的、基於父母的 __eq__
    def __eq__(self, other):
        # 確保比較的對象也是 Rabbit
        if not isinstance(other, Rabbit):
            return NotImplemented

        # 處理雙方都沒有父母的情況
        self_no_parents = self.parent1 is None or self.parent2 is None
        other_no_parents = other.parent1 is None or other.parent2 is None
        if self_no_parents and other_no_parents:
            # 如果都沒有父母，比較牠們自己的 rid
            return self.rid == other.rid
        if self_no_parents or other_no_parents:
            # 如果一方有父母，一方沒有，那肯定不相等
            return False

        # 現在，雙方都有父母，執行你原來的邏輯
        parents_same = self.parent1.rid == other.parent1.rid \
                    and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
                        and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite

    def __str__(self):
        return "rabbit:"+ self.get_rid()

print("\n---- rabbit tests ----")
print("---- testing creating rabbits ----")
r1 = Rabbit(3)
r2 = Rabbit(4)
r3 = Rabbit(5)
print("r1:", r1)
print("r2:", r2)
print("r3:", r3)
print("r1 parent1:", r1.get_parent1())
print("r1 parent2:", r1.get_parent2())

print("---- testing rabbit addition ----")
r4 = r1+r2   # r1.__add__(r2)
print("r1:", r1)
print("r2:", r2)
print("r4:", r4)
print("r4 parent1:", r4.get_parent1())
print("r4 parent2:", r4.get_parent2())

print("---- testing rabbit equality ----")
r5 = r3+r4
r6 = r4+r3
print("r3:", r3)
print("r4:", r4)
print("r5:", r5)
print("r6:", r6)
print("r5 parent1:", r5.get_parent1())
print("r5 parent2:", r5.get_parent2())
print("r6 parent1:", r6.get_parent1())
print("r6 parent2:", r6.get_parent2())
print("r5 and r6 have same parents?", r5 == r6)
print("r4 and r6 have same parents?", r4 == r6)
    

