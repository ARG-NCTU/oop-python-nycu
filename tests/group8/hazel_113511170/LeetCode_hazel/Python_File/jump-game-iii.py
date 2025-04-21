# Given an array of non-negative integers arr, 
# you are initially positioned at start index of the array. 
# When you are at index i, 
# you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.
# Notice that you can not jump outside of the array at any time.

def canReach(arr,start):
    if start>=len(arr) or start<0 or arr[start]<0:
        return False
    i=arr[start]
    if i==0:
        return True
    arr[start]=-1
    return canReach(arr,start+i) or canReach(arr,start-i)
    

arr=[4,2,3,0,3,1,2]  
start=2
print(canReach(arr,start))