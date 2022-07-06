""" 
/ 时间复杂度: O(N), N是数组的长度, 我们遍历了一遍数组
/ 空间复杂度: O(1), res, left占用了常数空间。
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        zeroCount = 0
        maxLen = 0
        
        left = 0
        right = 0
        
        while right < len(nums):
            rightNum = nums[right]
            
            if rightNum == 0:
                zeroCount += 1
                
            #* 当 nums[i] 为 0 时, 也就是 zeroCount 的数量大于 0 时, left 指针指向 right 的下一个位置, 这样才能确保 maxLen 的长度正确
            if zeroCount > 0:
                left = right + 1
                zeroCount = 0
            
            #* 此时滑动窗口 [left, right] 内的数字都是 1. 当 nums[right] 是 0 时, 此时的区间是 [right + 1, right], 不是正确的区间, 但也意味着目前区间「consecutive 1」的长度是 0
            maxLen = max(maxLen, right - left + 1)
            right += 1
            
        return maxLen
print(Solution().findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))
