
""" 
> 关键是要从后开始遍历
* 从后开始遍历的好处
* 先比较较大的数，把大的数放到数组nums1的后面
* 如果先从较小的数比较，则nums1的元素可能发生移位后挪，时间复杂度高一些。
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        insertIdx = len(nums1) - 1
        nums1Idx = m - 1
        nums2Idx = n - 1
        while insertIdx >= 0:
            if nums1Idx >= 0 and nums2Idx >= 0:
                num1 = nums1[nums1Idx]
                num2 = nums2[nums2Idx]
                if num1 > num2:
                    nums1[insertIdx] = num1
                    nums1Idx -= 1
                else:
                    nums1[insertIdx] = num2
                    nums2Idx -= 1
            elif nums1Idx >= 0:
                nums1[insertIdx] = nums1[nums1Idx]
                nums1Idx -= 1
            elif nums2Idx >= 0:
                nums1[insertIdx] = nums2[nums2Idx]
                nums2Idx -= 1
            
            insertIdx -= 1
        print(nums1)
Solution().merge(nums1 = [1], m = 1, nums2 = [], n = 0)
