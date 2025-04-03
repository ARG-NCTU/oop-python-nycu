class Animal:
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


def test_animal_basic():
    a = Animal(3)
    a.set_name("Fluffy")
    assert a.get_age() == 3
    assert a.get_name() == "Fluffy"
    assert str(a) == "animal:Fluffy:3"
