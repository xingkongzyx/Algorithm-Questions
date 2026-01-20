""" 
问: 是否会出现中间的某个栈为空的情况？
答: 不会。因为出栈一定是在元素频率最高的栈上发生的, 即上面动画中最右侧的非空栈。
问: 如果有多个相同频率的数字, 怎么保证弹出的是一定最接近栈顶的那个数字？
答: 因为这个做法本质上就是把原始栈拆分成多个栈, 每个栈都存储着相同频率的数字（这里的频率指的是数字入栈时的频率）, 且保持了原有的入栈顺序, 因此弹出的是一定最接近栈顶的那个数字。

链接: https://leetcode.cn/problems/maximum-frequency-stack/solutions/1998430/mei-xiang-ming-bai-yi-ge-dong-hua-miao-d-oich/

? 代码: https://leetcode.cn/problems/maximum-frequency-stack/solution/895-zui-da-pin-lu-zhan-python-by-bluegre-pux4/
? 动画解释: https://leetcode.com/problems/maximum-frequency-stack/discuss/1862015/BEST-Explanation-Visually
"""

from collections import defaultdict


class FreqStack:

    def __init__(self):
        # 维护两个字典, 以便快速查询频率和数字

        # 所有频率对应的数字集合, 用list实现后进先出
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
            self.maxFreq -= 1  # maxFreq 必然是连续的, 直接减一即可
        self.cnt[answer] -= 1
        return answer
