#########################
## EXAMPLE: returning a tuple
#########################
def bmi_counting(weight=57,height=1.7):
    bmi = weight/(height**2)
    health_index = 0
    print(bmi)
    if bmi < 18.5:
        print("Too thin")
        health_index = 1
        return (False , health_index)
    elif bmi > 24 :
        print("Overweight")
        health_index = 2
        return (False , health_index)
    else:
        print("Healthy")
        health_index = 0
        return (True , health_index)
    
bmi_counting()

#########################
## EXAMPLE: iterating over tuples
#########################
def get_data(data):
    patient = ()
    illness = ()
    height = ()
    for i in data:
        if i[0] not in patient:
            patient += (i[0],)
        if i[1] not in illness:
            illness += (i[1],)
        height += (i[2],)

    patient_num = len(patient)
    max_height = max(height)
    min_height = min(height)        
    illness_type = len(illness)
    return  (patient_num,max_height , min_height , illness_type)


data = ((1,"a",170),(2,"b",199),(3,"c",198),(4,"a",122),(5,"n",150))
(a,b,c,d)=get_data(data)
print("patient number", a ,"max: ", a , "min: ", b ,"illness type: ",c)

#########################
## EXAMPLE: sum of elements in a list
#########################
def add(data):
    result = 0
    for i in range(len(data)):
        result += data[i]
    return result

def minus(data):
    result = 0
    for i in range(len(data)):
        result -= data[i]
    return result

def multiple(data):
    result = 1
    for i in range(len(data)):
        result *= data[i]
    return result

data = [1,2,3,4,5,6,7,8,9,10]
print(add(data),minus(data),multiple(data))

#########################
## EXAMPLE: aliasing
#########################
def append_use(warm = ['red', 'yellow', 'orange']):
    copy = warm[:]
    hot = warm
    hot.append('pink')
    print(hot)
    print(warm)
    return (copy ,hot , warm)

#########################
## EXAMPLE: cloning
#########################

def simple_copy(cool = ['blue', 'green', 'grey'] ):
    chill = cool[:] # 淺層複製 cool 的內容
    chill.append('orange')
    print(chill)
    print(cool)
    return (chill,cool)

#########################
## EXAMPLE: sorting with/without mutation
#########################
def sort_use(warm = ['red', 'yellow', 'orange']):
    copy = warm[:]
    sortedwarm = warm.sort()#就地改變不回傳
    print(warm)
    print(sortedwarm)

    cool = copy
    sortedcool = sorted(cool)#改變後會回傳
    print(cool)
    print(sortedcool)
    return (sortedwarm , sortedcool)

#########################
## EXAMPLE: lists of lists of lists...
#########################
import copy
def alot_list(warm = ['yellow', 'orange']):
    hot = ['red']
    brightcolors = [warm]
    brightcolors.append(hot)
    b_o = copy.deepcopy(brightcolors)#深層複製
    print(b_o)
    hot.append('pink')#會跟著修改brightcolor[1]
    #print(hot)
    print(brightcolors)
    return (b_o , brightcolors)

append_use()
simple_copy()
sort_use()
alot_list()


###############################
## EXAMPLE: mutating a list while iterating over it
###############################
def present_or_not(all,absense):
    present = all
    for i in all:
        #print(f"Checking:{i}")
        #print(f"Before: {present}")
        if i in absense:
            present.remove(i)
            #print(f"After: {present}")
    return present

def present_or_not_new(all,absense):
    present = all[:]
    for i in all[:]:
        #print(f"Checking:{i}")
        #print(f"Before: {present}")
        if i in absense:
            present.remove(i)
            #print(f"After: {present}")
    return present

all = ["Alice" , "Bandy", "Cindy", "Diago", "Edward", "Fred"]
absense = ["Alice","Bandy" ,"Diago","Cindy"]
print(present_or_not(all, absense))

print("\n")

all = ["Alice" , "Bandy", "Cindy", "Diago", "Edward", "Fred"]
absense = ["Alice","Bandy" ,"Diago","Cindy"]
print(present_or_not_new(all, absense))



