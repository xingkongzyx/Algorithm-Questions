""" 
* 1、用一个 dp 数组存到当前位置的最大得分；
* 2、由于在单纯的动态规划解法中我们在每次计算 dp[i] 时，需要遍历 i 的前 k 个元素得到其中最大的 dp[i - k]. 可以用一个最大堆来存当前位置 i 到它的前 k 个位置里的得分, dp[i] = nums[i] + heap[0][0]
* 
* 注：最大堆的元素是一个元组 (val, index), val 表示得分, index 表示索引, 维护最大堆的大小为 k
! 但要注意，数据范围是流动的，当超范围时，要将移除堆中的数据, 这就是 while 中的heapq.heappop
? https://leetcode.cn/problems/jump-game-vi/solution/100-by-leaf_ye-ggah/
? https://leetcode.cn/problems/jump-game-vi/solution/1696-tiao-yue-you-xi-vi-java-by-wa-pian-b6byz/
? 必看https://leetcode.cn/problems/jump-game-vi/solution/tiao-yue-you-xi-vi-by-zerotrac2-r1kq/
"""


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        heap = []
        heapq.heappush(heap, (-nums[0], 0))
        for i in range(1, n):
            if heap:
                while i - heap[0][1] > k:
                    heapq.heappop(heap)
                val = -heap[0][0]
                dp[i] = nums[i] + val
                heapq.heappush(heap, (-dp[i], i))
        return dp[-1]
