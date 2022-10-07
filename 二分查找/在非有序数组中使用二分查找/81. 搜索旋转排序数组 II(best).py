""" 
* 使用 33 的代码无法成功的原因就是当 nums = [1,1,2,1], target = 2 的时候无法分清 mid 处在哪边的有序数组, 像 mid = 1, 在代码中被归结到右边的有序数组中, 实际上它属于左边的有序数组. 这样一判断错误, 永远无法找到 target
? https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/solution/er-fen-cha-zhao-by-liweiwei1419/
? https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/solution/81sou-suo-xuan-zhuan-pai-xu-shu-zu-ii-er-fen-cha-z/
"""


class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[left]:
                # * [left, mid] 之间是有序的
                if nums[left] <= target <= nums[mid]:
                    # * 如果 target 在 [left, mid] 间, 这个区间也会是下一轮的搜索区间
                    right = mid
                else:
                    # * 否则区间取反 下一轮搜索区间是 [mid + 1, right]
                    left = mid + 1
            elif nums[mid] < nums[left]:
                #! 为了保持 "分支逻辑和中位数取法不匹配(见模板代码)"这一条件, 代码中认为 [mid + 1, right] 是有序的
                if nums[mid + 1] <= target <= nums[right]:
                    # * 如果target 在 [mid + 1, right] 间, 这个区间也会是下一轮的搜索区间
                    left = mid + 1
                else:
                    right = mid
            else:
                # / 注意, 这里还要考虑只剩两个元素的情况: 像 "nums = [1,3], target = 1" 也被归到这个 else 里面了, 所以在排除现有的 left 之前要先判断一下当前的 mid/left 是否是目标值, 如果是目标值直接返回 true
                if nums[mid] == target:
                    return True
                else:
                    left += 1

        return nums[left] == target


print(Solution().search([2, 1], 1))
