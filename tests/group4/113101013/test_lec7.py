# === Lecture Code (自包含版) ===

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

# === Tests ===

def test_animal_speak():
    generic = Animal("Unknown")
    assert generic.speak() == "Unknown makes a sound"

def test_dog_speak():
    dog = Dog("Buddy")
    assert dog.speak() == "Buddy barks"

def test_cat_speak():
    cat = Cat("Kitty")
    assert cat.speak() == "Kitty meows"

def test_isinstance_relationship():
    dog = Dog("Rocky")
    cat = Cat("Mimi")
    assert isinstance(dog, Animal)
    assert isinstance(cat, Animal)
    assert not isinstance(dog, Cat)
