""" 
> 双路快排的思路
"""


class Solution:
    def sortArrayByParity(self, nums):
        # [0, left) 都是偶数
        # [left, right] 是未处理区域
        # (right, len(nums) - 1] 都是奇数
        left = 0
        right = len(nums) - 1

        while left < right:
            while left <= right and nums[left] % 2 == 0:
                left += 1
            while left <= right and nums[right] % 2 == 1:
                right -= 1
            # print("left is ", left, "right is ", right)
            if left >= right:
                break
            nums[left], nums[right] = nums[right], nums[left]
            """ 
            left += 1
            right -= 1
            # 这里与「双路快排」不同的地方在于, 这里没有 update left && right 指针, 原因是这个数字要不是奇数要不是偶数, 无论是什么上面嵌套的内层 while 循环都能更新指针直到推出循环. 当然在这里进行更新, 代码也是正确的
            """
        return nums


print(Solution().sortArrayByParity([3, 1, 5, 9, 4, 8, 2]))
