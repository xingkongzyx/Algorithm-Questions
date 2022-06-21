class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num // 2

        while left < right:
            mid = left + (right - left + 1) // 2
            # print(f"left is {left}, right is {right}, mid is {mid}")

            if mid > num // mid:
                right = mid - 1
            else:
                left = mid
        
        return left * left == num
Solution().isPerfectSquare(9)
