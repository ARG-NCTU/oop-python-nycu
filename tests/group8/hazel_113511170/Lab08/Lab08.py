import time

name = ["john doe", "jane smith", "bob johnson"]
number = 0
for person in name:
    first_last_name = person.split()
    if len(first_last_name) == 2:
        print(first_last_name[0] + " " + first_last_name[1])
        number += 1
    time.sleep(1)
print("total: " + str(number))