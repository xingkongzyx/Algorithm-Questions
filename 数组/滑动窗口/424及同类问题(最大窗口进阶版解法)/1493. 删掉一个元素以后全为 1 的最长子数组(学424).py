
#* 使用滑动窗口的原因: 如果找到了一个长度为 L 且删除 1 个字符以后不能保证当前数组范围内全部都是 1 的子数组，那么左边界相同、长度更长的子数组一定不符合要求。符合滑动窗口性质：向右边扩散得到和越来越大，向左边界扩散得到和越来越小。
#! 这种解法与 487 1004 思路一致，但是中间有无用的缩小滑动窗口的行为. 既然只对最长有效的子数组感兴趣，所以我们的滑动窗口不需要收缩，即使窗口可能覆盖无效的子数组。
class Solution(object):
    def longestSubarray(self, nums):     
        oneCount = 0
        maxOneCount = 0
        maxLen = 0
        
        left = 0
        right = 0
        k = 1 
        
        while right < len(nums):
            rightNum = nums[right]
            if rightNum == 1:
                oneCount += 1
                
            maxOneCount = max(oneCount, maxOneCount)
            
            if right - left + 1 <= maxOneCount + k:
                maxLen = max(maxLen, right - left + 1)

            if right - left + 1 > maxOneCount + k:
                leftNum = nums[left]
                if leftNum == 1:
                    oneCount -= 1
                left += 1
            
            right += 1
            
        #! 因为这道题是可以「删掉一个元素」而不是替换, 所以最后返回的是 「maxLen - 1」; 但像 424, 1004 都是替换元素, 返回的就是 maxLen   
        return maxLen - 1
print(Solution().longestSubarray(nums = [1,1,1]))
