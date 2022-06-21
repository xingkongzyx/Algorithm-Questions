class Solution(object):
    def guessNumber(self, n):
        left = 0
        right = n
        while left < right:
            mid = left + (right - left) // 2
            res = guess(mid)
            if res == 1:
                #* 中位数比猜的数小，因此比中位数小的数包括中位数都不是目标元素，所以下一轮搜索区间是 [mid + 1, right]
                #* [mid + 1, right]
                left = mid + 1
            else:
                #* 下一轮搜索区间 [left, mid]
                right = mid
        return left
