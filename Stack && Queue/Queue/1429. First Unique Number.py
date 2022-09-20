""" 
? https://leetcode.cn/problems/first-unique-number/solution/aya-python-li-yong-ha-xi-biao-ji-shu-xua-mwov/
"""


class FirstUnique:
    # 版本2:deque优化，效率在时间上提升了约40倍，用时248 ms
    def __init__(self, nums: List[int]):
        # 标准队列一个，辅助队列一个
        self.queue = []
        self.helper = collections.deque()
        self.memo = collections.defaultdict(int)
        for n in nums:
            self.memo[n] += 1
        for key in self.memo:
            if self.memo[key] == 1:
                self.helper.append(key)  # 里面存的都是只出现一次的

    def showFirstUnique(self) -> int:
        while len(self.helper) != 0:
            if self.memo[self.helper[0]] != 1:
                self.helper.popleft()
            else:
                return self.helper[0]
        return -1

    def add(self, value: int) -> None:
        self.queue.append(value)
        self.memo[value] += 1
        if self.memo[value] == 1:
            self.helper.append(value)
