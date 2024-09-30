def bubble_sort(arr):
     n = len(arr)
     for i in range(n):
         for j in range(j-1):
             if arr[j] > arr[j+1]:
                 tmp = arr[j]
                 arr[j] = arr[j+1]
                 arr[j+1] = tmp
     return arr
 
print(bubble_sort([4, 2, 1, 8, 7, 6]))
