""" 
dp[i] 为 i 的二进制形式的 1 的个数, 从「i >= 1」开始的 dp[i] = 1 + dp[i-power], power是指当前正在查看的数对应着的「2 的倍数」, 当前数字正好是「2 的倍数」的话就某一位为 1, 剩下的位为 0, 对应着 dp[0], 例如 0000->001(0)->01(00)->1(000)
? https://leetcode.com/problems/counting-bits/solutions/1808435/python-javascript-very-deep-explanation/?orderBy=most_votes
? https://leetcode.com/problems/counting-bits/solutions/657068/the-art-of-dynamic-programming/?orderBy=most_votes&page=2
? 视频: https://youtu.be/RyBM56RIWrM
"""


class Solution:
    def countBits(self, n: int):

        dp = [0 for _ in range(n + 1)]
        power = 1

        for i in range(1, n + 1):
            if power * 2 == i:
                power = power * 2

            dp[i] = 1 + dp[i - power]

        return dp
