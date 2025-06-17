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

class Bird(Animal):
    def speak(self):
        return f"{self.name} chirps"
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

def test_bird_speak():
    bird = Bird("Tweety")
    assert bird.speak() == "Tweety chirps"

def test_isinstance_relationship():
    dog = Dog("Rocky")
    cat = Cat("Mimi")
    assert isinstance(dog, Animal)
    assert isinstance(cat, Animal)
    assert not isinstance(dog, Cat)
def test_animal_class():
    animal = Animal("Leo")
    assert animal.name == "Leo"
    assert animal.speak() == "Leo makes a sound"
def test_dog_class():
    dog = Dog("Rex")
    assert dog.name == "Rex"
    assert dog.speak() == "Rex barks"
def test_cat_class():
    cat = Cat("Whiskers")
    assert cat.name == "Whiskers"
    assert cat.speak() == "Whiskers meows"
def test_bird_class():
    bird = Bird("Chirpy")
    assert bird.name == "Chirpy"
    assert bird.speak() == "Chirpy chirps"

def test_all():
    test_animal_speak()
    test_dog_speak()
    test_cat_speak()
    test_bird_speak()
    test_isinstance_relationship()
    test_animal_class()
    test_dog_class()
    test_cat_class()
    test_bird_class()
