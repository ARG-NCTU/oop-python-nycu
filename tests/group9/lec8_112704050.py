class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"<{str(self.x)} , {str(self.y)}>"
    def __add__(self,other):
        return Coordinate(self.x + other.x , self.y + other.y)
    def __sub__(self,other):
        return Coordinate(self.x - other.x , self.y - other.y)
    def __mul__(self,other):
        return Coordinate(self.x * other.x , self.y * other.y)
    def __truediv__(self,other):
        return Coordinate(self.x / other.x , self.y / other.y)
    def __float__(self):
        return (self.x + self.y)**0.5
    def distance(self,other):
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        return(x_diff**2 + y_diff**2)**0.5
    def vector(self,other):
        return f"<{self.x - other.x},{self.y - other.y}>"
    
try:
    a = Coordinate(3, 4)
    b = Coordinate(-3, -4)
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    print(c)
    print(d)
    print(e)
    print(f)
    print(float(a))
    print(a.distance(b))
    print(Coordinate.distance(a,b))
    print(a.vector(b))
    print(Coordinate.vector(b,a))
except ZeroDivisionError:
    print("分母為0")

####class Vendingmachine practice####
class Vendingmachine:
    def __init__(self, cash):
        self.inventory = {"Coke": 10, "Pepsi": 10, "Sprite": 10}
        self.price = {"Coke": 25, "Pepsi": 20, "Sprite": 15}
        self.dollar = cash

    #def __str__(self):
        #return f"{self.name}: {self.dollar}"
    
    #def __sub__(self, other):
        #return Vendingmachine(self.dollar - other.price)
    """
    def buy_flow(self):
        print("Welcome to the vending machine!")
        print(f"Your current cassh is: ${self.dollar}")
        print("Here are the available items:")
        
            
        while True:
            for item in self.inventory:
                print(f"{item}: {self.inventory[item]} available at ${self.price[item]} each")
            
            item = input("Please enter the item you want to buy: ")
            try:
                num = int(input("Please enter the quantity you want to buy: "))
                
                if self.inventory[item] < num:
                    print("Not enough stock. Please try again.")
                    continue
                elif self.dollar < self.price[item] * num:
                    print("Insufficient Cash. Please try again.")
                    continue  # 回到 while 迴圈頂端，重新輸入
                else:
                    self.inventory[item] -= num
                    self.dollar -= self.price[item] * num
                    print(f"Successfully purchased {num} {item}(s). Remaining cash: {self.dollar}")
                    answer = input("Do you want to continue? (yes/no): ")
                    if answer.lower() == "no":
                        print("Thank you for using the vending machine!")
                        break
                    else:
                        print("Here are the available items:")
                        continue
                   
            except KeyError:
                print("Invalid item. Please try again.")
            except ValueError:
                print("Invalid quantity. Please try again.")
    """
    def buy(self, item, num):
        if item not in self.inventory:
            return "Invalid item."
        if self.inventory[item] < num:
            return "Not enough stock."
        if self.dollar < self.price[item] * num:
            return "Insufficient Cash."

        self.inventory[item] -= num
        self.dollar -= self.price[item] * num
        return f"Successfully purchased {num} {item}(s). Remaining cash: {self.dollar}"

#vm = Vendingmachine(100)
#vm.buy_flow()