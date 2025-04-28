#####################################
# EXAMPLE:  Towers of Hanoi
#####################################

# 定義如何顯示移動的過程
def tower(n,fr ,to ,spare):
    moves = []    

    def move(n,fr ,to ,spare):
        if n == 1:
            moves.append((fr ,to))
        else:
            #step 1 : 將n-1個從p1移到p3
            move(n-1 , fr , spare , to)
            #step 2 : 將最下面那一個從p1移到p2
            moves.append((fr ,to))
            #step 3 : 將n-1個從p3移到p2
            move(n-1 , spare , to ,fr)
    
    move(n,fr ,to ,spare)
    return moves
print(tower(5,"p1","p2","p3"))


#####################################
# EXAMPLE:  fibonacci
#####################################
def fib2(x):
    if x == 0 or x==1: #F(0)=0 F(1)=1
        return x
    
    else:
        x = fib2(x-1)+fib2(x-2)
        return x
fib_num = []
for i in range(20):
    fib_num.append(fib2(i))
    print(f"F({i})={fib2(i)}")
print(fib_num)