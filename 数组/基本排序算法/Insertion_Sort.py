""" 
插入排序的核心思想是遍历整个数组, 保持当前元素左侧始终是排序后的数组, 然后将当前元素插入到前面排序完成的数组的对应的位置, 使其保持排序状态。有点动态规划的感觉, 类似于先把前i-1个元素排序完成, 再插入第i个元素, 构成i个元素的有序数组。
"""


class Solution:
    def sortArray(self, nums):
        # 将 nums[i] 插入到区间 [0, i) 使之成为有序数组
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                else:
                    break

        return nums
