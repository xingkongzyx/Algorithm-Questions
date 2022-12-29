""" 
* 将数组一分为二, 其中一定有一个是有序的, 另一个可能是有序, 也能是部分有序. 此时, 通过比较边界和 mid 的大小确定哪个部分是有序的, 再对有序部分比较两端, 从而判断target是否在此范围(正因为有序才可以这样做), 如果不在, 就落入另一个可能有序也可能无序的空间再次进行比较. 就这样循环进行查找. 

!与对完全有序的数组进行二分查找的区别: 如果整体都有序, 就直接判断target在哪半边, 一直分下去；现在一半有序, 就先判断有序的是哪边, 然后看target在不在有序的这边, 一直分下去, 相当于多了一个判断哪边有序的步骤(有序那边才能判断target在不在), 其余的和最常规的一样

> 总的来说就是找出有序区间(它属于左边的有序区间还是右边的有序区间), 然后根据target是否在有序区间舍弃一半元素
* 不难发现：将待搜索区间从中间一分为二, 位于中间的元素 nums[mid] 一定会落在其中一个有序区间里. 
? https://leetcode.cn/problems/search-in-rotated-sorted-array/solution/er-fen-fa-python-dai-ma-java-dai-ma-by-liweiwei141/
"""


class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                #! 这里就没有下面红色注释的问题, 因为判断条件是严格大于, 即使只有两个数 [2,1] 的时候, "nums[mid] == nums[left]" 不会进入if 循环. 而一般情况, [left, mid] 是有序的完全成立
                # > [left, mid] 是有序的增区间
                if nums[left] <= target <= nums[mid]:
                    # / 下一轮搜索区间 [left, mid]
                    right = mid
                else:
                    # / 下一轮搜索区间 [mid + 1, right]
                    left = mid + 1
            else:
                #! 这里weiwei的注释有错误, 考虑到只有两个数的情况, [2,1] 此时 left 和 mid 重合. 一般情况下 [mid, right] 都是有序的, 但因为只有两个数, left==mid, 此时 [2,1] 是无序的, 只能说 [mid+1, right] 区间中对应的唯一的元素 [1] 满足有序的条件.
                # ? 关于这部分看这里的评论, https://leetcode.cn/problems/search-in-rotated-sorted-array/solution/er-fen-fa-python-dai-ma-java-dai-ma-by-liweiwei141/879444/
                # > 准确的说有序区间是 [mid + 1, right] 而不是 [mid, right], 原因就是上面两个数的例子. 也可以理解为为了搜索区间统一, 这里必须是 [mid + 1, right], 才能有 left = mid + 1
                if nums[mid + 1] <= target <= nums[right]:
                    # / 下一轮搜索区间 [mid + 1, right]
                    left = mid + 1
                else:
                    # / 下一轮搜索区间 [left, mid]
                    right = mid

        return -1 if nums[left] != target else left
