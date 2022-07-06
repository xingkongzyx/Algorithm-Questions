""" 
#> 求最大窗口，所以在窗口非法时「收缩窗口」(也就是移动左指针)，并且在「收缩窗口」的判断句外面记录最大窗口。这道题「窗口非法」就是指窗口内的 absolute difference between any two elements 大于 limit

* 使用一般的滑动窗口的想法：
* 
* ➀ 维护 left 和 right 的窗口, 遍历过程中 Left 和 right 交替前移确保滑动窗口内的元素满足要求
* ➁ 滑动过程中保持 maxNumber(最大值) 和 minNumber(最小值) 两个最值。
* ➂ 向右滑动时, 更新 maxNumber 和 minNumber。
* ➃ 当 maxNumber 和 minNumber 的差大于 limit 时, 窗口缩小。
! ➄ 问题是, 窗口缩小时, 需要便历窗口内所有数字才能确定 maxNumber 和 minNumber 的大小, 这个过程时间复杂度是 O(n), 令算法整体时间复杂度到了O(n^2)。
* ➅ 那么, 如何在更短的时间内确定 maxNumber(最大值) 和 minNumber(最小值) 的大小呢？

? 来自 https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/solution/shi-jian-fu-za-du-onshuang-xiang-dui-lie-0pzn/

* ➆ 如果遍历求滑动窗口内的最大值和最小值, 时间复杂度是 O(n), 肯定会超时。降低时间复杂度的一个绝招就是增加空间复杂度：利用更好的数据结构。是的, 我们的目的是快速让一组数据有序, 那就寻找一个内部是有序的数据结构呗！在 Python 中 sortedcontainers  实现了有序的容器。

? 思路来自: https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/solution/he-gua-de-shu-ju-jie-gou-hua-dong-chuang-v46j/

/ 时间复杂度：O(nlogn)，其中 n 是数组长度。向有序集合中添加或删除元素都是 O(logn) 的时间复杂度。每个元素最多被添加与删除一次。
/ 空间复杂度：O(n)，其中 n 是数组长度。最坏情况下有序集合将和原数组等大


#? 从暴力法到滑动窗口到单调队列的思考过程: https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/solution/pythonhua-dong-chuang-kou-dan-diao-zhan-90tea/
"""


from sortedcontainers import SortedList


class Solution(object):
    def longestSubarray(self, nums, limit):

        maxLen = 0
        
        sortedList = SortedList([])

        left = 0
        right = 0

        while right < len(nums):
            rightNum = nums[right]
            sortedList.add(rightNum)
            
            #* 如果此时窗口内最大值和最小值的差 大于 limit, 则 left 指针右移从而缩小窗口, 直至窗口内最大值和最小值的差 小于等于 limit 为止
            while abs(sortedList[-1] - sortedList[0]) > limit:
                leftNum = nums[left]
                sortedList.discard(leftNum)
                left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen



