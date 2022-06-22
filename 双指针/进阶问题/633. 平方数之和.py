import math
from math import sqrt

""" 
? 为什么双指针不会错过正确答案？ https://leetcode.cn/problems/sum-of-square-numbers/solution/shuang-zhi-zhen-de-ben-zhi-er-wei-ju-zhe-ebn3/ 
"""
class Solution(object):
    def judgeSquareSum(self, c):
        if c == 0:
            return True
        left = 0
        right = math.ceil(sqrt(c))
        
        while left <= right:
            currentSquareSum = left ** 2 + right ** 2
            if currentSquareSum == c:
                return True
            elif currentSquareSum > c:
                right -= 1
            else:
                left += 1
                
        return False

print(Solution().judgeSquareSum(1000000000))
