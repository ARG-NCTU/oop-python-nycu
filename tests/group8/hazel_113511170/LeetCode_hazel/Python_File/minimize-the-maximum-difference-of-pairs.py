nums=[3,3,5,1,0,5,6,6]
p=4

nums.sort()
l=0
h=abs(nums[len(nums)-1]-nums[0])

def is_valid(mid):
    count=0
    n=0
    while count<p and n<len(nums)-1:
        if abs(nums[n]-nums[n+1])<=mid:
            count=count+1
            n=n+2
        else:
            n=n+1
    return count<p #and count+equal>=p


while l<h:
    mid=(l+h)//2
    if is_valid(mid):
        l=mid+1
    else:
        h=mid
print(l)