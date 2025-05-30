import copy
    
def p(nums):
    n=len(nums)
    ans=[]
    
    def rec(index):
        if index==n:
            return
            
        else:
            for i in range(index+1,n):
                
                t=nums[index]
                nums[index]=nums[i]
                nums[i]=t
                rec(index+1)

                #print(set)

                if nums not in ans:
                    ans.append(copy.deepcopy(nums))
                t=nums[index]
                nums[index]=nums[i]
                nums[i]=t
                rec(index+1)
                #print(set)
                if nums not in ans:
                    ans.append(copy.deepcopy(nums))
    rec(0)
    return ans


nums=[1,2,3]
print(p(nums))


    