import random

# NOTE: Commented out local dependency to ensure script runs standalone.
# from add_path import add_path
# add_path()

# ==============================================================================
# 1. Base Class: Animal 🐾
# ==============================================================================

class Animal:
    """
    Abstract Data Type for an Animal.
    Attributes: age, name
    """
    def __init__(self, age: int):
        self.age = age
        self.name = None

    def get_age(self) -> int:
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newage: int):
        self.age = newage

    def set_name(self, newname: str = ""):
        self.name = newname

    def __str__(self):
        return f"animal:{self.name}:{self.age}"


# ==============================================================================
# 2. Inheritance: Cat 🐱
# ==============================================================================

class Cat(Animal):
    """
    Cat inherits from Animal.
    Demonstrates polymorphism (speak method).
    """
    def speak(self):
        print("meow")

    def __str__(self):
        return f"cat:{self.name}:{self.age}"


# ==============================================================================
# 3. Inheritance: Person 👤
# ==============================================================================

class Person(Animal):
    """
    Person inherits from Animal.
    Adds 'friends' list and specific behavior.
    """
    def __init__(self, name: str, age: int):
        # Use super() to initialize the parent class
        super().__init__(age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def speak(self):
        print(f"Hello, my name is {self.name}!")

    def add_friend(self, fname: str):
        if fname not in self.friends:
            self.friends.append(fname)

    def age_diff(self, other: 'Person'):
        diff = abs(self.age - other.age)
        print(f"{diff} year difference between {self.name} and {other.name}")

    def __str__(self):
        return f"person:{self.name}:{self.age}"


# ==============================================================================
# 4. Inheritance: Student 🎓
# ==============================================================================

class Student(Person):
    """
    Student inherits from Person.
    Demonstrates overriding methods (speak).
    """
    def __init__(self, name: str, age: int, major: str = None):
        super().__init__(name, age)
        self.major = major

    def change_major(self, major: str):
        self.major = major

    def speak(self):
        # Student specific speech logic
        r = random.random()
        if r < 0.25:
            print("I have homework... 📚")
        elif r < 0.5:
            print("I need sleep... 😴")
        elif r < 0.75:
            print("I should eat... 🍕")
        else:
            print("I am watching TV... 📺")

    def __str__(self):
        return f"student:{self.name}:{self.age}:{self.major}"


# ==============================================================================
# 5. Advanced: Rabbit (Class Variables & Operator Overloading) 🐰
# ==============================================================================

class Rabbit(Animal):
    """
    Rabbit class demonstrates:
    1. Class Variables (tag) to create unique IDs.
    2. Operator Overloading (+ for reproduction, == for genetic equality).
    """
    tag = 1  # Class variable: shared by ALL instances of Rabbit

    def __init__(self, age: int, parent1=None, parent2=None):
        super().__init__(age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1  # Increment tag for the next rabbit

    def get_rid(self):
        # Format ID to be 3 digits (e.g., 001)
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    # Operator Overloading: +

    def __add__(self, other: 'Rabbit'):
        # Returns a new Rabbit, age 0, with self and other as parents
        return Rabbit(0, self, other)

    # Operator Overloading: ==
    # Define what it means for two Rabbits to be "equal"
    # Here: Same parents implies equality (siblings are equal in this logic)
    def __eq__(self, other: 'Rabbit'):
        # 1. Identity check
        if self is other:
            return True
        
        # 2. Type check
        if not isinstance(other, Rabbit):
            return False

        # 3. Check for missing parents (cannot compare ancestry if parents don't exist)
        if (self.parent1 is None or self.parent2 is None or
            other.parent1 is None or other.parent2 is None):
            return False

        # 4. Check if parents match (order doesn't matter)
        parents_same = (self.parent1.rid == other.parent1.rid and
                        self.parent2.rid == other.parent2.rid)

        parents_swapped = (self.parent1.rid == other.parent2.rid and
                           self.parent2.rid == other.parent1.rid)

        return parents_same or parents_swapped

    def __str__(self):
        return f"rabbit:{self.get_rid()}"


# ==============================================================================
# Main Execution
# ==============================================================================

def main():
    print("="*50)
    print("OOP Inheritance & Polymorphism Demo")
    print("="*50)

    # --- 1. Basic Inheritance (Person & Student) ---
    print("\n--- Person & Student ---")
    p1 = Person("Alice", 40)
    s1 = Student("Bob", 40, "CS")
    
    print(p1)
    p1.speak()
    
    print(s1)
    s1.speak()  # Random student response
    
    p1.age_diff(s1)

    # --- 2. Polymorphism (Cat) ---
    print("\n--- Cat ---")
    c1 = Cat(3)
    c1.set_name("Garfield")
    print(c1)
    c1.speak()

    # --- 3. Operator Overloading (Rabbit) ---
    print("\n--- Rabbit Reproduction ---")
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r3 = r1 + r2  # Uses __add__
    r4 = r2 + r1  # Different order addition
    
    print(f"Parent 1: {r1}, Parent 2: {r2}")
    print(f"Child 1: {r3}") 
    
    # Check Equality (Sibling logic)
    print(f"Are r3 and r4 equal? {r3 == r4}") # Should be True (same parents)
    print(f"Are r1 and r3 equal? {r1 == r3}") # Should be False

if __name__ == "__main__":
    main()