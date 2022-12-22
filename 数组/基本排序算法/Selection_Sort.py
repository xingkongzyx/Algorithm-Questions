# 首先在未排序序列中找到最小元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

class Solution:
    def sortArray(self, nums):
        # 循环不变量: [0, i) 有序, 且该区间里所有元素就是最终排定的样子
        for i in range(0, len(nums)):
            # 选择区间 [i, len - 1] 里最小的元素的索引, 交换到下标 i
            minIdx = i
            for j in range(i, len(nums)):
                if nums[j] < nums[minIdx]:
                    minIdx = j

            nums[minIdx], nums[i] = nums[i], nums[minIdx]

        return nums
