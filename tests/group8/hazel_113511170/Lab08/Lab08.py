import time

name = ["john doe", "jane smith", "bob johnson"]
x = 0
for person in name:
    y = person.split()
    if len(y) == 2:
        print(y[0] + " " + y[1])
        x += 1
    time.sleep(1)
print("total: " + str(x))