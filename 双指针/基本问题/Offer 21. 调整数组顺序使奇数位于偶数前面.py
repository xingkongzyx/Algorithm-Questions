
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
            if nums[left] % 2 == 1:
                left += 1
                continue
            
            if nums[right] % 2 == 0:
                right -= 1
                continue

            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right -= 1

        return nums

Solution().exchange(nums = [1,3,5])
