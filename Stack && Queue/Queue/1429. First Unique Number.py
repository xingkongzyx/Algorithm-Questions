""" 
? https://leetcode.cn/problems/first-unique-number/solution/python-by-intoloop/
"""


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dic = {}
        # * 初始化指针位置
        self.nums = []
        self.index = 0
        for num in nums:
            if num not in self.dic:
                self.dic[num] = 1
                self.nums.append(num)
            else:
                self.dic[num] += 1

    def showFirstUnique(self) -> int:
        # * 通过更新 self.idx 来找到第一个 unique number, 如果找不到, 则返回 -1
        while self.index < len(self.nums):
            if self.dic[self.nums[self.index]] == 1:
                return self.nums[self.index]
            self.index += 1
        return -1

    def add(self, value: int) -> None:
        if value in self.dic:
            self.dic[value] += 1
        else:
            self.dic[value] = 1
            self.nums.append(value)
