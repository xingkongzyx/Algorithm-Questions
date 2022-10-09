
class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        missing = [0] * len(nums)
        for i in range(1, len(nums)):
            missing[i] = missing[i - 1] + (nums[i] - nums[i - 1] - 1)

        for i in range(len(missing)):
            # * 说明到当前位置时, missing number的数量满足所求. 
            if missing[i] >= k:
                # * nums[i-1] 为了满足条件(找到第 k 个缺口数)需要增加的值 = 缺口数的总数量 k 减去 到 index=i-1 为止的缺口数的数量 missing[i - 1]
                return nums[i - 1] + (k - missing[i - 1])

        # * 如果到这里，说明缺口数的数量大于元素中存在的缺口数的数量，需要在元素后面直接添加
        return (k - missing[-1]) + nums[-1]


