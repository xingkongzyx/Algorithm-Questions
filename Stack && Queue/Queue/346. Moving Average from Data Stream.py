""" 
* 我们注意到并不需要存储数据流中的所有值, 只需要数据流中的最后 n 个值。
* 
* 根据移动窗口的定义, 在每个步骤中, 我们向窗口添加一个新元素, 同时从窗口中删除第一个元素。这里, 我们可以应用一种称为双端队列的数据结构(deque)来实现移动窗口, 它在两端删除或添加元素将具有常数的时间复杂度O(1)；使用双端队列, 我们可以将空间复杂度降低到 O(N), 其中 N 是移动窗口的大小。

? https://leetcode.cn/problems/moving-average-from-data-stream/solution/shu-ju-liu-zhong-de-yi-dong-ping-jun-zhi-by-leetco/
"""


class MovingAverage:
    from collections import deque

    def __init__(self, size: int):
        self.data = deque([])
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.data) < self.size:
            self.data.append(val)
            self.sum += val
        else:
            popped = self.data.popleft()
            self.sum -= popped
            self.sum += val
            self.data.append(val)

        return self.sum / len(self.data)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
