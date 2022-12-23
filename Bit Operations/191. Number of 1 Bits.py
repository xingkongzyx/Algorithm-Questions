class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            # 任何数字与 1 进行 & 操作时得到的结果只会是 0 或者 1, 因为 1 的二进制表示是(000…0001), 只有最后一位进行 & 操作才有变为 1 的可能, 其余位置即使另一个数字有的位数不为 0 也没有用
            if n & 1 == 1:
                count += 1
            # 相当于 n // 2
            n = n >> 1

        return count
