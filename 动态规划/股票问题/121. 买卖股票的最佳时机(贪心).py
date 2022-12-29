""" 
* 保持在「最便宜」的时候买入, 「最贵」的时候卖出, 即可获最大的利润. 那么我们看这道题, 按照题意只能进行一次买卖。使用贪心思想, 为了使利润最大化, 要尽量以一个较低的价格买入, 较高的价格抛出。将问题分解为局部问题, 则是找到当天对应最大利润, 最后得到最大值即可。

? 用贪心来理解: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/solution/by-jyd-cu90/
? 用动态规划理解: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/solution/teng-xun-leetcode121mai-mai-gu-piao-de-zui-jia-shi/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minCost = float("inf")
        maxProfit = 0

        for i in range(len(prices)):
            # 到当前的「第i天」为止的最低买入价格
            minCost = min(minCost, prices[i])
            # # 到当前「第i天」为止的最大收益, 这个收益可能来源于今天的卖出 -「第 i 天卖出的最高利润: price - minCost」, 也有可能是「前 i-1 天最高利润 profit 」。无论哪种都能够保证不会颠倒买入卖出的顺序
            maxProfit = max(maxProfit, prices[i] - minCost)

        return maxProfit
