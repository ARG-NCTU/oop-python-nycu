#########################
## EXAMPLE: sum of elements in a list
#########################
def sum_elem_method1(L):
  total = 0 
  for i in range(len(L)): 
      total += L[i] 
  return total
  
def sum_elem_method2(L):
    total = 0 
    for i in L: 
        total += i 
    return total
  
print(sum_elem_method1([1,2,3,4]))
print(sum_elem_method2([1,2,3,4]))