class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxLen = 0
        left = 0
        right = 0

        cost = 0
        
        while right < len(s):
            currentCharCost = abs(ord(t[right]) - ord(s[right]))
            cost += currentCharCost
            
            if cost <= maxCost:
                maxLen = max(maxLen, right - left + 1)
            """             
            ! 注意这里, 不符合条件时 left 只需右移一格, 我们不需要 left 一直右移, 来重新使得窗口重新符合条件, 因为：
            * 1. 我们只关心子数组的最大长度, 不需要关心子数组到底有哪些. 所以此时 left - right 的区间肯定是字符串到 right 为止时, 符合条件的最大的子区间长度。
            * 极端情况, 每一个字符差值都不符合条件, 那么 left 将会一直等于right, 最后相减的结果也将会是0。
            
            * 最后举个例子, 假设两字符最大区间为下标 5-10（长度5）。当 left 等于5之前, 最大长度计算出为3, 那么窗口右移的过程中,  left=5, right=8, 此时肯定是符合条件的, right 将会一直到 10。此时right 右移到11时不符合条件, left 继续跟踪右移为 6, 直到字符串结尾, right 和 left 之间的长度会一直是 5。
            """
            if cost > maxCost:
                leftCharReturnedCost = abs(ord(t[left]) - ord(s[left]))
                cost -= leftCharReturnedCost
                left += 1
            
            right += 1
            
        return maxLen
        

print(Solution().equalSubstring(s = "krrgw", t = "zjxss", maxCost = 19))

