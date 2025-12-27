import random
from add_path import add_path
add_path()


#################################
## Animal abstract data type 
#################################

class Animal(object):
    """Abstract base class representing an Animal.
    
    Attributes:
        age: Age of the animal (non-negative int)
        name: Name of the animal (str or None)
    
    Methods:
        get_age(): Returns animal's age
        get_name(): Returns animal's name
        set_age(newage): Updates animal's age
        set_name(newname): Updates animal's name
    """
    def __init__(self, age):
        """Initialize an animal with an age.
        
        Args:
            age: Non-negative integer representing age
        
        Raises:
            ValueError: If age is negative
        """
        if age < 0:
            raise ValueError(f"age must be non-negative, got {age}")
        self.age = age
        self.name = None

    def get_age(self):
        """Return the animal's age."""
        return self.age

    def get_name(self):
        """Return the animal's name."""
        return self.name

    def set_age(self, newage):
        """Set the animal's age.
        
        Args:
            newage: New age (non-negative int)
        
        Raises:
            ValueError: If newage is negative
        """
        if newage < 0:
            raise ValueError(f"age must be non-negative, got {newage}")
        self.age = newage

    def set_name(self, newname=""):
        """Set the animal's name.
        
        Args:
            newname: New name (str, default: empty string)
        """
        self.name = newname

    def __str__(self):
        return f"animal:{self.name}:{self.age}"


#################################
## Cat inherits from Animal
#################################

class Cat(Animal):
    """Cat class inheriting from Animal.
    
    Additional methods:
        speak(): Makes the cat meow
    """
    def speak(self):
        """Make the cat speak (meow)."""
        print("meow")

    def __str__(self):
        return f"cat:{self.name}:{self.age}"


#################################
## Person inherits from Animal
#################################

class Person(Animal):
    """Person class inheriting from Animal.
    
    Additional attributes:
        friends: List of friend names
    
    Additional methods:
        get_friends(): Returns list of friends
        speak(): Says hello
        add_friend(fname): Adds a friend to the list
        age_diff(other): Prints age difference with another person
    """
    def __init__(self, name, age):
        """Initialize a person with name and age.
        
        Args:
            name: Person's name (str)
            age: Person's age (non-negative int)
        
        Raises:
            ValueError: If age is negative
        """
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        """Return list of friends."""
        return self.friends

    def speak(self):
        """Make the person speak (hello)."""
        print("hello")

    def add_friend(self, fname):
        """Add a friend to the friends list (no duplicates).
        
        Args:
            fname: Friend's name (str)
        """
        if fname not in self.friends:
            self.friends.append(fname)

    def age_diff(self, other):
        """Print age difference with another person.
        
        Args:
            other: Another Person object
        
        Raises:
            AttributeError: If other doesn't have 'age' attribute
        """
        if not isinstance(other, Animal):
            raise TypeError(f"Expected Animal object, got {type(other).__name__}")
        diff = abs(self.age - other.age)
        print(diff, "year difference")

    def __str__(self):
        return f"person:{self.name}:{self.age}"


#################################
## Student inherits from Person
#################################

class Student(Person):
    """Student class inheriting from Person.
    
    Additional attributes:
        major: Student's major (str or None)
    
    Additional methods:
        change_major(major): Changes the student's major
        speak(): Random motivational student statement
    """
    def __init__(self, name, age, major=None):
        """Initialize a student with name, age, and optional major.
        
        Args:
            name: Student's name (str)
            age: Student's age (non-negative int)
            major: Student's major (str, default: None)
        
        Raises:
            ValueError: If age is negative
        """
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        """Change the student's major.
        
        Args:
            major: New major (str)
        """
        self.major = major

    def speak(self):
        """Make a random student statement."""
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif r < 0.5:
            print("i need sleep")
        elif r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")

    def __str__(self):
        return f"student:{self.name}:{self.age}:{self.major}"


#################################
## Rabbit uses class variable & operator overloading
#################################

class Rabbit(Animal):
    """Rabbit class demonstrating class variables and operator overloading.
    
    Class variables:
        tag: Counter for unique rabbit IDs
    
    Instance attributes:
        parent1, parent2: Parent rabbits
        rid: Unique rabbit ID
    
    Methods demonstrate:
        - Class variables (tag counter)
        - Operator overloading (__add__, __eq__)
    """
    tag = 1  # class variable

    def __init__(self, age, parent1=None, parent2=None):
        """Initialize a rabbit with optional parents.
        
        Args:
            age: Age of the rabbit (non-negative int)
            parent1: First parent Rabbit object (optional)
            parent2: Second parent Rabbit object (optional)
        
        Raises:
            ValueError: If age is negative
        """
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        """Return zero-padded rabbit ID (3 digits)."""
        return str(self.rid).zfill(3)

    def get_parent1(self):
        """Return the first parent rabbit."""
        return self.parent1

    def get_parent2(self):
        """Return the second parent rabbit."""
        return self.parent2

    def __add__(self, other):
        """Operator overloading: Create offspring from two rabbits.
        
        Args:
            other: Another Rabbit object
        
        Returns:
            New Rabbit with age 0 and self and other as parents
        
        Raises:
            TypeError: If other is not a Rabbit
        """
        if not isinstance(other, Rabbit):
            raise TypeError(f"Can only breed with another Rabbit, got {type(other).__name__}")
        return Rabbit(0, self, other)

    def __eq__(self, other):
        """Check equality based on parent lineage.
        
        Two rabbits are equal if:
        - They are the same object, or
        - They have the same parents (in any order)
        
        Args:
            other: Another Rabbit object
        
        Returns:
            True if rabbits are equal, False otherwise
        """
        # If same exact object, automatically equal
        if self is other:
            return True

        # If other is not a Rabbit, not equal
        if not isinstance(other, Rabbit):
            return False

        # If any parent is None, cannot compare family lines
        if (self.parent1 is None or self.parent2 is None or
            other.parent1 is None or other.parent2 is None):
            return False

        # Check parents same order
        parents_same = (self.parent1.rid == other.parent1.rid and
                        self.parent2.rid == other.parent2.rid)

        # Check parents reversed order
        parents_swapped = (self.parent1.rid == other.parent2.rid and
                           self.parent2.rid == other.parent1.rid)

        return parents_same or parents_swapped

    def __str__(self):
        return "rabbit:" + self.get_rid()
