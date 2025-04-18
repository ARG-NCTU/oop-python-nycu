#Partition nums into two arrays, nums1 and nums2, such that:

#Each element of the array nums belongs to either the array nums1 or the array nums2.
#Both arrays are non-empty.
#The value of the partition is minimized.
#The value of the partition is |max(nums1) - min(nums2)|.
nums=[100,1,10]
nums.sort()
print(nums)
dif=[]
for n in range(len(nums)-1):
    dif.append(abs(nums[n]-nums[n+1]))
print(min(dif))
#value=max(num1)-min(num2)