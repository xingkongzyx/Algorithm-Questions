"""
/ 左、中、右三个位置的值相比较，有以下几种情况： 
/ 1. 左值 < 中值, 中值 < 右值 ：没有旋转，最小值在最左边，可以收缩右边界 
/ 2. 左值 > 中值, 中值 < 右值 ：有旋转，最小值在左半边，可以收缩右边界 
/ 3. 左值 < 中值, 中值 > 右值 ：有旋转，最小值在右半边，可以收缩左边界 
/ 4. 左值 > 中值, 中值 > 右值 ：单调递减，不可能出现
/ 分析前面三种可能的情况, 会发现情况1、2是一类, 情况3是另一类。 
/ 如果中值 < 右值，则最小值在左半边，可以收缩右边界。
/ 如果中值 > 右值，则最小值在右半边，可以收缩左边界。

! 而情况1与情况3都是左值 < 中值，但是最小值位置范围却不同，这说明，如果只比较左值与中值，不能确定最小值的位置范围。
> 通过比较中值与右值，可以确定最小值的位置范围，从而决定边界收缩的方向。
> 所以最后收缩的结果就是当left与right重合, 此时它们指向的位置就是最小值
* 在while循环内, nums[mid]要么大于要么小于nums[right]，不会等于。因为循环条件是 left < right, 并且left的计算方式是向下取整的, 所以left在最后一次循环与left重合, 但绝对不会与right重合, 所以 nums[mid] != nums[right]

# 这个二分的目的,是将目标最小值套住, 通过判断mid与左右的大小关系, 将单调递增的那部分去除掉, 最后剩下的就是不连续的那个点。 问题来了, 如果我们是 mid 比较 right, 因为是找最小值, 如果mid < right,立即能判断出来mid到right之间都递增, 最小值必不在其中(mid仍可能), 因此能移动right. 
# ******但如果left < mid, 左侧递增, 你能直接排除left到mid吗******
# 并不能,因为最小数可能就在left上,你无法据此把这部分排除出去。 这里存在一个取巧办法: 当 nums[left] < nums[right] 时, nums[left] 就是最小值, 因为在收缩过程中, 如果 "nums[left] > nums[right]",说明不连续的点仍然在 [left, right] 中间,一旦nums[left] <= nums[right], 说明这个区间已经连续递增, 这只能说明, 
! 之前的left指针收缩, 将左半边那个连续的区间正好排除出去,才导致[left, right]成为递增区间,所以left就是右半区间的第一个元素。
 """

""" 
! 题目让找出两个单增区间的边界, 这个边界所在的位置就是一般二分搜索中的target

? 为什么只能跟 nums[right] 比较而不能跟 nums[left] 比较呢?
? 超级好的讲解: https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solution/er-fen-cha-zhao-wei-shi-yao-zuo-you-bu-dui-cheng-z/
"""

class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            # * 如果nums[mid] < nums[right], mid 处在右边的单增区间中, "边界所在的位置"应该在mid或者mid的左侧
            if nums[mid] < nums[right]:
                right = mid
            # * 如果 nums[mid] > nums[right], 则说明 mid 处在左边的单增区间，"边界所在的位置"在mid的右侧，所以我们让 left = mid + 1; 由于 "nums[mid] > nums[right]" 所以此时mid所在的位置肯定不是最小值, 最小值在 [mid+1, right] 区间
            elif nums[mid] > nums[right]:
                left = mid + 1

        """ 
        # ! 由于设定的是 left < right 退出循环, 说明此时nums还剩下两个元素, 那么 mid 与 right 永远不会重合, 所以上面没有判断 nums[mid] == nums[right]. 最后循环到的情况可能是 [10,1] 或者 [1,10], 经过推算发现最后left指向的位置就会是最小值，也就是旋转点的位置
        """
        return nums[left]
