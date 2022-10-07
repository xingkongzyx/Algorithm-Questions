# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n

        while left < right:
            mid = left + (right - left) // 2
            # * if mid version is not bad, means bad version must in [mid + 1, right], next search interval should be [mid + 1, right]
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid

        return left
