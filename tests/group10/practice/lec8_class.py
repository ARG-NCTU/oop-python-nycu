class coordinate():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __str__(self):
        return "(x,y) = (" + str(self.x) + "," + str(self.y) + ")"
    
    def distance(self,other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

class fraction():
    def __init__(self,num,denom):
        self.num=num
        self.denom=denom
        self.reduce()
        
    def __str__(self):
        return str(self.num) + "/" + str(self.denom)
    
    def __add__(self,other):
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return fraction(top,bott)
    
    def __sub__(self,other):
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return fraction(top,bott)
    
    def __mul__(self,other):
        top = self.num*other.num
        bott = self.denom*other.denom
        return fraction(top,bott)
    
    def __truediv__(self,other):
        top = self.num*other.denom
        bott = self.denom*other.num
        return fraction(top,bott)
    
    def __float__(self):
        return self.num/self.denom
    
    def inverse(self):
        return fraction(self.denom,self.num)
    
    def reduce(self):
        def gcd(a,b):
            if b==0:
                return a
            else:
                return gcd(b,a%b)
        common=gcd(self.num,self.denom)
        return fraction(self.num//common,self.denom//common)
    
    
    
    
def coor_main():
    point1=coordinate(3,4)
    point2=coordinate(0,0)
    print(point1)
    print(point2)
    print(point1.distance(point2))
    
def frac_main():
    f1=fraction(1,4)
    f2=fraction(1,2)
    print(f1)
    print(f2)
    print(f1+f2)
    print(f1-f2)
    print(f1*f2)
    print(f1/f2)
    print(float(f1))
    print(f1.inverse())
    
if __name__ == "__main__":
    frac_main()