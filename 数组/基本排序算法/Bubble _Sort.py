""" 
冒泡排序是从左到右依次比较相邻的两个元素, 如果前一个元素比较大, 就把前一个元素和后一个交换位置, 遍历数组之后保证最后一个元素相对于前面的永远是最大的。然后让最后一个保持不变, 重新遍历前n-1个元素, 保证第n-1个元素在前n-1个元素里面是最大的。依此规律直到第2个元素是前2个元素里面最大的, 排序就结束了。因为这个排序的过程很像冒泡泡, 找到最大的元素不停的移动到最后端, 所以这个排序算法就叫冒泡排序。

「冒泡排序」有个特点：在遍历的过程中, 提前检测到数组是有序的, 从而结束排序, 而不像「选择排序」那样, 即使输入数据是有序的, 「选择排序」依然需要「傻乎乎」地走完所有的流程。
"""


class Solution:
    def sortArray(self, nums):
        for i in range(0, len(nums) - 1):
            sorted = True
            for j in range(1, len(nums) - i):
                if nums[j-1] > nums[j]:
                    sorted = False
                    nums[j-1], nums[j] = nums[j], nums[j-1]

            if sorted == True:
                return nums

        return nums
