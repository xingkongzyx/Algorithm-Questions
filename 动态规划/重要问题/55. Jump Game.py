"""
 * dp[i] 表示在下标 i 处还能够继续跳跃的最大步数(注意, 定义的是步数而不是位置)
 * if dp[i-1] == 0, 根本就无法到达 i 位置, 自然就无法跳到终点, 直接返回 False
 * if dp[i-1] > 0, 有两中步数的选择, 一是到达 i 位置以后, 选择 nums[i] 的值作为能跳跃的步数。二是, 选择上次剩下的步数作为选择。两者取最大值: dp[i] = max(dp[i-1] - 1, nums[i])
 
? https://leetcode.cn/problems/jump-game/solution/55-tiao-yue-you-xi-dong-tai-gui-hua-jie-9vsu7/

"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0 for _ in nums]

        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i-1] == 0:
                return False
            else:
                dp[i] = max(dp[i-1] - 1, nums[i])

        return True
