
# > 这道题 与 1423 非常类似
""" 
* 题意转换:
* 每次都从数组开头和结尾进行取数, 而最终x变为0, 即从开头和结尾取出来的数总和为x
* 而若每次都从数组的开头和结尾处取值, 则剩余未取的数在数组中是连续的, 且其总和为数组总和 sum-x。而题目求的是从开头和结尾拿的最少次数, 等价于求「总长度-余下数」的最大长度
! 即现在问题：求和为 sum - x 的子数组的最大长度

? https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/solution/jiang-x-jian-dao-0-de-zui-xiao-cao-zuo-s-tggw/

"""
class Solution(object):
    def minOperations(self, nums, x):

        target = sum(nums) - x
        if target < 0:
            return -1

        left = 0
        right = 0
        totalSum = 0
        ## 解释一下为什么最开始 maxLen 要置为 -1 而不是0, 因为当遍历过后 maxLen 还是 -1 说明初始两端都大于 x, 没有机会到代码中判等的那段代码, 也就没法做更新。后面若 maxLen 被更新为 0 则代表数组全部之和为 x 这种情况。
        maxLen = -1
       
        while right < len(nums):
            print(left, right, totalSum)
            rightNum = nums[right]            
            totalSum += rightNum
                  
            while totalSum > target:     
                leftNum = nums[left]
                totalSum -= leftNum
                left += 1
            
            if totalSum == target:
                maxLen = max(maxLen, right - left + 1)
            right += 1
        
        if maxLen == -1:
            return -1  
        return len(nums) - maxLen


res = Solution().minOperations([1,2,3,4,5], 15)
print(res)
