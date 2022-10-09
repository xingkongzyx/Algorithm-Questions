""" 
* 可以发现，每一对「偶数下标, 奇数下标」的数肯定是相等的，因此，我们可以利用这条特性来进行二分查找。也就是 数组应该呈现为nums[0] == nums[1], nums[2] == nums[3]的形式
* 如果 mid 所在的「偶数下标, 奇数下标」的值相等，说明前面半段没有缺失的数，那么，缺失的数肯定在后半段，反之，则在前半段。
? https://leetcode.cn/problems/single-element-in-a-sorted-array/solution/tong-ge-lai-shua-ti-la-er-fen-cha-zhao-b-x8dd/

* 初始时, 二分查找的左边界是 0, 右边界是数组的最大下标。每次取左右边界的平均值 mid 作为待判断的下标, 根据 mid 的奇偶性决定和左边或右边的相邻元素比较：
* if mid is 「even」, then it's duplicate should be in next index, 所以比较 nums[mid] 和 nums[mid+1] 是否相等
* if mid is 「odd」, then it's duplicate should be in previous index, 所以比较 nums[mid-1] 和 nums[mid] 是否相等
/ 时间复杂度: O(log n), 其中 n 是数组 nums 的长度。需要在全数组范围内二分查找, 二分查找的时间复杂度是 O(log n)。
/ 空间复杂度: O(1)

? 外网讲解: https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/627921/Java-or-C%2B%2B-or-Python3-or-Easy-explanation-or-O(logn)-or-O(1)
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            # * 如果 mid 是「偶数」, 则比较  nums[mid] 和 nums[mid+1] 是否相等
            if mid % 2 == 0:
                # * 如果相等，说明分割点在该点右边，下一轮搜索区间 [mid + 1, right]
                if nums[mid] == nums[mid + 1]:
                    left = mid + 1
                # * 如果不相等，那么说明该点及其左边可能是分割点, 下一轮搜索区间 [left, mid]
                else:
                    right = mid
            else:
                # * 如果 mid 是「奇数」, 则比较 nums[mid-1] 和 nums[mid] 是否相等
                # * 如果相等，说明分割点在该点右边，下一轮搜索区间 [mid + 1, right]
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    # * 如果不相等，那么说明该点及其左边可能是分割点, 下一轮搜索区间 [left, mid]
                    right = mid

        return nums[left]
