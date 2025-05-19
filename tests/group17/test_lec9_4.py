print("\n==== Running test cases ====")
# Test Student
s = Student("tom", 21, "Math")
assert s.get_name() == "tom"
assert s.get_age() == 21
assert str(s) == "student:tom:21:Math"
s.change_major("CS")
assert str(s) == "student:tom:21:CS"
print("✅ Student tests passed!")
