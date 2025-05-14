from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # 配對 names 和 heights
        people = list(zip(names, heights))
        # 按身高降序排序
        people_sorted = sorted(people, key=lambda x: x[1], reverse=True)
        # 提取排序後的名字
        return [name for name, _ in people_sorted]
    # [expression for variable in iterable] return [(name, height) for name, height in people_sorted] return [name for name, _ in people_sorted]