import random

#################################
## Animal abstract data type 
#################################
class Human(object):
    '''Human Class 
    Attributes: age, name, gender
    Methods: get_age, get_name, set_age, set_name, __str__, get_gender, set_gender
    '''
    def __init__(self, age, name, gender=None):
        self.age = age
        self.name = name
        self.gender = gender
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def get_gender(self):
        if self.gender == None:
            return "None of your business!"
        return self.gender
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def set_gender(self, newname=""):
        self.gender = newname
    def __str__(self):
        return "human:"+str(self.name)+":"+str(self.age)+":"+str(self.gender)
        
print("\n---- human tests ----")
a = Human(14, "Bob", "male")
print(a)
print(a.get_age())
a.set_name("Bobby")
print(a)
a.set_name()
print(a)



#################################
## Inheritance example 
#################################
class Asian(Human):
    def speak(self):
        print("I'm Asian.")
    def __str__(self):
        return "Asian:"+str(self.name)+":"+str(self.age)+":"+str(self.gender)
    
print("\n---- Asian tests ----")
c = Asian(51, "Xiao-mei", "female" )
c.set_name("Tsu-yu")
print(c)
c.speak()
print(c.get_age())
#a.speak() # error because there is no speak method for Animal class

    
#################################
## Inheritance example
#################################
class Character(Human):
    def __init__(self, age, name, gender, race="human"):
        Human.__init__(self, age, name, gender)
        self.set_name(name)
        self.friends = []
        self.race = race
        self.Class = self.set_class()
    def get_friends(self):
        return self.friends
    def speak(self):
        print("Hi!Today is a nice day!How are you?")
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")
    def set_class(self):
        chr_list = ["fighter", "monk", "martial artist", "wolf_rider", "archer", "warlord", "necromancer"]
        sel = random.randint(0, len(chr_list) - 1)
        return chr_list[sel]
    def change_race(self):
        race_list = ["human", "elf", "dwarf", "gnome", "giant", "Therianthropy", "half elf"]
        sel = random.randint(0, len(race_list) - 1)
        return race_list[sel]
    def __str__(self):
        return "charater:"+str(self.name)+":"+str(self.age)+":"+str(self.gender)+":"+str(self.Class)+":"+str(self.race)

print("\n---- character tests ----")
p1 = Character(30, "jason", "male")
p2 = Character(15, "Farry", "female")
print(p1.get_name())
print(p1.get_age())
print(p2.get_name())
print(p2.get_age())
print(p1)
p1.speak()
p1.age_diff(p2)
p1.set_class()
p1.change_race()
print(p1)
p2.set_class()
p2.change_race()
print(p2)

#################################
## Inheritance example
#################################
class Professor(Character):
    def __init__(self, age, name, gender, major=None):
        Character.__init__(self, age, name, gender)
        self.major = major
    def __str__(self):
        return "professor:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have meeting")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am doing research")

print("\n---- professor tests ----")
s1 = Professor(30, 'alice', "female",  "CS")
s2 = Professor(67, 'beth', "male", "DOP")
print(s1)
print(s2)
print(s1.get_name(),"says:", end=" ")
s1.speak()
print(s2.get_name(),"says:", end=" ")
s2.speak()



#################################
## Use of class variables  
#################################
class Android(Human):
    # a class variable, tag, shared across all instances
    tag = 1
    def __init__(self, age,parent1=None, parent2=None):
        Human.__init__(self, age, None)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Android.tag
        Android.tag += 1
    def get_rid(self):
        # zfill used to add leading zeroes 001 instead of 1
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        # returning object of same type as this class
        return Android(0, self, other)
    def __eq__(self, other):
        # compare the ids of self and other's parents
        # don't care about the order of the parents
        # the backslash tells python I want to break up my line
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
                           and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite
    def __str__(self):
        return "android:"+ self.get_rid()

print("\n---- android tests ----")
print("---- testing creating androids ----")
r1 = Android(3)
r2 = Android(4)
r3 = Android(5)
print("r1:", r1)
print("r2:", r2)
print("r3:", r3)
print("r1 parent1:", r1.get_parent1())
print("r1 parent2:", r1.get_parent2())

print("---- testing android addition ----")
r4 = r1+r2   # r1.__add__(r2)
print("r1:", r1)
print("r2:", r2)
print("r4:", r4)
print("r4 parent1:", r4.get_parent1())
print("r4 parent2:", r4.get_parent2())

print("---- testing android equality ----")
r5 = r3+r4
r6 = r4+r3
print("r3:", r3)
print("r4:", r4)
print("r5:", r5)
print("r6:", r6)
print("r5 parent1:", r5.get_parent1())
print("r5 parent2:", r5.get_parent2())
print("r6 parent1:", r6.get_parent1())
print("r6 parent2:", r6.get_parent2())
print("r5 and r6 have same parents?", r5 == r6)
print("r4 and r6 have same parents?", r4 == r6)
