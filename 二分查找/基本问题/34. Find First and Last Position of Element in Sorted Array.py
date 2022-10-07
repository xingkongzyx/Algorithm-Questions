""" 
#! 根据排除法的思路, 也就是 nums[mid] 严格大于或者小于 target, 那么mid位置就一定不是所求
? https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/solution/si-lu-hen-jian-dan-xi-jie-fei-mo-gui-de-er-fen-cha/

"""


class Solution(object):
    def searchRange(self,  nums,  target):
        if len(nums) == 0:
            return [-1,  -1]
        return [self.findFirstIdx(nums,  target),  self.findLastIdx(nums,  target)]

    # * 寻找的是第一个大于等于 target 的位置，所以 "nums[mid] < target" 时一定不是答案

    def findFirstIdx(self,  nums,  target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                # 此时的搜索区间应变为 [mid + 1,  right]
                left = mid + 1
            else:
                # 否则搜索区间应变为 [left,  mid]
                right = mid
        if nums[left] == target:
            return left
        else:
            return -1

    # * 寻找的是最后小于等于 target 的位置，所以 "nums[mid] > target" 时一定不是答案

    def findLastIdx(self,  nums,  target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        if nums[left] == target:
            return left
        else:
            return -1
