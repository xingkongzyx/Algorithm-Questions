
""" 
! 为什么两数之和不能使用双指针呢
! 因为两数之和要求返回的是索引下标, 而双指针法一定要排序, 一旦排序之后原数组的索引就被改变了。
"""


class Solution(object):
    def twoSum(self, nums, target):
        record = {}

        for i in range(len(nums)):
            found = target - nums[i]

            if found in record:
                return [record[found], i]

            record[nums[i]] = i

        return [-1, -1]


Solution.twoSum(nums=[2, 7, 11, 15], target=9)
