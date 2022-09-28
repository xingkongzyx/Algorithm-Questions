""" 
/ 时间复杂度: O(n)
/ 空间复杂度: 令 C 为字符集大小, C 固定为 10。复杂度为 O(C)
? 代码: https://leetcode.cn/problems/bulls-and-cows/solution/cai-shu-zi-you-xi-by-leetcode-solution-q9lz/
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretFreq = [0] * 10
        guessFreq = [0] * 10

        bulls = 0
        cows = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secretFreq[int(secret[i])] += 1
                guessFreq[int(guess[i])] += 1

        for i in range(10):
            if secretFreq[i] > 0 and guessFreq[i] > 0:
                cows += min(secretFreq[i], guessFreq[i])

        return f"{bulls}A{cows}B"
