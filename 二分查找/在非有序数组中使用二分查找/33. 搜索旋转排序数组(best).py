
#? https://leetcode.cn/problems/search-in-rotated-sorted-array/solution/er-fen-fa-python-dai-ma-java-dai-ma-by-liweiwei141/
class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                #! 这里就没有下面红色注释的问题, 因为判断条件是严格大于, 即使只有两个数 [2,1] 的时候, "nums[mid] == nums[left]" 不会进入if 循环. 而一般情况, [left, mid] 是有序的完全成立
                #> [left, mid] 是有序的增区间
                if nums[left] <= target <= nums[mid]:
                    #/ 下一轮搜索区间 [left, mid]
                    right = mid
                else:
                    #/ 下一轮搜索区间 [mid + 1, right]
                    left = mid + 1
            else:
                #! 这里weiwei的注释有错误, 考虑到只有两个数的情况, [2,1] 此时 left和mid 重合。一般情况下 [mid, right] 都是有序的, 但因为只有两个数, left==mid, 此时 [2,1] 是无序的, 只能说 [mid+1, right] 对应的数组元素是 [1,1] 是有序的。
                # ? 关于这部分看这里的评论, https://leetcode.cn/problems/search-in-rotated-sorted-array/solution/er-fen-fa-python-dai-ma-java-dai-ma-by-liweiwei141/879444/
                #> 准确的说有序区间是 [mid + 1, right]
                # [mid, right] 是有序区间
                if nums[mid + 1] <= target <= nums[right]:
                    #/ 下一轮搜索区间 [mid + 1, right]
                    left = mid + 1
                else:
                    #/ 下一轮搜索区间 [left, mid]
                    right = mid
        
        return -1 if nums[left] != target else left
