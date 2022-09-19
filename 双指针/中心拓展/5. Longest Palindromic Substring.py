""" 
? 枚举「中心位置」时间复杂度为 O(N)，从「中心位置」扩散得到「回文子串」的时间复杂度为 O(N)，因此时间复杂度可以降到 O(N^2)


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

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if left == right:
                    # * left == right 的时候，说明从当前扩张的字符就是 1 个，相应的长度只会加 1
                    curLen += 1
                else:
                    # * left != right 的时候，说明是从两个字符开始向同时两侧扩张，每次扩张长度加 1
                    curLen += 2
                left -= 1
                right += 1

            # * 与之前记录的最大长度进行对比, 更新当前最大回文串的起始索引和长度
            if curLen > maxLen:
                maxLen = curLen
                startIdx = left + 1

        for i in range(len(s)):
            findPalindrome(i, i)
            findPalindrome(i, i + 1)

        print(maxLen, startIdx)
        return s[startIdx: startIdx+maxLen]


# Solution().longestPalindrome(s="babad")
