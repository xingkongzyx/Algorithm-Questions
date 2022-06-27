
#? https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/solution/javashuang-zhi-zhen-shi-xian-by-neil2020/
""" 
* 指针 left 从左向右寻找偶数；
* 指针 right 从右向左寻找奇数；
* 将 偶数 nums[left] 和 奇数 nums[right] 交换。
"""
class Solution(object):
    def exchange(self, nums):
        left = 0
        right = len(nums) - 1
        
        while left < right:   
            #* 当找到一个奇数时，就跳出循环。
            while left < right and nums[right] % 2 != 1:
                right -= 1
                
            #* 当找到一个偶数时，就跳出循环。
            while left < right and nums[left] % 2 != 0:
                left += 1
                
            #* 如果两个指针还没有碰到一起时，说明找到了需要交换的位置
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]

        return nums

Solution().exchange(nums = [1,3,5])
