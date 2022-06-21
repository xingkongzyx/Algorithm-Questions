
#? https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/solution/san-chong-fang-fa-tuo-zhan-si-lu-dong-tu-fb9m/
class Solution(object):
    def maxScore(self, cardPoints, k):
        preSum = [0 for _ in range(len(cardPoints) + 1)]
        
        for i in range(1, len(preSum)):
            preSum[i] = preSum[i-1] + cardPoints[i-1]
            
        #! 从前面取走 i 张卡(i是包括0的，代表一张都不从前面取), 然后计算中间卡牌的最小点数和
        minMidSum = float("inf")
        middleCards = len(cardPoints) - k
        #* 从 -1 开始的原因就是如果从前面一张票不取，那么中间窗口的起始 index 就是 -1 + 1 = 0
        for i in range(-1, k):
            midIdxStart = i + 1
            midIdxEnd = (i + 1) + middleCards - 1
            #* 相当于要求 nums[midIdxStart ... midIdxEnd] 左闭右闭区间内所有元素的和。因为preSum数组比nums多一位的，所以计算方式如下
            midSum = preSum[midIdxEnd + 1] - preSum[midIdxStart]
            #! 获取中间卡牌的和的最小值
            minMidSum = min(midSum, minMidSum)
            # print(f"当前面抽取卡 {i}, midIdx范围是 {midIdxStart}, {midIdxEnd}, midSum 是 {midSum}")

        return preSum[-1] - minMidSum


res = Solution().maxScore([1,2,3,4,5,6,1], 3)
print(res)
