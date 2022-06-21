
""" 
* 单调性: 假设我们选择了除数 d, 当 d 增加时, 正整数数组 nums 中的每个数 num[i] 除以 d 的结果 num[i] / d 单调递减, 它们的和 total 同样也单调递减。
/ 时间复杂度：O(N * log max(nums))，这里 N 是数组的长度，每一次二分都执行了边界判断函数，都得遍历一遍数组；
"""
class Solution:
    def smallestDivisor(self, nums, threshold):
        #* 二分查找的下限是 1, 这是最小的正整数。而二分查找的上限可以设置为数组 nums 中的最大值 M(也就是max(nums)), 这是因为当除数 d >= M 时, 数组 nums 中的每个数除以 d 的结果均为 1, divisionResult 的值恒等于数组 nums 的长度。由于题目中要求除数尽可能小, 那么选择除数 d = M 一定比 d > M 更优。因此, 将二分查找的上限设置为 M(也就是max(nums)), 可以保证不遗漏最优解。

        left = 1
        right = max(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            divisionResult = self.calculateDivision(mid, nums)
            
            if divisionResult > threshold:
                left = mid + 1
            else:
                right = mid
                
        return left
    
    def calculateDivision(self, divisor, nums):
        result = 0
        import math
        for num in nums:
            result += math.ceil(num / divisor)
        
        return result 

print(Solution().smallestDivisor(nums = [44,22,33,11,1], threshold = 5))
