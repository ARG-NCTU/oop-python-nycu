class Solution:
    def romanToInt(self, s: str) -> int:
        # 正確的字典語法
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s) - 1):  # 遍歷到倒數第二個字符
            if roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]  # 減去當前值
            else:
                total += roman_map[s[i]]  # 加上當前值
        # 處理最後一個字符
        total += roman_map[s[-1]]
        return total