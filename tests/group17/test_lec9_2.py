print("\n==== Running test cases ====")
c = Cat(1)
c.set_name("whiskers")
assert c.get_name() == "whiskers"
assert c.get_age() == 1
assert str(c) == "cat:whiskers:1"
print("✅ Cat tests passed!")
