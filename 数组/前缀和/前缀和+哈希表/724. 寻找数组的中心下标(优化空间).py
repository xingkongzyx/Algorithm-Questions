""" 
* 第 i 数字为中间数的条件为: pre_sum[i] - nums[i] == totalSum - pre_sum[i]
* 
* 由于我们不再关心之前已经使用过的前缀和，可以把前缀和数组优化为一个数

/ 时间复杂度: O(n)
/ 空间复杂度: O(1)
"""
class Solution(object):
    def pivotIndex(self, nums):
        numsSum = sum(nums)
        preSum = 0
        
        for i in range(len(nums)):
            preSum += nums[i]
            leftSum = preSum - nums[i]
            rightSum = numsSum - preSum
            if leftSum == rightSum:
                return i
        
        return -1
