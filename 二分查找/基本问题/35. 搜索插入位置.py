""" 
? https://leetcode.cn/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/
* ⑴ 题目要找的元素是：第一个大于等于 target 的元素的下标；
* ⑵ 数组的长度 len 也有可能是问题的答案，代码中设置 right = len 不是因为设置区间是「左闭右开」，而是因为 len 位置本来就有可能是问题的答案(如果 target 大于数组中的所有元素, 那么 target 的插入位置就应该是 len)。
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                # 下一轮搜索区间变为[mid + 1, right]
                left = mid + 1
            else:
                # 下一轮搜索区间变为[left, mid]
                right = mid
        return left
