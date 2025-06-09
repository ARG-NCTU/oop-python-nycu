print("\n==== Running test cases ====")

# Test Animal
a = Animal(2)
assert a.get_age() == 2
assert a.get_name() is None
a.set_name("buddy")
assert a.get_name() == "buddy"
a.set_age(3)
assert a.get_age() == 3
assert str(a) == "animal:buddy:3"

# Test Cat
c = Cat(1)
c.set_name("whiskers")
assert c.get_name() == "whiskers"
assert c.get_age() == 1
assert str(c) == "cat:whiskers:1"

# Test Person
p = Person("john", 40)
assert p.get_name() == "john"
assert p.get_age() == 40
p.add_friend("mike")
p.add_friend("susan")
p.add_friend("mike")  # should not duplicate
assert p.get_friends() == ["mike", "susan"]
assert str(p) == "person:john:40"

# Test Student
s = Student("tom", 21, "Math")
assert s.get_name() == "tom"
assert s.get_age() == 21
assert str(s) == "student:tom:21:Math"
s.change_major("CS")
assert str(s) == "student:tom:21:CS"

# Test Rabbit unique IDs and addition
Rabbit.tag = 1  # reset tag to ensure consistent test
r1 = Rabbit(2)
r2 = Rabbit(3)
r3 = Rabbit(4)
assert r1.get_rid() == "001"
assert r2.get_rid() == "002"
assert r3.get_rid() == "003"

r4 = r1 + r2
assert r4.get_age() == 0
assert isinstance(r4.get_parent1(), Rabbit)
assert r4.get_parent1() == r1
assert r4.get_parent2() == r2

r5 = r3 + r4
r6 = r4 + r3
assert r5 == r6  # same parents in different order
assert not (r4 == r6)  # different parents

print("✅ All tests passed!")

