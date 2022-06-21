 #? 四道题一起: https://leetcode.cn/problems/search-in-rotated-sorted-array/solution/yi-wen-jie-jue-4-dao-sou-suo-xuan-zhuan-pai-xu-s-2/
 
 #? https://leetcode.cn/problems/search-in-rotated-sorted-array/solution/duo-tu-yan-shi-33-sou-suo-xuan-zhuan-pai-xu-shu-zu/

""" 
分界点，用来分界两个升序数组。

所以我们可以总结以下规律：

1、分界点的左侧元素 >= 第一个元素
2、分界点的右侧元素 < 第一个元素

! 总的来说就是找出有序区间(它属于左边的有序区间还是右边的有序区间)，然后根据target是否在有序区间舍弃一半元素
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while(left <= right):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            #* mid 及其左边的元素都是有序的(也就是在第一个增区间), 它右边的元素可能会出现 "增, 分界点(相当于减), 增". 例如[4,5,7,8,9,2,3] nums[mid]=8, 它后面就是无序的, 而它的左边(包括它本身是有序的). 但是在后面轮次的遍历中右边也是有序的, 因为后面会确定在一个有序区间寻找target, 例如在[4,5,6,7,8]中寻找5. 此时 nums[right]=8, nums[left]=4
            #* 这里必须使用 >=, 因为第二个有序数组的所有values都必然是小于nums[left]的像 [4,5,7,8,9,2,3], [2,3] 必然是小于 [4,5,7,8,9] 的
            if nums[mid] >= nums[left]:
                ## 如果target就在[left, mid) 区间中(mid已经在上面判断过了), 下一轮的搜索区间是 [left, mid-1], nums[left] <= target 使用等号就是因为目前没有排除 nums[left] == target的可能性, 并且下一轮的搜索区间是 [left, mid-1], left也是包含在下一轮的搜索区间的
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    #* 除了上面的情况外，说明target一定在mid后面的区间内, 所以下一轮搜索区间定在 [mid+1, right]
                    left = mid + 1
            #* 此时nums[mid]在第二个增区间, mid 及其右边的元素都是有序的.
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


res = Solution().search(nums=[1], target=0)
print(res)
