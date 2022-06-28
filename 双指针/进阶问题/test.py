class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c == 0 or c == 1:
            return True
        import math
        left = 0 
        right = math.floor(c ** 0.5)

        while left <= right:
            squareSum = left ** 2 + right ** 2
            if squareSum == c:
                return True
            elif squareSum < c:
                left += 1
            else:
                right -= 1
        return False


print(Solution().judgeSquareSum(3))
