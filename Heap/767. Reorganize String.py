""" 
? 详细讲解: https://leetcode.cn/problems/reorganize-string/solution/cjavapython-zui-da-dui-by-yanghk/
? 代码借鉴: https://leetcode.cn/problems/reorganize-string/solution/c-da-ding-dui-ji-hu-shuang-bai-de-jie-fa-1bkq/
? https://leetcode.cn/problems/reorganize-string/solution/lc767-zhong-gou-zi-fu-chuan-dui-tan-xin-by-fight_f/
"""


class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap = MaxHeap()
        record = {}
        for char in s:
            record[char] = record.get(char, 0) + 1

        for key in record:
            max_heap.insert([key, record[key]])

        preChar, preFrequency = None, 0
        res = []

        while max_heap.size:
            curChar, curFrequency = max_heap.remove()
            res.append(curChar)
            if preFrequency > 0:
                max_heap.insert([preChar, preFrequency])

            preChar, preFrequency = curChar, curFrequency - 1

        # * 注意, 我们最后插入的字符就是此时的 preChar, 因为有 "preChar = curChar", 并且此时 heap 是空的, 等于除了 preChar 没有其他字符可以继续间隔插入. 所有, 如果 preFrequency 是大于 0 的, 那么说明最后插入的那个字符(也就是 preChar)还有剩余, 只能继续插入到末尾, 而继续插入就会构成重复. 不满足题目要求, 返回 "". 例子: abaa, 最后一个a就会造成重复出现
        if preFrequency > 0:
            return ""
        else:
            return "".join(res)


class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    @property
    def size(self):
        return len(self.heap)

    def insert(self, val):
        self.heap.append(val)
        self.siftUp(self.size - 1)

    def siftUp(self, curIdx):
        while curIdx > 0:
            parIdx = (curIdx - 1) // 2
            if self.heap[parIdx][1] < self.heap[curIdx][1]:
                self.swap(parIdx, curIdx)
                curIdx = parIdx
            else:
                break

    def remove(self):
        removedItem = self.heap[0]
        self.swap(0, self.size - 1)
        self.heap.pop()
        self.siftDown(0)
        return removedItem

    def siftDown(self, parIdx):
        while 2 * parIdx + 1 < self.size:
            childOneIdx = 2 * parIdx + 1
            childTwoIdx = 2 * parIdx + 2

            idxToSwap = childOneIdx
            if childTwoIdx < self.size and self.heap[childOneIdx][1] < self.heap[childTwoIdx][1]:
                idxToSwap = childTwoIdx

            if self.heap[idxToSwap][1] > self.heap[parIdx][1]:
                self.swap(idxToSwap, parIdx)
                parIdx = idxToSwap
            else:
                break

    def peek(self):
        return self.heap[0]

    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]
