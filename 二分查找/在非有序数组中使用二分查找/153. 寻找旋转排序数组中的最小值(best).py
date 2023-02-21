""" 
> 通过比较中值与右值, 可以确定最小值的位置范围, 从而决定边界收缩的方向。所以最后收缩的结果就是当left与right重合, 此时它们指向的位置就是最小值

* 在while循环内, nums[mid] 要么大于要么小于 nums[right], 不会等于。因为循环条件是 left < right, 并且 mid 的计算方式是向下取整的, 所以 mid 在最后一次循环与 left 重合, 但绝对不会与 right 重合, 所以 nums[mid] != nums[right]

*  这个二分的目的, 是将目标最小值套住, 通过判断 nums[mid] 与左右的大小关系, 将单调递增的那部分去除掉, 最后剩下的就是不连续的那个点。问题来了, 如果我们是 mid 比较 right, 因为是找最小值, 如果 "nums[mid] < nums[right]", 立即能判断出来 mid 到 right 之间都递增, 最小值必不在其中(mid 仍可能), 因此能移动 right. 

# 但如果 left < mid, 左侧递增, 你能直接排除 left 到 mid 吗?
# 并不能, 因为最小数可能就在left上,你无法据此把这部分排除出去。 这里存在一个取巧办法: 当 nums[left] < nums[right] 时, nums[left] 就是最小值, 因为在收缩过程中, 如果 "nums[left] > nums[right]",说明不连续的点仍然在 [left, right] 中间,一旦nums[left] <= nums[right], 说明这个区间已经连续递增, 这只能说明, 
! 之前的left指针收缩, 将左半边那个连续的区间正好排除出去,才导致[left, right]成为递增区间,所以left就是右半区间的第一个元素。


? 为什么只能跟 nums[right] 比较而不能跟 nums[left] 比较呢?
? 超级好的讲解: https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solution/er-fen-cha-zhao-wei-shi-yao-zuo-you-bu-dui-cheng-z/

? https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solution/er-fen-fa-fen-zhi-fa-python-dai-ma-java-dai-ma-by-/
"""


class Solution:
    def findMin(self, nums) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            print(left, mid, right)
            if nums[mid] > nums[right]:
                # * [left, mid] 之间是有序的, 位于第一个递增区间内, mid及其左边一定不是最小值
                # * 下一轮搜索区间 [mid + 1, right]
                left = mid + 1
            elif nums[mid] < nums[right]:
                # ! 这道题因为跟 right 比较,并且 mid 的计算是向下取整, 所以一定不会有 nums[mid] == nums[right], 即使只有两个数 mid 也只会和 left 重合
                # * [mid, right] 之间是有序的, 位于第二个递增区间内, mid 及其左边有可能是最小值
                # * 下一轮搜索区间 [left, mid]
                right = mid
        return nums[left]
