
#? 类比 424的解法 - 最大窗口技巧
#? 参考: https://leetcode.cn/problems/max-consecutive-ones-iii/solution/hua-dong-chuang-kou-chuang-kou-chang-du-jian-xiao-/
"""
【最大窗口解法】- 窗口只增不减

核心思想：
因为最终要求的是最长的滑动窗口，所以比当前窗口更小的窗口没有意义。
当窗口无效时，保持窗口大小不变（左右指针同步移动），而不是收缩到有效状态。

关键变量：
- numOfOnes：当前窗口 [left, right] 内 1 的个数（不是历史最大值！）
- 窗口大小：right - left + 1

不变量：
窗口大小始终等于历史最大有效窗口的大小

判断条件：
- numOfOnes + k >= windowSize → 窗口有效，可以继续扩大
- numOfOnes + k < windowSize → 窗口无效，左边界右移一步（保持窗口大小）

窗口变化规则：
1) 窗口增大：当 numOfOnes + k >= windowSize 时，only right++，窗口扩大
2) 窗口平移：当 numOfOnes + k < windowSize 时，left++ 和 right++ 同步，窗口大小不变

为什么正确？
- 我们只关心最大值，比当前窗口更小的有效窗口不会更新答案
- 保持窗口大小，等待找到更好的位置即可
"""
class Solution(object):
    def longestOnes(self, nums, k):
        """
        最大窗口解法：窗口只增不减
        
        不变量：窗口大小始终等于历史最大有效窗口的大小
        numOfOnes：当前窗口 [left, right] 内 1 的个数
        
        判断条件：numOfOnes + k < windowSize 表示窗口无效
        （即使把 k 个 0 变成 1，1 的个数也不够填满窗口）
        """
        left = 0
        right = 0
        numOfOnes = 0  # 当前窗口内 1 的个数
        maxLen = 0
        
        while right < len(nums):
            rightNum = nums[right]
            
            # 右边界扩展，更新 1 的计数
            if rightNum == 1:
                numOfOnes += 1
            
            # 窗口无效时，左边界右移一步（保持窗口大小不变）
            if numOfOnes + k < right - left + 1:
                leftNum = nums[left]
                if leftNum == 1:
                    numOfOnes -= 1
                left += 1
            
            # 更新最大长度（此时窗口大小就是历史最大）
            maxLen = max(maxLen, right - left + 1)
            right += 1
        
        return maxLen
res = Solution().longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2)
print(res)
