
""" 
* 题目要求获取一个数据流排序后的中位数, 那么可以使用两个优先队列（堆）实现。
* 该题使用一个 maxHeap, 一个 minHeap 完成。
* ➀ 小顶堆(minHeap)用于存储所有元素中「较大的一半」, 堆顶存储的是其中「最小的数」。
* ➁ 大顶堆(maxHeap)用于存储所有元素中「较小的一半」, 堆顶存储的是其中「最大的数」。
* ➂ 相当于, 把所有元素分成了「大」和「小」两半, 我们计算中位数, 只需要「大的那半的最小值」和「小的那半的最大值」即可。即是 "大顶堆的堆顶" 与 "小顶堆的堆顶" 就是排序数据流的两个中位数。
* ➃ 在 addNum 过程中, 需要保证这 2 个堆的『平衡』。这里的平衡指得是：
*    ➊ 储存所有元素中「较小的一半」的 maxHeap 的大小 = 储存所有元素中「较大的一半」minHeap 的大小, 
*    ➋ 或者 maxHeap 的大小 = minHeap 的大小 + 1。
*    ➌ 如果不满足以上两个条件则要进行『重新平衡』
* ➄ 当调用 findMedian 查询中位数的时候, 中位数就是最大堆的堆顶元素, 或者 (最大堆的堆顶元素 + 最小堆的堆顶元素)/2


? 过程图解: https://leetcode.cn/problems/find-median-from-data-stream/solution/tong-ge-lai-shua-ti-la-tu-jie-da-ding-du-ghiy/
? 代码借鉴: https://leetcode.com/problems/find-median-from-data-stream/discuss/74158/Python-O(lgn)-using-two-heapq-data-sturctures

/ 时间复杂度: addNum 函数的复杂度为 O(logn); findMedian 函数的复杂度为 O(1)
/ 空间复杂度: O(n)
"""


class MedianFinder(object):

    def __init__(self):
        self.lowerHalf = MaxHeap()
        self.greaterHalf = MinHeap()

    def addNum(self, num):
        # * 我们要保证每次插入元素后, 两堆维持相对长度。让 minHeap 为长度较大的堆, 每次插入元素时进行判断。
        if self.lowerHalf.size == 0 or num < self.lowerHalf.peek():
            self.lowerHalf.insert(num)
        else:
            self.greaterHalf.insert(num)

        # * 如果按照上述规则插入后发现两个堆的长度「差为 2」, 则需要从「元素多」的那个堆中「移除」一个元素, 并将「移除的元素」给予另一个「元素少」的那个堆
        if self.lowerHalf.size - self.greaterHalf.size == 2:
            self.greaterHalf.insert(self.lowerHalf.remove())
        elif self.greaterHalf.size - self.lowerHalf.size == 2:
            self.lowerHalf.insert(self.greaterHalf.remove())

    def findMedian(self):
        # * 如果当前两个 heaps 大小一样, 则中位数是两堆的「堆顶元素平均值」。
        # * 如果当前两个 heaps 大小不一样, 因为我们上面的『重新平衡』操作, 则一定有一个「元素多」的堆, 中位数为「数字较多堆」的堆顶元素。
        if self.lowerHalf.size == self.greaterHalf.size:
            return float(self.lowerHalf.peek() + self.greaterHalf.peek()) / 2
        elif self.lowerHalf.size > self.greaterHalf.size:
            return self.lowerHalf.peek()
        elif self.lowerHalf.size < self.greaterHalf.size:
            return self.greaterHalf.peek()


class MaxHeap:
    def __init__(self):
        self.heap = []

    @property
    def size(self):
        return len(self.heap)

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)

    def remove(self):
        item = self.heap[0]
        self.swap(0, len(self.heap) - 1)
        self.heap.pop()
        self.siftDown(0)
        return item

    def siftUp(self, currentIdx):
        while currentIdx > 0:
            parentIdx = (currentIdx - 1) // 2
            if self.heap[currentIdx] > self.heap[parentIdx]:
                self.swap(currentIdx, parentIdx)
                currentIdx = parentIdx
            else:
                break

    def siftDown(self, currentIdx):
        endIdx = len(self.heap) - 1
        while currentIdx * 2 + 1 <= endIdx:
            childOneIdx = currentIdx * 2 + 1
            childTwoIdx = currentIdx * 2 + 2
            childIdxToSwap = childOneIdx
            if childTwoIdx <= endIdx and self.heap[childTwoIdx] > self.heap[childOneIdx]:
                childIdxToSwap = childTwoIdx

            if self.heap[currentIdx] < self.heap[childIdxToSwap]:
                self.swap(childIdxToSwap, currentIdx)
                currentIdx = childIdxToSwap
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


class MinHeap:
    def __init__(self):
        self.heap = []

    @property
    def size(self):
        return len(self.heap)

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)

    def siftUp(self, currentIdx):
        while currentIdx > 0:
            parentIdx = (currentIdx - 1) // 2
            if self.heap[currentIdx] < self.heap[parentIdx]:
                self.swap(currentIdx, parentIdx)
                currentIdx = parentIdx
            else:
                break

    def remove(self):
        item = self.heap[0]
        self.swap(0, len(self.heap) - 1)
        self.heap.pop()
        self.siftDown(0)
        return item

    def siftDown(self, currentIdx):
        endIdx = len(self.heap) - 1
        while currentIdx * 2 + 1 <= endIdx:
            childOneIdx = currentIdx * 2 + 1
            childTwoIdx = currentIdx * 2 + 2
            childIdxToSwap = childOneIdx
            if childTwoIdx <= endIdx and self.heap[childTwoIdx] < self.heap[childOneIdx]:
                childIdxToSwap = childTwoIdx

            if self.heap[childIdxToSwap] < self.heap[currentIdx]:
                self.swap(childIdxToSwap, currentIdx)
                currentIdx = childIdxToSwap
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
