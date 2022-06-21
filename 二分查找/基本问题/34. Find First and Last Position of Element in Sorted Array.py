class Solution(object):
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        return [self.findFirstIdx(nums, target), self.findLastIdx(nums, target)]

    #! 根据排除法的思路，也就是 nums[mid] 严格大于或者小于 target，那么mid位置就一定不是所求
    """ 
    # 其实从这两个分支(严格大于或者小于)的反面去理解可能好理解一点：
    * nums[mid] < target（对应区间 [mid + 1, right]）的反面是：nums[mid] >= target，对应的区间是 [left, mid]。

    * 换句话说：[left, mid] 这个区间内所有的元素满足的性质是 >= target，如果看到的中间元素 mid 恰好等于 target，它有可能是第 1 次出现的元素，它的前面的位置也有可能是第 1 次出现的元素，但是区间 [left, mid - 1] 一定不会是最后出现的那个位置。

    * 你紧紧盯着 [left, mid] 这个区间能找到的什么， mid 往前面看只能找到第 1 次出现的位置。

    * 再说一遍就是 nums[mid] >= target 的时候，只能往前看，找到第 1 次出现的下标。
    """
    def findFirstIdx(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                # 此时的搜索区间应变为 [mid + 1, right]
                left = mid + 1
            else:
                # 否则搜索区间应变为 [left, mid]
                right = mid
        if nums[left] == target:
            return left
        else:
            return -1
    def findLastIdx(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        if nums[left] == target:
            return left
        else:
            return -1
