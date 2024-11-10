def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
<<<<<<< HEAD
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
=======
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
>>>>>>> 22d825dedfe9895059f530f53327f88c34904392
    return arr

print(bubble_sort([4, 2, 1, 8, 7, 6]))

