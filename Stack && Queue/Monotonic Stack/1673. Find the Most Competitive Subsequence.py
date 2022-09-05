""" 
! 与 402 属于同题. 相当于 402 的反面, 402 是给出了 "removing k digits from num", 也就是应该删除的元素的个数。而这道题则是说明了「要保留元素的个数」。所以, 首先求出「需要删除的元素的个数」, 然后就与 402 一模一样了。

* 本题我们要维护一个「单调递增」的栈, 每当遍历到一个新的元素时, 将该元素与「栈顶元素」比较, 如果该元素小于「栈顶元素」则弹出「栈顶元素」, 直到与「栈顶元素」相等或大于「栈顶元素」即可。同时我们要维护一个变量 deletedCount 来记录我们最多可以删除多少个元素, 所谓删除元素就是从栈内弹出元素, 我们最多能删除 len(nums) - k 个元素。
# 若删除的数目达到上限, 则保留栈中元素不再删除。
* 遍历一遍后, 若栈中元素数目大于k个(即 n-k>0), 将多余元素出栈, 或者直接保留前 k 个元素
"""


class Solution:
    def mostCompetitive(self, nums, k):
        deletedCount = len(nums) - k
        stack = []

        for i in range(len(nums)):
            while len(stack) > 0 and stack[-1] > nums[i] and deletedCount > 0:
                stack.pop()
                deletedCount -= 1
            stack.append(nums[i])

        return stack[:k]
