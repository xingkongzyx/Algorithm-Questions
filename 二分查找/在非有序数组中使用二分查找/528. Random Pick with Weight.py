""" 
* 「前缀和」正好可以达成「权重」与「数字」之间的对应关系, 「数字」越大的元素, 它的「权重」越大, 如果在这个「前缀和」里面掷骰子, 概率分布式服从这个原则
* 取下标的问题就转换成了取某一个和的问题, 唯一需要注意的是, 产生随机数 randNum 后, 需要使用「二分法」在 pre_sum 数组中找到「第一个大于等于」randNum 的元素的下标。
/ 时间复杂度: Solution 类的构造方法整体复杂度为 O(n); pickIndex 的复杂度为 O(logn)
/ 空间复杂度: O(n)
? 代码借鉴: https://leetcode.cn/problems/random-pick-with-weight/solution/java-qian-zhui-he-er-fen-cha-zhao-zhu-xi-v6u2/
? 前缀和部分讲解: https://leetcode.cn/problems/random-pick-with-weight/solution/chi-xiao-dou-nojie-ti-python-dai-ni-du-d-7iev/


* 为什么取随机数时要从 1 开始而不是 0:
* 因为 w 中每一个元素都是 "w[i] >= 1", 一个长度为 n 的构造好的「前缀和」数组可以看是一个基本单位为 1 的 [1, sum[n - 1]] 数轴。如果想要根据前缀和数组保持正确的权重, 就要从 1 开始, 否则从 0 开始的话, 第一个元素的权重就会变大。

/ The random.randint(start, stop) method returns an integer number selected element from the specified range. 并且 start, stop 都是被包含在其中的
"""

import random


class Solution:

    def __init__(self, w):
        self.pre_sum = [0 for _ in range(len(w))]
        self.pre_sum[0] = w[0]

        for i in range(1, len(w)):
            self.pre_sum[i] = self.pre_sum[i - 1] + w[i]

    def pickIndex(self) -> int:
        # * 使用随机函数参数产生 [1, pre_sum[-1]] 范围内的随机数, 然后通过「二分法」在 pre_sum 数组中找到「第一个大于等于」randNum 的元素的下标。
        randNum = random.randint(1, self.pre_sum[-1])
        left = 0
        right = len(self.pre_sum) - 1

        while left < right:
            mid = left + (right - left) // 2
            # * 因为要找到「第一个大于等于」randNum 的元素的下标, 是用排除法, 小于一定不是想要的情况. 下一轮搜索区间是 [mid + 1, right]
            if self.pre_sum[mid] < randNum:
                left = mid + 1
            else:
                right = mid

        return left
