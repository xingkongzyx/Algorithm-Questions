""" 
* 给定一个二进制数组, 你可以最多将 1 个 0 翻转为 1, 找出其中最大连续 1 的个数. 

* Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

* 示例 1: 
* 输入: [1,0,1,1,0]
* 输出: 4
* 解释: 翻转第一个 0 可以得到最长的连续 1. 
*       当翻转以后, 最大连续 1 的个数为 4. 

* 注: 
* 输入数组只包含 0 和 1.
* 输入数组的长度为正整数, 且不超过 10,000
"""

#! 窗口中每次循环结束后 [left, right) 包含的就是只含有0个『0』或者1个『0』的子数组
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        ## Step 1
        ## 定义需要维护的变量
        ## 因为是求最大长度, 所以有 maxLen, 又同时涉及计数 (最多将 1 个 0 翻转为 1 翻译就是 满足条件的子数组中 0 的个数不能超过 1 个), 所以还要一个哈希表
        record = {}
        maxLen = 0
        
        ## Step 2: 定义窗口的首尾端 (left, right), 然后滑动窗口
        left = 0
        right = 0
        
        ## Step 3: 更新需要维护的变量 (record, max_len). 
        #! 只要 record 中记录的 0 的个数「小于等于 1 个」, 说明就可以反转这个0变为1(有1个0) 然后计算长度; 或者直接计算目前全是 1 的子数组的长度(有0个0)
        while right < len(nums):
            rightNum = nums[right]
            record[rightNum] = record.get(rightNum, 0) + 1
            
            if record.get(0, 0) <= 1:
                maxLen = max(right - left + 1, maxLen)
            
            ## Step 4
            ## 根据题意, 题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            ## 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            ## 当 record 里面0的个数大于1的时候，窗口不合法
            ## 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (record)
            while record.get(0, 0) > 1:
                leftNum = nums[left]
                record[leftNum] -= 1
                left += 1
            
            right += 1
            
        return maxLen
    
res = Solution().findMaxConsecutiveOnes([1,1,1,1,1,0])
print(res)
