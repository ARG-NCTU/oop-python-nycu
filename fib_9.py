
class Fibo(object):
    def cal(self,n):
        if n < 0:
            print("Incorrect input")
        elif n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.cal(n-1) + self.cal(n-2)

#a=Fibo()
#assert a.cal(10) == 55
#print(a.cal(10))
