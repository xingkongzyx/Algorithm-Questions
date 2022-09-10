""" 
* dp[j] 定义: 跳跃到达 j 位置后的 maximum score
* 递推公式: 从距离 j 位置的 k 距离内都可以跳跃到 j 位置, 所以只需要取可以跳跃到 j 位置的这些起跳位置的最大得分即可，最后将这个最大值加上 j 位置本身的 score
* dp[j] = max(dp[j-1], dp[j-2], ... , dp[j-k]) + nums[j]
* 初始化: dp[0] = nums[0]
"""


class Solution:
    def maxResult(self, nums, k):
        dp = [float("-inf") for _ in range(len(nums))]

        dp[0] = nums[0]

        for pos in range(1, len(nums)):
            # * 循环遍历能够到达 pos 的所有起跳位置, 也就是从 pos - k 到达 pos - 1 这之间的所有位置, 注意 pos - k 要确保结果最少是 0，否则报错
            for start in range(max(0, pos - k), pos):
                dp[pos] = max(dp[pos], dp[start])

            # * 前面只是计算到达这个位置(不包含这个位置本身)的最大得分，现在加上这个位置本身的得分。
            dp[pos] += nums[pos]

        return dp[-1]
