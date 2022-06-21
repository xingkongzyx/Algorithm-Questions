class Solution:
    def minDays(self, bloomDay, m, k):
        #/ 单调性就是 制作过程中等待的天数越少，能够使用相邻的且盛开的花来制作花束的数量越少，等待天数越多，能够制作的花束数量也就越多
        
        #* 特殊情况，制作 m 花束所需要盛开的鲜花数量不足，直接返回 -1
        if m * k > len(bloomDay):
            return -1
        
        #* 二分法范围是 最小是只等待一天，最大是等待所有花全部开放(也就是max(bloomDay))
        left = 1
        right = max(bloomDay)
        
        while left < right:
            mid = left + (right - left) // 2
            
            madeBouquets = self.calculateBouquets(mid, bloomDay, k)
            
            #> 与前几题的不同之处，这里是「大于等于」的情况进行了合并，这是由于单调性决定的
            if madeBouquets < m:
                left = mid + 1
            else:
                right = mid
        return left
    
    def calculateBouquets(self, waitDays, bloomDayArr, k):
        resBouquets = 0
        #* flowers 变量是用于「记录相邻的开放的花的计数器」
        flowers = 0
        
        for i in range(len(bloomDayArr)):
            if bloomDayArr[i] <= waitDays:
                #* 说明这个花在经过 waitDays 的时间后开放，变成可以使用的花
                flowers += 1
                if flowers == k:
                    #* 如果有数量满足k的相邻的花都处于开放状态，说明可以构成一个新的 bouquet，它的数量加 1，用于「记录相邻的开放的花的计数器 flowers」 归零，进行新一轮的统计
                    resBouquets += 1
                    flowers = 0
            else:
                #* 说明这个花在经过 waitDays 的时间后不会开放，不能被使用. 这个index之前即使有开放的花因为这个点不开放的原因也不能构成 bouquets. 所以用于「记录相邻的开放的花的计数器 flowers」 归零，重新计数
                flowers = 0
        
        return resBouquets

res = Solution().minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3)
print(res)
