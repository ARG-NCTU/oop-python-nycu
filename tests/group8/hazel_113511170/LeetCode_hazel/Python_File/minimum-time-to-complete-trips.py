# given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

time=[5,10,10]
totalTrips=9

l=1
h=totalTrips*min(time)
m=0

while l<=h:
    m=(l+h)//2
    if l==h:
        break
    num=sum(m//t for t in time)
    if num<totalTrips:
        l=m+1
    elif num>=totalTrips:
        h=m
    
print(m)
        




