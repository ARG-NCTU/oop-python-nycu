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

def get_data(aTuple):
    """
    aTuple, tuple of tuples (int, string)
    Extracts all integers from aTuple and sets 
    them as elements in a new tuple. 
    Extracts all unique strings from from aTuple 
    and sets them as elements in a new tuple.
    Returns a tuple of the minimum integer, the
    maximum integer, and the number of unique strings
    """
    nums = ()    # empty tuple
    words = ()
    for t in aTuple:
        # concatenating with a singleton tuple
        nums = nums + (t[0],)   
        # only add words haven't added before
        if t[1] not in words:   
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

test = ((1,"a"),(2, "b"),
        (1,"a"),(7,"b"))
(a, b, c) = get_data(test)
print("最多的:",a,"最少的:",b,"總共幾個字母:",c)

# apply to any data you want!
tswift = ((2014,"phono wu"),
          (2014, "gibbs wu"),
          (2012,"porco wu"), 
          (2010,"gibbs wu"), 
          (2008,"lagrange wu"), 
          (2000,"alan wu"))    
(min_year, max_year, num_people) = get_data(tswift)
print("From", min_year, "to", max_year, \
        "Taylor Swift wrote songs about", num_people, "people!")