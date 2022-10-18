""" 
* 不生气时顾客会留下，生气时会赶走顾客。
* 〖秘密技巧〗 可以使老板在窗口大小 X 的时间内不生气。我们使用 〖秘密技巧〗 的原则是: 寻找一个时间长度为 X 的窗口，能留住更多的原本因为老板生气而被赶走顾客。
! 使用 〖秘密技巧〗 能得到的最终的顾客数 = 所有不生气时间内的顾客总数 + 在窗口 X 内使用 〖秘密技巧〗 挽留住的原本因为生气而被赶走顾客数。
? 链接: https://leetcode.cn/problems/grumpy-bookstore-owner/solution/yong-mi-mi-ji-qiao-wan-liu-zhu-zui-duo-d-py41/

"""
class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        # # Step 1: 
        # # 定义需要维护的变量
        # # 本文需要得到最大的顾客满意数，分析中知道 "能得到的最终的顾客数 = 所有不生气时间内的顾客总数 + 在窗口 X 内使用 〖秘密技巧〗 挽留住的原本因为生气而被赶走顾客数。" 所以需要定义 "所有不生气时间内的顾客总数 「regularCustomers」", "在窗口 X 内使用 〖秘密技巧〗 挽留住的顾客数 「curBonusCustomers」", 以及 "在所有窗口 X 内能挽留住的最大顾客数 「maxBonusCustomers」"
        # # 同时我们需要找到所有合法解，所以还需要一个res数组
        regularCustomers = 0
        curBonusCustomers = 0
        maxBonusCustomers = 0
        
        # # Step 2: 定义窗口的首尾端 (left, right)， 然后滑动窗口
        left = 0
        right = 0
        
        while right < len(customers):
            rightGrumpy = grumpy[right]
            rightCustomers = customers[right]
            
            # # Step 3: 根据这个时间点老板是否生气更新需要维护的变量(不生气更新 regularCustomers, 生气则更新 curBonusCustomers)
            if rightGrumpy == 0:
                regularCustomers += rightCustomers
            elif rightGrumpy == 1:
                curBonusCustomers += rightCustomers
            
            # # Step 4 
            # # 根据题意可知窗口长度固定，所以用if
            # # 更新固定时间 「minutes」内挽留住的最多顾客数
            #! 滑动窗口在每次循环结束后[left, right) 代表的的都是 「minutes-1」时间内所能挽留的顾客数，通过下面的 if 确保循环结束后 curBonusCustomers 记载的是下次加上 right 前的数据
            # # 窗口左指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (curBonusCustomers)
            if right - left + 1 == minutes:
                maxBonusCustomers = max(maxBonusCustomers, curBonusCustomers)
                leftGrumpy = grumpy[left]
                leftCustomers = customers[left]
                
                if leftGrumpy == 1:
                    curBonusCustomers -= leftCustomers
                
                left += 1
                
            right += 1
            
        
        return maxBonusCustomers + regularCustomers

res = Solution().maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3)
print(res)
