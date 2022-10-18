
""" 
# > 这道题 与 1658 非常类似
> 使之变成固定滑动窗口问题的关键的转换
* 从两边选择卡片，选择 k 张，卡片的总数量为 n 张，即有 n - k 张不被选择。
! 所有卡边的总和 sum 固定，要使选择的 k 张的总和最大，反过来就是要让不被选择的 n - k 张的总和最小。
* 
* 可以使用滑动窗口来计算 n - k 张卡片的最小总和 min，最终答案为 sum - min。

# 每次遍历结束后 [left, right) 代表窗口长度比 所求固定窗口长度 小1的窗口
"""
class Solution(object):
    def maxScore(self, cardPoints, k):
        ## Step 1: 定义需要维护的变量们(题目转化成求 n-k 张卡片的最小总和，所以需要变量 minScore)
        totalScore = sum(cardPoints)
        numOfCards = len(cardPoints)
        
        if numOfCards == k:
            return totalScore
        
        curScore = 0
        minScore = float('inf')
        
        ## Step 2: 定义窗口的首尾端 (left, right)， 然后滑动窗口
        left = 0
        right = 0
        
        while right < numOfCards:
            ## Step 3: 更新需要维护的变量, 这里只需要更新 curScore
            rightCard = cardPoints[right]
            curScore += rightCard
            
            ## 属于 Step 4 - 情况1
            ## 如果题目的窗口长度固定：用一个if语句判断一下当前窗口长度是否达到了限定长度. 如果达到了，窗口左指针前移一个单位，从而保证下一次右指针右移时，窗口长度保持不变, 
            ## 左指针移动之前, 先更新Step 1定义的维护变量 
            if right - left + 1 == numOfCards - k:
                minScore = min(curScore, minScore)
                leftCard = cardPoints[left]
                curScore -= leftCard
                ## 窗口左指针前移一个单位保证下一次右指针右移时窗口长度保持不变
                left += 1
                
            right += 1
        # print("minScore is ", minScore)   
        return totalScore - minScore

so = Solution().maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3)
print(so)
