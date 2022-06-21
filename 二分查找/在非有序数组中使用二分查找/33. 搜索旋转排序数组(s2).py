# ?https://leetcode.cn/problems/search-in-rotated-sorted-array/solution/duo-tu-yan-shi-33-sou-suo-xuan-zhuan-pai-xu-shu-zu/ 解法1
#! 这里的findMin 方法来自于 leetcode 153
class Solution(object):
    def search(self, nums, target):
        length = len(nums)
        # * 说明数组是有序的，直接进行二分查找target
        if nums[0] <= nums[length - 1]:
            minIdx = 0
            return self.binarySearch(minIdx, length - 1, target, nums)
        # * 查找最小值的下标
        minIdx = self.findMin(nums)
        print("minIdx is ", minIdx)
        # *如果target在第二个增区间, 最终结果在 [minIdx, length-1], 在这个区间进行常规的binary search
        if nums[minIdx] <= target <= nums[length - 1]:
            return self.binarySearch(minIdx, length - 1, target, nums)
        # *否则, 说明target在 [0, minIdx-1] 区间中, 在这个区间进行常规的binary search
        else:
            return self.binarySearch(0, minIdx - 1, target, nums)

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

        ''' 
        # ! 由于设定的是 left < right 退出循环, 说明此时nums还剩下两个元素, 那么 mid 与 right 永远不会重合, 所以上面没有判断 nums[mid] == nums[right]. 最后循环到的情况可能是 [...,10,1...] 或者 [...,1,10,...], 经过推算发现最后left指向的位置就会是最小值，也就是旋转点的位置
        '''
        return left

    def binarySearch(self, leftIdx, rightIdx, target, nums):
        while leftIdx <= rightIdx:
            midIdx = leftIdx + (rightIdx - leftIdx) // 2
            if nums[midIdx] == target:
                return midIdx
            elif nums[midIdx] < target:
                leftIdx = midIdx + 1
            else:
                rightIdx = midIdx - 1
        return -1


s = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
print("idx of target is ", s)
