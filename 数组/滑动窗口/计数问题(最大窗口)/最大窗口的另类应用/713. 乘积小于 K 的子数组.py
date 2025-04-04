
#> 求最大窗口，所以在窗口非法时「收缩窗口」(也就是移动左指针)，并且在「收缩窗口」的判断句外面记录最大窗口。这道题「窗口非法」就是指窗口内的数字的乘积 >= k
#* 每次 while 循环结束后 nums[left...right) 区间内的数字的乘积 mul 都是严格小于 k 的，所以需要获得「以 right 结尾」的子数组的数量，方法就是在循环中 "right += 1" 前使用 "count += (right-left+1)" 记录数量
#? https://leetcode.cn/problems/subarray-product-less-than-k/solution/jian-dan-yi-dong-xiang-xi-zhu-jie-shuang-jvy3/
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):    
        count = 0
        mul = 1
        
        left = 0
        right = 0
        while right < len(nums):
            rightNum = nums[right]
            mul *= rightNum 
            
            """
            ! 对于这道题而言将更新count的语句放在这里是不正确的! 以 [10, 5, 2, 6] 举例, 当 left=10, right=2, mul=100 此时不满足「严格小于k」的条件, 只能移动左指针到 left=5. 移动后的滑动窗口的区间变为 [5,2] 是满足条件的, 退出「while mul >= k」 的循环. 但在结束左指针的前移后没有更新count便进入了下一轮 while 循环, right 进行了更新变为 right=6, 这时进行记录便会缺少『以5结尾的满足要求的子数组』
            if mul < k:
                count += (right - left + 1)  
            """     
            ## 这里 left 一定要有 ｢<=｣ right 的条件, 这样在满足 mul >= k 条件时 left 会更新到等于 right + 1(nums = [12,1,3], k=0), 再更新 count 时 right-left + 1 = 0, 最后的结果会是正确的. 像这里的例子, left=1, right=0, count += 0, 最后能获得正确的答案
            while mul >= k and left <= right:
                leftNum = nums[left]
                mul //= leftNum
                left += 1
            
            """ 
            *每次右指针位移到一个新位置，应该加上 x 种数组组合：
            *  nums[right]
            *  nums[right-1], nums[right]
            *  nums[right-2], nums[right-1], nums[right]
            *  nums[left], ......, nums[right-2], nums[right-1], nums[right]
            * 共有 right - left + 1 种
            ? https://leetcode.cn/problems/subarray-product-less-than-k/solution/jian-dan-yi-dong-xiang-xi-zhu-jie-shuang-jvy3/
            """
            count += (right - left + 1)            
            right += 1
            
        print(count)
        return count

Solution().numSubarrayProductLessThanK(nums = [2,2,2], k = 8)
