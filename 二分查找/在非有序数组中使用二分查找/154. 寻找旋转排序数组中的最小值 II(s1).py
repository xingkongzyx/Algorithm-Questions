 
 #? 综合性讲解 https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/solution/154-find-minimum-in-rotated-sorted-array-ii-by-jyd/
 
 #/ 关于细节很好的讲解(包括为什么要与右段尾部进行比较，而不与左段头部进行比较，明明也有类似的效果？ 为什么变化时right = mid；而left = mid + 1？为什么nums[mid] == nums[right]时，直接将right--，再继续比较就可以，这样不会出现问题吗？): https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/solution/di-zi-dui-guan-fang-ti-jie-er-fen-fa-de-omkrg/
 
 #? 一般性情况的图画: https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/solution/tong-guo-hua-tu-lai-shen-ke-li-jie-er-fen-fa-by-ch/

#! 与旋转数组I非常类似,唯一的不同就是有重复元素

class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            elif nums[mid] == nums[right]:
                #> 与153相比新增加的情况
                right -= 1
        return nums[left]
