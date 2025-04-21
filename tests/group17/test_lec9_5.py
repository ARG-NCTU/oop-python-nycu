print("\n==== Running test cases ====")
#Test Rabbit unique IDs and addition
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

print("✅ Rabbit tests passed!")
