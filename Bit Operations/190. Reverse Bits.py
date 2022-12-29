""" 
每次把 res 左移, 把 n 的二进制末尾数字, 拼接到结果 res 的末尾。然后把 n 右移, 看 n 的新的最后一位
? 解释的动图 https://leetcode.cn/problems/reverse-bits/solution/4chong-jie-jue-fang-shi-tu-wen-xiang-jie-fsgg/
/ time complexity is O(32), space complexity is O(1).
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # * 得到当前 n 的最后一位bit, 0&1=0, 1&1=1, 结果为 0 或者 1
            curEndBit = n & 1
            # * 将 res 左移一位, 把最后一个空出来, 放置 n 的最后一位 bit
            res = res << 1
            # * add last bit of n(对应着 curEndBit) to res
            res = res | curEndBit
            # * remove last bit from n
            n = n >> 1

        return res
