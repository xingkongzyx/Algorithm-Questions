import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        # * 「第 1 大」的元素所在的位置是 len(nums) - 1,「第 2 大」的元素所在的位置是 len(nums) - 2,「第 k 大」的元素所在的位置是 len(nums) - k
        target = len(nums) - k
        while True:
            pivotIdx = self.partition(left, right, nums)
            # 如果通过 partition 函数排序好的 pivotIdx 不属于「第 k 大的元素」应该在的位置, 则根据不同的情况对其左边或者右边接着进行排序
            if pivotIdx == target:
                return nums[pivotIdx]
            elif pivotIdx < len(nums) - k:
                left = pivotIdx + 1
            else:
                right = pivotIdx - 1

    # > 双路快排的代码
    def partition(self, left, right, nums):
        # 先「随机选择」切分的元素的位置, 在这版代码中体现为随机选择 [left, right] 之间的某个位置作为 randIdx, 为了不破坏剩下的 code, 获取到 randIdx 后将其与 nums[left] 交换，这样随机选择的元素又回到了 nums[left] 的位置, 不需要改变剩下的代码
        randIdx = random.randint(left, right)
        nums[randIdx], nums[left] = nums[left], nums[randIdx]
        pivot = nums[left]

        # 初始化时要保证这两个区间里恰好是空区间
        le = left + 1
        ge = right
        # ! pivot 后面的第一个区间 nums[left+1, le) 之中的所有元素「小于等于」pivot, pivot 后面的第二个区间 (ge, right] 之中的所有元素「大于等于」pivot. le, ge 都表示是接下来要看到的元素的 index

        # 遍历的过程中使用le, ge 在区间的头和尾进行遍历
        while True:
            while le <= ge and nums[le] < pivot:
                le += 1
            while le <= ge and nums[ge] > pivot:
                ge -= 1

            # 此时, le 来到了第一个大于等于pivot的位置, ge 来到了第一个小于等于pivot的位置
            if le >= ge:
                # 如果 le 与 ge 重合的话, le 所在的位置的值与 ge 所在的位置的值是相等的, 都等于 pivot
                break

            # 细节：相等的元素通过交换，等概率分到数组的两边
            nums[le], nums[ge] = nums[ge], nums[le]
            le += 1
            ge -= 1

        nums[left], nums[ge] = nums[ge], nums[left]
        return ge
