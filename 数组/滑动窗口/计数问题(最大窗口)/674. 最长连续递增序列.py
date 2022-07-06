
#> 这道题也能用动态规划解决 
class Solution(object):
    def findLengthOfLCIS(self, nums):
        maxLen = 0
        
        left = 0
        right = 0
        
        while right < len(nums):
            
            if right > 0 and nums[right] > nums[right - 1]:
                maxLen = max(maxLen, right - left + 1)
                
            #* 如果 nums[right - 1]『大于等于』nums[right], 则不满足连续递增的 subsequence 的条件, 缩小滑动窗口, 使得左指针右指针重合, 代表此时连续递增子序列就是当前字符 1 个, 长度为 1 
            if right > 0 and nums[right] <= nums[right - 1]:
                left = right
            
            right += 1        
        return maxLen if maxLen != 0 else 1
