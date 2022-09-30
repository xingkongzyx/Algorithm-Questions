""" 
? 代码: https://leetcode.cn/problems/maximum-frequency-stack/solution/895-zui-da-pin-lu-zhan-python-by-bluegre-pux4/
? 动画解释: https://leetcode.com/problems/maximum-frequency-stack/discuss/1862015/BEST-Explanation-Visually
"""

from collections import defaultdict


class FreqStack:

    def __init__(self):
        # 维护两个字典，以便快速查询频率和数字

        # 所有频率对应的数字集合，用list实现后进先出
        self.stack = defaultdict(list)
        # 所有数字对应的频率
        self.cnt = defaultdict(int)
        # o(1)找到最大的频率
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        self.stack[self.cnt[val]].append(val)
        if self.cnt[val] > self.maxFreq:  # 更新self.maxFreq
            self.maxFreq = self.cnt[val]

    def pop(self) -> int:
        answer = self.stack[self.maxFreq].pop()
        if len(self.stack[self.maxFreq]) == 0:
            del self.stack[self.maxFreq]
            self.maxFreq -= 1  # maxFreq 必然是连续的，直接减一即可
        self.cnt[answer] -= 1
        return answer
