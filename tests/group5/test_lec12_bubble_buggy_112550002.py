def bubble_sort(arr):
     n = len(arr)
     for i in range(n):
         for j in range(n-1):
             if arr[j] > arr[j+1]:
                 tmp = arr[j]
                 arr[j] = arr[j+1]
                 arr[j+1] = tmp
     return arr
 

def test_bubble_sort():
    assert bubble_sort([4,2,1,8,7,6]) == [1,2,4,6,7,8]
    # print(bubble_sort([4, 2, 1, 8, 7, 6]))
