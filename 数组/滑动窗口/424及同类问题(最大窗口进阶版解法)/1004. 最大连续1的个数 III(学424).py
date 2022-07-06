
#? 类比 424的解法: https://leetcode.cn/problems/max-consecutive-ones-iii/solution/hua-dong-chuang-kou-chuang-kou-chang-du-jian-xiao-/
""" 
因为最终要求的是最长的滑动窗口, 我们可以先找到第一个满足条件的滑动窗口, 之后以该窗口滑动。如果窗口内 maxOneCount + k 小于此时窗口的长度, 则不改变窗口长度继续滑动 (即保持左右指针的相对距离是maxOneCount + k); 如果窗口内 maxOneCount + k 的个数比当前的窗口大, 则扩大窗口长度 (即右指针右移）


链接：https://leetcode.cn/problems/max-consecutive-ones-iii/solution/python3-hua-dong-chuang-kou-de-liang-cho-4xvj/


1) 窗口增大: left不变, right右移, 即right++

什么时候增大? 窗口内的1的数量加上k, 比当前窗口的长度大, 说明k还可以替换更多的0, 此时增大窗口

2) 窗口不变: 当 maxOneCount 没有发生变化的时候, 我们的窗口始终保持着 maxOneCount + k 的长度。也就是新的循环开始, 检查在上次循环中更新的 right += 1 情况下 maxOneCount 是否会变大(也就是新的窗口更新后的 oneCount 数量是否会大于 maxOneCount). 如果没变大, 则在后面的 if 循环中通过 left += 1 缩小窗口, 使得窗口大小恢复 maxOneCount + k

"""
class Solution(object):
    def longestOnes(self, nums, k):
        oneCount = 0
        maxOneCount = 0
        maxLen = 0
        
        left = 0
        right = 0
        
        while right < len(nums):
            rightNum = nums[right]
            if rightNum == 1:
                oneCount += 1
            maxOneCount = max(maxOneCount, oneCount)

            if right - left + 1 <= maxOneCount + k:
                maxLen = max(maxLen, right - left + 1)
                
            if right - left + 1 > maxOneCount + k:
                leftNum = nums[left]
                if leftNum == 1:
                    oneCount -= 1
                left += 1

            right += 1
        return maxLen
res = Solution().longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2)
print(res)
