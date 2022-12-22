# 第二种方法(随机选择 pivot)能够通过 17/18 的测试
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

        pivotIdx = self.partition(left, right, nums)
        # 经过 partition 后我们就排定了一个元素(pivot element)的位置, 接下来就是递归对这个位置前面的区间还有后面的区间进行同样的处理
        self.quickSort(left, pivotIdx - 1, nums)
        self.quickSort(pivotIdx + 1, right, nums)

    def partition(self, left, right, nums):

        # 先「随机选择」切分的元素的位置, 在这版代码中体现为随机选择 [left, right] 之间的某个位置作为 randIdx, 为了不破坏剩下的 code, 获取到 randIdx 后将其与 nums[left] 交换，这样随机选择的元素又回到了 nums[left] 的位置, 不需要改变剩下的代码
        randIdx = random.randint(left, right)
        nums[randIdx], nums[left] = nums[left], nums[randIdx]
        pivot = nums[left]

        # ! 循环不变量: pivot 后面的第一个区间 nums[left+1, j] 之中的所有元素「小于等于」pivot, pivot 后面的第二个区间 (j, i) 之中的所有元素「大于」pivot, i 表示是接下来要看到的元素的 index
        # # j 就是指 pivot 后面的两个区间里第一个区间的最后一个位置,  j 取 left 的时候, 上述两个区间恰好都是空区间
        j = left
        for i in range(left + 1, right + 1):
            # > 大放过, 小交换到前面
            if nums[i] <= pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]
        return j
