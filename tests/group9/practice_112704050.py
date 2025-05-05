def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i ,j]





nums1 = [2,7,11,15]
target1 = 9
nums_2 = [3,2,4]
target2 = 6
def roman_int(s):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

    nums = []
    for i in range(len(s)):
        if s[i] == "I":
            num = I
            nums.append(num)
        elif s[i] == "V":
            num = V
            nums.append(num)
        elif s[i] == "X":
            num = X
            nums.append(num)
        elif s[i] == "L":
            num = L
            nums.append(num)
        elif s[i] == "C":
            num = C
            nums.append(num)
        elif s[i] == "D":
            num = D
            nums.append(num)
        elif s[i] == "M":
            num = M
            nums.append(num)

    i = 0
    sum = 0
    while i < len(nums):
        if i == len(nums)-1:
            sum += nums[i]
            break
        if nums[i] < nums[i+1]:
            val = nums[i+1] - nums[i]
            sum += val
            i += 2
        else:
            sum += nums[i]
            i += 1

    
    return nums,sum
s1 = "III"
s2 = "LVIII"
s3 = "MCMXCIV"

def min_time_trip(bus_time,trip):
    time = 1
    while True:
        sum = 0
        #print(f"time: {time}")
        for i in range(len(bus_time)):
            sum += time // bus_time[i]

        #print(f"sum: {sum}")
        if sum >= trip:
            return time
        
        time += 1
bus_time1 = [1,1,2,3]
trips1 = 10
bus_time2 = [2]
trips2 = 1


###sort people
def sort_by_height(names,heights):
    copy_heights = heights[:]
    copy_heights.sort()
    copy_names = names[:]
    new_names = []
    """
    #print(copy_heights)
    while copy_heights:
        #print(copy_heights[0])

        for i in range(len(heights)):

            if copy_heights[0] == heights[i]:
                #print(i)
                #print(copy_names[i])
                new_names.append(copy_names[i])
                copy_names[i] = "0"
                copy_heights.remove(heights[i])
                heights[i] = 0

                #print(copy_names)
                #print(new_names)
                break
    """
    for i in range(len(heights)):
            #print(copy_heights[i])
            for j in range(len(heights)):
                 if copy_heights[i] == heights[j]:
                      #print(names[j])
                      new_names = [names[j]] + new_names
                      heights[j] = 0




    #new_names = sorted(new_names, reverse=True)
    return new_names
names1 = ["M", "J", "E"]
heights1 = [180,165,170]
names2 = ["A", "B","B","C","D","E","F","G"]
heights2 = [122,133,124,190,190,192,194,192]

def partition(nums):
    diff = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            s = abs(nums[i]-nums[j])
            diff.append(s)

    diff.sort()
    return diff[0]

nums1 = [1,3,2,4]
numss2 = [100,10,1]

def min_max_diff(nums, p):
    copy_nums = nums[:]
    copy_nums.sort()
    result = []
   
    for i in range(p):
        #print(copy_nums)
        min = copy_nums[1] - copy_nums[0]
        index = 2
        temp = 1
        #print(min)
        while index <len(copy_nums):
            val = copy_nums[index] - copy_nums[index-1]
            #print(f"{index}: {val}")

            if val < min:
                min = val
                temp = index
                index += 1
                #print(val)
            else:
                index += 1

        #print(temp)
        copy_nums.remove(copy_nums[temp])
        copy_nums.remove(copy_nums[temp-1])
        result.append(min)
            
        #print(result)
    return max(result)

numsss1 = [10,1,2,7,4,1,8,11,12,12]
p1 = 2

def fib(n):
    if n == 1 or n == 0:   
        return n
    return (fib(n-1) + fib(n-2))



def reverse_list(list):
    if len(list) < 1:
        return list
    return reverse_list(list[1:]) + [list[0]]

list1 = [1,2,3,4,5]
list2 = [1,2,3,5,3]

def remove_nodes(list):
    new_list = []
    while list:
        #print(list)

        for i in range(len(list)):
            check = 1
            if list[0] < list[i]:
                check = 0
                
            else:
                check =1
        #print(check)
        if check == 0:
            #print(f"remove:{list[0]}")

            list.remove(list[0])
        else:
            #print(f"add {list[0]}")
            new_list.append(list[0])
            list.remove(list[0])

    #print(new_list)
    return new_list

