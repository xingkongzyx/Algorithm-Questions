""" 
 * 调用hit() 函数时, 将时间戳入队列
 * 调用getHits()函数时, 将队列中不满足条件的删除, 剩下元素的个数即为结果。
 ? https://leetcode.cn/problems/design-hit-counter/solution/by-bw-zhang-zv2y/
"""


class HitCounter:
    from collections import deque

    def __init__(self):
        self.data = deque([])

    def hit(self, timestamp: int) -> None:
        self.data.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # # queue 不为空的情况下才能使用其首元素的 index, 避免了 queue 是空时 index 越界
        while self.data and self.data[0] <= timestamp - 300:
            self.data.popleft()

        return len(self.data)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
