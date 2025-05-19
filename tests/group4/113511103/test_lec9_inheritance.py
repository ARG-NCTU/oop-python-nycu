class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow"

# 以下為 pytest 測試
def test_animal_speak():
    a = Animal("Generic")
    assert a.name == "Generic"
    assert a.speak() == "..."

def test_dog_speak():
    d = Dog("Fido")
    assert isinstance(d, Animal)
    assert d.name == "Fido"
    assert d.speak() == "Woof!"

def test_cat_speak():
    c = Cat("Kitty")
    assert isinstance(c, Animal)
    assert c.name == "Kitty"
    assert c.speak() == "Meow"
