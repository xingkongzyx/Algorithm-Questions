""" 
#> 求最大窗口, 所以在窗口非法时「收缩窗口」(也就是移动左指针), 并且在「收缩窗口」的判断句外面记录最大窗口。这道题「窗口非法」就是指窗口内的 absolute difference between any two elements 大于 limit

* 使用一般的滑动窗口的想法：
* 
* ➀ 维护 left 和 right 的窗口, 遍历过程中 left 和 right 交替前移确保滑动窗口内的元素满足要求
* ➁ 滑动过程中保持 maxNumber(最大值) 和 minNumber(最小值) 两个最值。
* ➂ 向右滑动时, 更新 maxNumber 和 minNumber。
* ➃ 当 maxNumber 和 minNumber 的差大于 limit 时, 窗口缩小。
! ➄ 问题是, 窗口缩小时, 需要便历窗口内所有数字才能确定 maxNumber 和 minNumber 的大小, 这个过程时间复杂度是 O(n), 令算法整体时间复杂度到了O(n^2)。
* ➅ 那么, 如何在更短的时间内确定『滑动窗口』的 maxNumber(最大值) 和 minNumber(最小值) 的大小呢？那我们完全可以借助滑动窗口的最大值这个题目的思想来解决这个题目。
# 维护一个「单调递减」的双端队列, 进而得到滑动窗口的「最大值」。维护一个「单调递增」的双端队列, 来获取滑动窗口的「最小值」。
? 代码来自 https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/solution/jue-dui-chai-bu-chao-guo-xian-zhi-de-zui-chang-lia/
#? 从暴力法到滑动窗口到单调队列的思考过程: https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/solution/he-gua-de-shu-ju-jie-gou-hua-dong-chuang-v46j/

/ 时间复杂度: O(n), 两个队列出队、入队最多 n 次。所以时间复杂度为 O(n)
/ 空间复杂度: O(n), 其中 n 是数组长度。最坏情况下有序集合将和原数组等大
"""


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        left = 0
        right = 0
        maxLen = 0

        # get maximum value
        decreaseQueue = deque([])
        # get minimum value
        increaseQueue = deque([])

        while right < len(nums):
            # * 右沿元素的下标进入窗口、维护最小值单调队列
            while increaseQueue and nums[increaseQueue[-1]] > nums[right]:
                increaseQueue.pop()
            increaseQueue.append(right)

            # * 右沿元素的下标进入窗口、维护最大值单调队列
            while decreaseQueue and nums[decreaseQueue[-1]] < nums[right]:
                decreaseQueue.pop()
            decreaseQueue.append(right)

            # * 如果当前窗口的最大值最小值的差大于 limit, 则不断缩小窗口（左沿++）, 直至最大值变小或者最小值变大从而满足 limit 限制
            while nums[decreaseQueue[0]] - nums[increaseQueue[0]] > limit:
                left += 1
                while decreaseQueue and decreaseQueue[0] < left:
                    decreaseQueue.popleft()
                while increaseQueue and increaseQueue[0] < left:
                    increaseQueue.popleft()

            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen
