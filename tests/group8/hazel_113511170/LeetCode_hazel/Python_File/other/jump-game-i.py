def jump(nums):
    n=len(nums)
    cur_pos=0
    destination=0
    jump=0
    if n==1 or n==0:
        return 0
    for i in range(n):
        destination=max(destination,i+nums[i])
        if cur_pos==i:
            cur_pos=destination
            jump=jump+1
        if cur_pos>=n-1:
            return jump
           
nums = [2,3,1,1,4]
print(jump(nums))
nums = [2,3,0,1,4]
print(jump(nums))