# dp的定义与 647 完全一样的

def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[False for _ in range(len(s))] for _ in range(len(s))] 
        for i in range(len(s)):
            dp[i][i] = True
        resLen = 0
        startIdx = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] != s[j]:
                    dp[i][j] = False
                elif s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    if dp[i][j] == True:
                        currentPalindromeLen = j - i + 1
                        if currentPalindromeLen > resLen:
                            resLen = currentPalindromeLen
                            startIdx = i

        return s[startIdx: startIdx + resLen]