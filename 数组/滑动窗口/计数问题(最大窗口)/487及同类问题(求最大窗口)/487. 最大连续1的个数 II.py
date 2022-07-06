
#> 求最大窗口，所以在窗口非法时「收缩窗口」(也就是移动左指针)，并且在「收缩窗口」的判断句外面记录最大窗口。这道题「窗口非法」就是指窗口内的「0元素」的个数大于了可翻转的个数 1

#! 窗口中每次循环结束后 [left, right) 包含的就是只含有『0 个 0』或者『1 个 0』的子数组
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
        
        ## Step 3: 更新需要维护的变量 (record). 
        while right < len(nums):
            rightNum = nums[right]
            record[rightNum] = record.get(rightNum, 0) + 1
            
            ## Step 4
            ## 根据题意, 题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            ## 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            ## 当 record 里面0的个数大于1的时候，窗口不合法
            ## 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (record)
            while record.get(0, 0) > 1:
                leftNum = nums[left]
                record[leftNum] -= 1
                left += 1
            
            maxLen = max(right - left + 1, maxLen)
            right += 1
            
        return maxLen
    
res = Solution().findMaxConsecutiveOnes([1,1,1,1,1,0])
print(res)
