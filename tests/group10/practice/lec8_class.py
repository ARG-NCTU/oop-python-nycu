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
    
def main():
    point1=coordinate(3,4)
    point2=coordinate(0,0)
    print(point1)
    print(point2)
    print(point1.distance(point2))
    
if __name__ == "__main__":
    main()