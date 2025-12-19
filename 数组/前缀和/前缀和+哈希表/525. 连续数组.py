
#! 为什么不能使用滑动窗口?
#* Sliding window needs a clear break clause in order to know when to stop growing the window and start shrinking it. In this case this condition is much more ambiguous since array only contains elements 0 and 1 which makes sliding window difficult to apply here.

'''
#* 我们在预处理前缀和时, 将 nums[i] 为 0 的值当做 -1 处理. 从而将问题转化为: 
## 如何求得数组中最大连续数组和为0的问题. 此时思路就与 523, 525 一样了. 希望在子区间 [i, j] 找到区间和等于 0 的子数组, 也就是 preSum[i] - preSum[j-1] == 0, 那么相当于遍历nums 数组, 每次更新 preSum, 然后判断在位置 i 之前是否存在位置使得前缀和也为 preSum,  出现过的话, 它们俩相减就能得到为和 0 的子数组, 也就说明『这个子数组的 0 和 1 的数量相同』
'''

class Solution(object):
    def findMaxLength(self, nums):
        from collections import defaultdict

        # / 配合创建Hash表,  记录{总和 : 下标},  由于可能存在 nums 前 N 数字的和刚好满足条件的情况, 我们预制字典{0,-1}来规避该问题. 
        map = defaultdict(int)
        map[0] = -1
        
        preSum = 0
        maxLen = 0
        
        for i in range(len(nums)):
            currentNum = -1 if nums[i] == 0 else 1
            
            preSum += currentNum
            
            if preSum in map:
                maxLen = max(i - map[preSum], maxLen)
            else:
                map[preSum] = i

        return maxLen


s = Solution()
print(s.findMaxLength([0, 1, 0, 1]))
