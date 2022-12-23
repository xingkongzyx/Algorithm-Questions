""" 
> 三路快排
"""

import random


class Solution(object):
    def sortArray(self, nums):
        left = 0
        right = len(nums) - 1
        self.quickSort(left, right, nums)
        return nums

    def quickSort(self, left, right, nums):
        if left >= right:
            return

        randIdx = random.randint(left, right)
        nums[randIdx], nums[left] = nums[left], nums[randIdx]
        pivot = nums[left]

        # 初始化时要保证这两个区间里恰好是空区间, lt 指 less than, gt 指 great than
        lt = left
        gt = right + 1
        """ 
        # 「第一个区间」: nums[left+1, lt] 之中的所有元素「小于」pivot, 
        # 「第二个区间」: nums(lt, i) 之中的所有元素「等于」pivot,  将它定义为开区间, 表示 i 前面的所有的元素我我们都看过, i 当前我们要看的这个位置的元素
        # 「第三个区间」: nums[gt, right] 之中的所有元素「大于」pivot
        lt 是第一个区间里的「最后一个位置」
        lt + 1 是第二个区间里的「第一个位置」
        gt 是第三个区间里的「第一个位置」
        """
        i = left + 1
        # 当 i 恰好等于 gt 的时候, 循环不需要继续下去. 因为重合的那个位置的值我们已经看到过了, 所以循环可以继续的条件是 i「严格小于」gt
        while i < gt:
            if nums[i] < pivot:
                lt += 1
                nums[i], nums[lt] = nums[lt], nums[i]
                i += 1
            elif nums[i] == pivot:
                i += 1
            elif nums[i] > pivot:
                # 这个时候 i 就不能够向右移动了, 因为交换回来的这个元素我们还要让下一轮看到, 这就是这个 while 循环不能将它写成 for 循环的原因
                gt -= 1
                nums[i], nums[gt] = nums[gt], nums[i]

        # 在遍历完成以后, 我们还要将 pivot 交换到它对应的位置. 因为第二个区间里的所有的元素都等于 pivot, 我们应该将第一个区间里的最后一个位置和 left 进行交换, 所以我们要交换的是 lt 和 left 位置的值. lt 这个位置的元素的值在交换完成以后就等于 pivot 了
        nums[left], nums[lt] = nums[lt], nums[left]

        # 所以下一轮我们要递归的处理 lt 前面的那个区间, lt 前面的那个区间是什么呢？就是 left 到 lt - 1 这个区间
        self.quickSort(left, lt - 1, nums)
        # gt 这个位置的值恰好就是大于 pivot 区间的第一个位置, 所以后面处理的这个区间就是 gt到 right
        self.quickSort(gt, right, nums)
