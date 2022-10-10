""" 
# 根据题意可以知道：珂珂吃香蕉的速度越小，耗时越多。反之，速度越大，耗时越少，这是题目的 单调性；
* 注意: 当「二分查找」算法猜测的速度恰好使得珂珂在规定的时间内吃完香蕉的时候，还应该去尝试更小的速度是不是还可以保证在规定的时间内吃完香蕉。这是因为题目问的是「最小速度 minimum integer k」。

? 详细说明: https://leetcode.cn/problems/koko-eating-bananas/solution/er-fen-cha-zhao-ding-wei-su-du-by-liweiwei1419/1598921
"""


class Solution(object):
    def minEatingSpeed(self, piles, h):
        minSpeed = 1
        # * 因为题目限制了珂珂一个小时之内只能选择一堆香蕉吃，因此速度最大值就是这几堆香蕉中，数量最多的那一堆。
        maxSpeed = max(piles)

        left = minSpeed
        right = maxSpeed

        while left < right:
            mid = left + (right - left) // 2
            eatingTime = self.calculateTime(mid, piles)

            # * 如果吃完所有香蕉花费的时间少于 h, 说明每小时吃的过度(eating speed of k 过大), 通过调整右边界缓慢 eating speed. 如果是等于的情况, 因为题目想获得的是 "h hours 中吃完所有 bananas 的最小 eating speed", 所以继续向左探索
            if eatingTime <= h:
                right = mid
            else:
                left = mid + 1

        return left

    def calculateTime(self, speed, piles):
        totalHours = 0
        import math
        for pile in piles:
            neededHours = math.ceil(pile / speed)
            totalHours += neededHours
        return totalHours


res = Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8)
print(res)
