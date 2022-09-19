import math
from math import sqrt

""" 
* 根据等式 a² + b² = c. 可得知 a 和 b 的范围均为 [0,√c]
? 为什么双指针不会错过正确答案？ https://leetcode.cn/problems/sum-of-square-numbers/solution/shuang-zhi-zhen-de-ben-zhi-er-wei-ju-zhe-ebn3/ 
"""
class Solution(object):
    def judgeSquareSum(self, c):
        left = 0
        right = int(sqrt(c))
        
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
