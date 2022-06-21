""" 
? https://leetcode.cn/problems/find-pivot-index/solution/qian-zhui-he-kong-jian-fu-za-du-cong-on-w6zjj/
* 题目中的提到的「pivot index」左边和右边的元素相加的和是不包含「pivot index」位置的；并且，允许「pivot index」左边或者右边的元素为空。
* 首先求得 preSum 数组, 与nums数组的位置一一对应, preSum[0]代表了nums[0]的和, preSum[1] 代表了 nums[0] + nums[1] 的和
/ 从左向右遍历 nums 数组，当遍历到数组的 i 位置时，因为 preSum 的定义方法，
/ preSum[i] 表示包含 i 位置的前面的元素之和。如果将 i 作为「pivot index」, 那么它的左边元素之和就是 preSum[i] - nums[i], 它的右边元素之和就是 〔整个数组所有元素之和 - 到i位置(包含i位置)的前缀和〕☛ 〔preSum[len(nums) - 1] - preSum[i]〕
/时间复杂度: O(n)
/ 空间复杂度: O(1)
"""
class Solution(object):
    def pivotIndex(self, nums):
        preSum = [0 for _ in range(len(nums))]
        preSum[0] = nums[0]
        for i in range(1, len(nums)):
            preSum[i] = preSum[i - 1] + nums[i]
        
        
        for i in range(len(nums)):
            #! 「pivot index」左边和右边的元素相加的和是不包含「pivot index」位置的
            leftSum = preSum[i] - nums[i]
            rightSum = preSum[-1] - preSum[i]
            
            if leftSum == rightSum:
                return i
        return -1




r = Solution().pivotIndex([-1,-1,0,1,1,-1])
print(r)
            
            
