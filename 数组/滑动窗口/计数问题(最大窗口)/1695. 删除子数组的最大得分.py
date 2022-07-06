
#> 求最大窗口，所以在窗口非法时「收缩窗口」(也就是移动左指针)，并且在「收缩窗口」的判断句外面记录最大窗口。这道题「窗口非法」就是指窗口内出现了重复数字，不再满足题目要求的「erase a subarray containing unique elements」
class Solution(object):
    def maximumUniqueSubarray(self, nums):
        ## Step 1: 定义需要维护的变量, 本题求Maximum Erasure Value，所以需要定义 maxScore 以及 窗口内的和 sum, 该题又涉及去重，因此还需要一个哈希表
        maxScore = 0
        sum = 0
        record = {}
        
        ## Step 2: 定义窗口的首尾端 (left, right)， 然后滑动窗口
        left = 0
        right = 0
        
        while right < len(nums):
            ## Step 3
            ## 更新需要维护的变量 (maxScore, record)
            ## i.e. 把窗口末端元素加入哈希表，使其频率加1，并更新目前窗口内的数字的和 sum
            rightNum = nums[right]
            sum += rightNum
            record[rightNum] = record.get(rightNum, 0) + 1
                            
            
            ## Step 4: 
            ## 根据题意, 题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            ## 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            ## 当窗口长度大于哈希表长度时候 (说明目前被删除的子数组存在重复元素)，窗口不合法
            ## 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (sum, record)   
            while len(record) < right - left + 1:
                leftNum = nums[left]
                sum -= leftNum
                record[leftNum] -= 1
                if record[leftNum] == 0:
                    del record[leftNum]
                left += 1
            
            #* 经过「窗口缩小」后，此时 [left, right] 窗口内的元素都是 unique elements, 可以用于计算题目所求的 erasure score
            maxScore = max(maxScore, sum)
            right += 1
            
        return maxScore
            