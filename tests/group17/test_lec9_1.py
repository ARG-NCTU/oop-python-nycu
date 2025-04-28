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

print("✅ Animal tests passed!")
