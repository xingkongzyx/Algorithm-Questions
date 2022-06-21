#* 返回能在 days 天内将传送带上的所有包裹送达的船的最低运载能力。
""" 
* 单调性是:「船的运载能力」越大，则能将所有包裹运送上船所需要的时间越短.「船的运载能力」越小，则能将所有包裹运送上船所需要的时间越长

* 接下来我们要确定二分的范围，由于不存在包裹拆分的情况，考虑如下两种边界情况：
* 1. 理论最低运力：只确保所有包裹能够被运送，自然也包括重量最大的包裹，此时理论最低运力为 max，max 为数组 weights 中的最大值 🚩必须要满足一天至少运一个，运载能力至少要比每个包裹的重量都要大才行，不然就会出现有包裹一直运不走🚩
* 2. 理论最高运力：使得所有包裹在最短时间（一天）内运送完成，此时理论最高运力为 sum，sum 为数组 weights 的总和
* 由此，我们可以确定二分的范围为 [max, sum]。
 """
class Solution:
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            neededDays = self.calculateShipDays(mid, weights)
            print(f"left is {left}, mid is {mid}, right is {right}, time is {neededDays}")
            if neededDays > days:
                #* 如果大于，说明「船的运载能力」太低，所以需要的天数比 "days" 多，需要提高「船的运载能力」。下一轮搜索区间 [mid + 1, right]
                left = mid + 1
                
            else:
                #* 如果小于，说明「船的运载能力」太高，所以需要的天数比 "days" 少，需要减少「船的运载能力」。下一轮搜索区间 [left, mid - 1]
                #* 如果目前尝试的 「船的运载能力」 恰好使得传送带上的包裹在 D 天（注意：恰好是 D 天）从一个港口运送到另一个港口，还应该继续尝试减少运载能力。从而得到题目要求的 🌸船的最低运载能力🌸
                right = mid 
        return left        
            
    
    def calculateShipDays(self, weightCapacity, weights):
        # * 总共需要的天数
        totalDays = 1
        # * 当天所能运送的最大包裹的重量
        currentWeight = 0
        
        for itemWeight in weights:
            #* 如果当天再继续运输当前item，当天运输的总的重量就会超过传入函数的 ｢船的运载能力｣，是不被允许的。所以当前的item只能下一天在运输。totalDays加1，currentWeight 重置
            if currentWeight + itemWeight > weightCapacity:
                # 如果当天已经运输的重量加上新的物品超过了运载能力，则需要多一天运输
                totalDays += 1
                currentWeight = 0
            currentWeight += itemWeight
        return totalDays

print(Solution().shipWithinDays([1,2,3,1,1], 4))
