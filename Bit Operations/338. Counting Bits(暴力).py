""" 
结合了 191 题的 "count bit 1" 的方法, 对于从0开始到n的每个数, 都计算当前数包含几个1, 把结果append到res中。
/ 时间复杂度: 每个数计算有几个 1 的时间复杂度是 O(logn), 因为是通过 ">>2" 循环, 相当于每次 "num //= 2", 最终到 0 的次数是 logn 次, 一共有0个数需要计算, 所以总的时间复杂度是 O(n * logn)
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(0, n + 1):
            curNum = self.countOnes(i)
            res.append(curNum)

        return res

    def countOnes(self, num):
        count = 0

        while num > 0:
            if num & 1 == 1:
                count += 1
            num = num >> 1

        return count
