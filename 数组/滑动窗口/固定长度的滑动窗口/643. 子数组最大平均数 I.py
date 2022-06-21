
# ! 滑动窗口过程中，仅计算最大sum数值，待全部计算完成后，再做平均
#* 在每次循环结束的时候(right更新后) nums[left...right) 表示长度为 k-1 的子数组
class Solution(object):
    def findMaxAverage(self, nums, k):
        ## Step 1: 定义需要维护的变量们(这里是目前的和sum, 以及题目需要的最大average)
        sum = 0
        # > 因为有负数的因素，这里初始化为 "负无穷" 非常重要
        maxSum = float('-inf')
        
        ## Step 2: 定义窗口的首尾端 (left, right)， 然后滑动窗口
        left = 0
        right = 0
        
        while right < len(nums):
            ## Step 3: 更新需要维护的变量, 这里只需要更新 sum
            rightNum = nums[right]
            sum += rightNum
            
            ## 属于 Step 4 - 情况1
            ## 如果题目的窗口长度固定：用一个if语句判断一下当前窗口长度是否达到了限定长度. 如果达到了，窗口左指针前移一个单位，从而保证下一次右指针右移时，窗口长度保持不变, 
            ## 左指针移动之前, 先更新Step 1定义的维护变量 
            if (right - left + 1) == k:
                ## 更新 (部分或所有) 维护变量 
                maxSum = max(sum, maxSum)
                leftNum = nums[left]
                sum -= leftNum
                ## 窗口左指针前移一个单位保证下一次右指针右移时窗口长度保持不变
                left += 1
                
            right += 1
            
        ## Step 5: 返回答案
        return maxSum / k
res = Solution().findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4)
print(res)
