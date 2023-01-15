""" 
* 枚举「中心位置」时间复杂度为 O(N), 从「中心位置」扩散得到「回文子串」的时间复杂度为 O(N), 因此时间复杂度可以降到 O(N^2)

? https://leetcode.cn/problems/longest-palindromic-substring/solution/5-zui-chang-hui-wen-zi-chuan-by-alexer-660/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 当前最大回文串的长度
        maxLen = 0
        # 当前最大回文串的起始索引
        startIdx = 0

        def findPalindrome(left, right):
            nonlocal maxLen
            nonlocal startIdx
            curLen = 0

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    # * s[left] != s[right] 的时候, 不在满足回文的要求, 退出循环
                    break

            # * 此时 curLen 的长度计算如下, 无论是奇数长度还是偶数长度的回文串, 公式都是有效的
            curLen = right - left - 1
            # * 退出循环的时候, left 要不是小于 0 的, 要不是所在位置已经无法与 s[right] 构成回文串, 所以真正的起始位置是 left + 1
            curStartIdx = left + 1
            # * 与之前记录的最大长度进行对比, 更新当前最大回文串的起始索引和长度
            if curLen > maxLen:
                maxLen = curLen
                startIdx = curStartIdx

        for i in range(len(s)):
            findPalindrome(i, i)
            findPalindrome(i, i + 1)

        # print(maxLen, startIdx)
        return s[startIdx: startIdx+maxLen]


# Solution().longestPalindrome(s="babad")
