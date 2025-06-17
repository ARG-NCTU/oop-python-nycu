def bubble_sort(in_lis):
    n = len(in_lis)
    for i in range(n):
        for j in range(i, n-1):
            if in_lis[i + n - j - 2] > in_lis[i + n - j - 1]:
                in_lis[i + n - j - 1], in_lis[i + n - j - 2] = in_lis[i + n - j - 2], in_lis[i + n - j - 1]
    return in_lis

print(bubble_sort([4, 2, 1, 8, 7, 6]))