list_1 = [5,2,13,3,8]
list_2 = [1,1,1,1]

##evaluate booleantree

#### Number of Enclaves
def path_togo(grid):
    m ,n = len(grid) , len(grid[0])
    def dfs(i,j):
        if i<0 or i >= m or j < 0 or j >= n or grid[i][j]!=1:#不能走
            return
        grid[i][j] = 2 # 走過

        dfs(i+1 ,j)
        dfs(i-1 ,j)
        dfs(i ,j+1)
        dfs(i ,j-1)

    for i in range(m):
        dfs(i,0)
        dfs(i,n-1)
    
    for j in range(n):
        dfs(0,j)
        dfs(m-1,j)

    #print(grid)
    def count(grid):
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count +=1
        return count
    #print(count(grid))
    return count(grid)
grid1 = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]

###jump game3
def rule1(arr,index):
    index -= arr[index]
    return index

def rule2(arr,index):
    index += arr[index]
    return index
  
    
def path(arr,start):
    for i in range(len(arr)):
        if arr[i] == 0:
            dest = i
            break            
    
    index = start
    trials = 1
    while trials <= 5*10**4:
        #print(f"step:{trials} index: {index}")
        if index > dest :
            #print(">")
            #print(rule1(arr,index))
            index = rule1(arr,index)
        elif index == dest:
            return True
        else:
            #print("<")
            #print(rule2(arr,index))
            index = rule2(arr,index)
        
        trials +=1
    return False
        
    


arr1 = [4,2,3,0,3,1,2]
start1 = 5
arr2 = [4,2,3,0,3,1,2]
start2 = 0
arr3 = [3,0,2,1,2]
start3 = 2

###Find path exist
def find_path(edges ,source ,dest):
    visited = set()
    queue = [source]

    while queue:
        node = queue.pop(0)
        if node == dest :
            return True


        visited.add(node)
        for u,v in edges:
            if u == node and v not in visited :
                queue.append(v)
            
            elif v == node and u not in visited:
                queue.append(u)
                

    return False
n1 = 3
edges1 = [[0,1],[1,2],[2,0]]
source1 = 0
dest1 =2
n2 = 6
edges2 = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source2 = 1
dest2 =6

##province
def num_of_province(isConnected):
    m  = len(isConnected)

    visited = set()
    def dfs(city):
        for neighbor in range(m):
            if isConnected[city][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)                

    province = 0
    for city in range(m):
        #print(f"visited:{visited}, city:{city} ,province: {province}")

        if city not in visited:
            visited.add(city)
            dfs(city)
            province+=1

    return province

isConnected1 = [[1,1,0],[1,1,0],[0,0,1]]
isConnected2 = [[1,0,0],[0,1,0],[0,0,1]]

###minimum score
def min_score(n,roads):
    visited = set()
    queue = [1]


    dest = []
    while queue:
        node = queue.pop(0)

        if node == n:
            return min(dest)

        visited.add(node)

        for u, v ,d in roads:
            if u == node and v not in visited:
                queue.append(v)
                dest.append(d)
            elif v == node and u not in visited:
                queue.append(u)
                dest.append(d)


n1 = 4
roads1 = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
n2 = 4
roads2 = [[1,2,2],[1,3,4],[3,4,7]]

if __name__ == "__main__":
    print(two_sum([2,7,11,15], 9))
    print(roman_int("MCMXCIV"))
    print(num_of_province(isConnected2))
    print(find_path(edges2,source2,dest2))
    print(path(arr3,start3))
    print(path(grid1))
    print(remove_nodes(list_2))
    print(reverse_list(list2))
    print(fib(10))
    print(min_max_diff(numsss1,p1))
    print(partition(numss2))
    print(sort_by_height(names2,heights2))
    print(min_time_trip(bus_time1,trips1))
    print(roman_int(s1))
    print(two_sum(nums_2,target2))
    print(min_score(n2,roads2))
