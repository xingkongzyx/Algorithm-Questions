class Solution(object):
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """ 
        dp[i] 考虑到index 为 i的序列为止，其总预约时间最长是
        dp[i] = dp[i-1], dp[i-2] + nums[i]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        dp = [0 for _ in nums]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

        