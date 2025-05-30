# Python 字典 (Dictionary) 的詳細介紹與使用說明

Python 字典 (Dictionary) 是一種可變的、無序的集合，包含了鍵值對 (key-value pairs)。每個鍵 (key) 都是唯一的，並且與一個值 (value) 相關聯。字典的鍵可以是不可變（immutable）的數據類型，如字符串、數字或元組，而值可以是任何數據類型。

## 創建字典

可以使用花括號 `{}` 或 `dict()` 函數來創建字典：

```python
# 使用花括號創建字典
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# 使用 dict() 函數創建字典
person = dict(name='Alice', age=25, city='New York')
```

## 訪問字典中的值

可以使用鍵來訪問字典中的值：

```python
print(person['name'])  # 輸出: Alice
print(person.get('age'))  # 輸出: 25
```

## 添加或更新鍵值對

可以通過指定鍵來添加或更新鍵值對：

```python
# 添加新的鍵值對
person['email'] = 'alice@example.com'

# 更新已有的鍵值對
person['age'] = 26
```

## 刪除鍵值對

可以使用 `del` 關鍵字或 `pop()` 方法來刪除鍵值對：

```python
# 使用 del 關鍵字
del person['city']

# 使用 pop() 方法
email = person.pop('email')
```

## 遍歷字典

可以使用 `for` 循環來遍歷字典的鍵、值或鍵值對：

```python
# 遍歷鍵
for key in person:
    print(key)

# 遍歷值
for value in person.values():
    print(value)

# 遍歷鍵值對
for key, value in person.items():
    print(f'{key}: {value}')
```

## 字典方法

Python 字典有多種方法，以下是一些常用的方法：

- `clear()`: 清空字典
- `copy()`: 返回字典的淺拷貝
- `fromkeys(seq[, value])`: 使用序列 seq 中的元素作為鍵創建新字典，並設置值 value（默認為 None）
- `get(key[, default])`: 返回鍵 key 對應的值，如果鍵不存在則返回 default（默認為 None）
- `items()`: 返回包含字典所有鍵值對的視圖
- `keys()`: 返回包含字典所有鍵的視圖
- `pop(key[, default])`: 刪除鍵 key 並返回其值，如果鍵不存在則返回 default（默認為 None）
- `popitem()`: 隨機刪除並返回字典中的一對鍵值對
- `setdefault(key[, default])`: 如果鍵 key 存在則返回其值，否則設置並返回 default（默認為 None）
- `update([other])`: 使用其他字典或鍵值對更新當前字典
- `values()`: 返回包含字典所有值的視圖

## 範例: 計算單詞出現次數

以下是一個使用字典來計算文本中單詞出現次數的範例：

```python
text = "hello world hello python"
words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)  # 輸出: {'hello': 2, 'world': 1, 'python': 1}
```
