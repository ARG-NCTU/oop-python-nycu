print("\n==== Running test cases ====")
# Test Person
p = Person("john", 40)
assert p.get_name() == "john"
assert p.get_age() == 40
p.add_friend("mike")
p.add_friend("susan")
p.add_friend("mike")  # should not duplicate
assert p.get_friends() == ["mike", "susan"]
assert str(p) == "person:john:40"
print("✅ Person tests passed!")
