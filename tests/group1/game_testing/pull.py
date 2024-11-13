#get user input the number
pull = 30
sac = 0
total = 0
for i in range(8):
    total += (pull+sac)*3
    sac = (pull+sac) * 50 // 100
    print(total)
