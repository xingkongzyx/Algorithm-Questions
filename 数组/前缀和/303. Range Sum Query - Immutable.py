""" 
所以我们可以先创建一个数组, 用来存放从原数组每项累加的和, 我们称其为前缀和数组。这样, 我们可以利用减法, 直接得出结果, 公式: sumRange(i,j) = presum[j+1] - presum[i]。

/ 时间复杂度: 构造函数的时间复杂度是 O(N), sumRange 函数调用的时间复杂度是 O(1)
/ 空间复杂度: O(N)。

? https://leetcode.cn/problems/range-sum-query-immutable/solutions/627185/jian-dan-wen-ti-xi-zhi-fen-xi-qian-tan-q-t2nz/?orderBy=most_votes
"""


class NumArray:

    def __init__(self, nums):
        length = len(nums)
        self.presum = [0 for _ in range(length + 1)]
        for i in range(length):
            self.presum[i + 1] = self.presum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:

        return self.presum[right + 1] - self.presum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
