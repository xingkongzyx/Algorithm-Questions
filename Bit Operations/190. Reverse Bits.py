""" 
每次把 res 左移, 把 n 的二进制末尾数字, 拼接到结果 res 的末尾。然后把 n 右移, 看 n 的新的最后一位
/ time complexity is O(32), space complexity is O(1).
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # 得到当前 n 的最后一位bit, 0&1=0, 1&1=1, 结果为 0 或者 1
            curEndBit = n & 1
            left_shift_res = res << 1
            # add last bit of n(对应着 curEndBit) to res
            res = left_shift_res | curEndBit
            # remove last bit from n
            n = n >> 1

        return res
