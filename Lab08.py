import time

names_data = ["john doe", "jane smith", "bob johnson"] #name list
names_count = 0 #used to reocrd the number of names in the list
for i in names_data:
    #go through all the names in the list
    if len(i.split()) == 2:
        print(i)
        #directly print out the name
        names_count += 1
    time.sleep(1)
    #to slow down the printing speed
print("total: " + str(names_count))
