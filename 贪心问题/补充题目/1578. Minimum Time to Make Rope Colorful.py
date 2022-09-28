""" 
* 根据题意可以知道, 如果字符串 colors 中有若干相邻的重复颜色, 则这些颜色中最多只能保留一个。因此, 我们可以采取贪心的策略：在这一系列重复颜色中, 我们保留「删除成本最高」的颜色, 并删除其他颜色。这样得到的删除成本一定是最低的。
? https://leetcode.cn/problems/minimum-time-to-make-rope-colorful/solution/bi-mian-zhong-fu-zi-mu-de-zui-xiao-shan-chu-chen-4/
"""


class Solution:
    def minCost(self, colors: str, neededTime):
        cost = 0
        index = 0
        while index < len(colors):
            curColor = colors[index]

            # * 在处理 colors[i] 字符时，当 colors[i+1..j] 都是与它一样的字符时，统计 colors[i..j] 的花费总和 sum，并保留其中最大的花费 max。那么使 colors[i..j] 这一阶段 colorful 所需的最小花费就是 sum - max。

            maxCostOfCurColor = 0
            sumOfCurColor = 0
            while index < len(colors) and colors[index] == curColor:
                maxCostOfCurColor = max(maxCostOfCurColor, neededTime[index])
                sumOfCurColor += neededTime[index]
                index += 1

            # * 如果「当前元素」与「下一个元素」是「同一个颜色」的, 那么这两个变量相减的结果就是 0, 不影响 cost 最后的结果。
            cost += sumOfCurColor - maxCostOfCurColor
        return cost


Solution().minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1])
