""" 
#* 题意: 每个元素找到它右边「第一个比它大」的元素的位置，求它们的距离。这题与 593 非常类似，并且更加简单，因为 temperatures array 并不是 circular。单调栈解题。
? https://leetcode.cn/problems/daily-temperatures/solution/dong-hua-yan-shi-dan-diao-zhan-739mei-ri-iita/
? 动画: https://leetcode.cn/problems/daily-temperatures/solution/leetcode-tu-jie-739mei-ri-wen-du-by-misterbooo/
/ 时间复杂度: O(n)，其中 n 是温度列表的长度。正向遍历温度列表一遍，对于温度列表中的每个下标，最多有一次进栈和出栈的操作。
/ 空间复杂度: O(n)，其中 n 是温度列表的长度。需要维护一个单调栈存储温度列表中的下标。
"""


class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0 for _ in temperatures]

        for i in range(len(temperatures)):
            curTemperature = temperatures[i]

            if len(stack) == 0:
                stack.append(i)
            else:
                while len(stack) > 0 and curTemperature > temperatures[stack[-1]]:
                    topDayIdx = stack.pop()
                    res[topDayIdx] = i - topDayIdx

                stack.append(i)

        return res
