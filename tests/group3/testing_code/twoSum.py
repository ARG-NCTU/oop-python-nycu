def twoSum(nums:list[int],target:int)-> list[int]:
	for i in nums:
		if target-i in nums:
			n1=nums.index(i)
			n2=nums.index(target-i)
			if n1 != n2:
				return [n1,n2]
			else:
				for j in range(len(nums)):
					if j!=n1 and target-i ==nums[j]:
						return [n1,j]
	return []
