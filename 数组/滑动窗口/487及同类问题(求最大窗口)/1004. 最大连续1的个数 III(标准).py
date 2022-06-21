
#! 与 487 几乎一模一样, 窗口中每次循环结束后 [left, right) 包含的就是只含有0-k个『0』的子数组
class Solution(object):
    def longestOnes(self, nums, k):

        record = {}
        maxLen = 0
        
        left = 0
        right = 0
        
        while right < len(nums):
            rightNum = nums[right]
            record[rightNum] = record.get(rightNum, 0) + 1
            
            ## 因为滑动窗口代表的含义，所以这句判断放在这里或者循环结束前都可以
            if record.get(0, 0) <= k:
                maxLen = max(right - left + 1, maxLen)
                
            while record.get(0, 0) > k: 
                leftNum = nums[left]
                record[leftNum] -= 1
                left += 1
            
            # if record.get(0, 0) <= k:
            #     maxLen = max(right - left + 1, maxLen)
            
            right += 1
            
        return maxLen
