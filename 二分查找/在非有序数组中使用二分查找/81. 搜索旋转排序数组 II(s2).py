""" 
 二分寻找

 解题思路:
  第一类
      当搜索有重复元素的排序数组时，我们会遇到一个问题：如果 
      nums[left] == nums[mid] == nums[right] 时怎么办？比如 [2,1,2,2,2] 和 [2,2,2,1,2], 最开始时, left 指向 第 0 位置, right 指向第 4 位置, mid 指向中间的 2 位置；此时三者相等都为 2。
      > 如果我们想找 1, 而这个 1 可以在 mid 的左边也可以在 mid 的右边。所以就不知道该在哪个区间继续搜索。
      链接：https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/solution/fu-xue-ming-zhu-bang-zhu-ni-geng-shen-ke-zcu0/

  第二类
      [2,3,4,5,6,7,1]这种，也就 "nums[left] < nums[mid]"。此例子中就是2 < 5 ;
      这种情况下，前半部分有序。因此如果 nums[left] <= target < nums [mid]，则在前半部分找，否则去后半部分找。
  第三类
      [6,7,1,2,3,4,5]这种，也就是 "nums[left] > nums[mid]"。此例子中就是6 > 2 ;
      这种情况下，后半部分有序。因此如果 nums[mid] <target <= nums[end] 。则在后半部分找，否则去前半部分找。
""" 



class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        ## 这里使用 = 符号，说明 "left==right==mid" 时也已经与target对比过了, 如果此时还是因为不等于退出了循环, 则一定是没有找到, return False
        while left <= right:
            mid = left + (right - left) // 2
            # print(f"left Idx is {left}, rightIdx is {right}, mid is {mid}")
            if nums[mid] == target:
                return True
            #! 新增的判断语句
            if nums[mid] == nums[left]:
                left += 1
            elif nums[mid] > nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
