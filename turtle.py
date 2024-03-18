x,y=0,0
for i in range(999):
    print("The turtle Pos is at["+str(x)+","+str(y)+"]")
    motion=input()
    if motion=="left":
        x-=1
    elif motion=="right":
        x+=1
    elif motion=="up":
        y+=1
    elif motion=="down":
        y-=1
    elif motion=="end":
        print("turtle: (die)")
        break
    else :
        print("turtle: hi")

