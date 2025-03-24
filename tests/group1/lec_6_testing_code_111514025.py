times = 0

def honi(n, fr, to, spare):
    global times
    times = 0  # Reset times for each call

    def printMove(fr, to):
        print('move from ' + str(fr) + ' to ' + str(to))

    def Towers(n, fr, to, spare):
        global times  # Declare that we want to modify the global variable `times`
        if n == 1:
            printMove(fr, to)
            times += 1  # Increment the global `times`
        else:
            Towers(n-1, fr, spare, to) 
            Towers(1, fr, to, spare) 
            Towers(n-1, spare, to, fr) 
    
    Towers(n, fr, to, spare)
    print("if n =", n, ", need to doing", times, "times.")

honi(4, 'P1', 'P2', 'P3')
honi(1, 'P1', 'P2', 'P3')
honi(2, 'P1', 'P2', 'P3')
honi(5, 'P1', 'P2', 'P3')

# 恩, 之前計概課lab寫過