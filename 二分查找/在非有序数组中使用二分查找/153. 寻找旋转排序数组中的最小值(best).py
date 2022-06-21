
#? https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solution/er-fen-fa-fen-zhi-fa-python-dai-ma-java-dai-ma-by-/
class Solution:
    def findMin(self, nums) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            print(left, mid, right)
            if nums[mid] > nums[right]:
                # [left, mid] 之间是有序的, 位于第一个递增区间内, mid及其左边一定不是最小值
                # 下一轮搜索区间 [mid + 1, right]
                left = mid + 1
            elif nums[mid] < nums[right]:
                # ! 这道题因为跟right比较,并且mid的计算是向下取整,所以一定不会有 nums[mid] == nums[right], 即使只有两个数 mid 也只会和 left 重合
                # [mid, right] 之间是有序的, 位于第二个递增区间内, mid 及其左边有可能是最小值
                # 下一轮搜索区间 [left, mid]
                right = mid
        return nums[left]
