# 元組 (Tuples) 的使用

def compute_divmod(a, b):
    return (a // b, a % b)

q, r = compute_divmod(10, 3)
print(f"Quotient: {q}, Remainder: {r}")

# 提取元組內數據
def extract_tuple_data(tuples):
    numbers, unique_strings = (), ()
    for item in tuples:
        numbers += (item[0],)
        if item[1] not in unique_strings:
            unique_strings += (item[1],)
    return min(numbers), max(numbers), len(unique_strings)

data_set = ((2014, "Alice"), (2014, "Bob"), (2012, "Charlie"), (2010, "David"))
low, high, count = extract_tuple_data(data_set)
print(f"Min year: {low}, Max year: {high}, Unique names: {count}")

# 列表 (Lists) 操作
def sum_list_elements(lst):
    return sum(lst)

print(sum_list_elements([1, 2, 3, 4]))

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums1.extend([0, 7])
print(nums1)
merged_list = nums1 + nums2
print(merged_list)

# 排序與反向排序
values = [9, 3, 5, 1]
print(sorted(values))
values.sort()
print(values)

# 別名與複製
warm_colors = ['red', 'yellow', 'orange']
hot_colors = warm_colors
hot_colors.append('pink')
print(warm_colors)

cool_colors = ['blue', 'green', 'grey']
cloned_colors = cool_colors[:]
cloned_colors.append('black')
print(cool_colors)
print(cloned_colors)

# 刪除列表元素
lst = [2, 1, 3, 6, 3, 7, 0]
lst.remove(3)
print(lst)
del lst[1]
print(lst)
print(lst.pop())
print(lst)

# 迭代時刪除元素 (正確方式)
def remove_common_elements(list1, list2):
    copy_list = list1[:]
    for elem in copy_list:
        if elem in list2:
            list1.remove(elem)

l1 = [1, 2, 3, 4]
l2 = [1, 2, 5, 6]
remove_common_elements(l1, l2)
print(l1)

# 多層列表
yellow_orange = ['yellow', 'orange']
red = ['red']
colors_group = [yellow_orange]
colors_group.append(red)
print(colors_group)
red.append('pink')
print(colors_group)

# 排序與回傳新列表
flat_list = ['yellow', 'blue', 'red', 'green']
flat_list.sort()
print(flat_list)
new_sorted_list = sorted(flat_list, reverse=True)
print(new_sorted_list)
