""" 
* 关于 counter 的解释: 
* 1 - It is like a global index of the stack and it is used to differentiate two nodes with the same frequency
* 2 - The heapq library needs some value to differentiate between two nodes with the same priority(here node is list inside heap)
* 3 - Heapq suggest implementing a 3-element list where the first value is the priority, second is the entry counter and third is the actual number (docs - https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes)
# 4 - We are not decrementing this counter because the previous value is already used by some node inside the heap and reusing the counter value would give a wrong answer as heapq will not have a unique differentiator between a few elements.
* 5 - Also, we don't need to keep the counter in proper sequence(1,2,3), it just has to be an increasing integer sequence(1,3,4) so that heapq is able to unique tell which number of inserted recently

? 思路: https://leetcode.com/problems/maximum-frequency-stack/discuss/163435/Python-Simple-PriorityQueue

/ Time complexity: push and pull in O(log n) 
"""


class FreqStack:
    def __init__(self):
        # * self.counter 用于记录在FreqStack的位置
        self.counter = 0
        # * 用于记录栈中每个元素的出现次数
        self.freqMap = {}
        # * 用于每次能把堆中出现次数最多的元素弹出
        self.maxHeap = MaxHeap()

    def push(self, val: int) -> None:
        self.freqMap[val] = self.freqMap.get(val, 0) + 1
        # # 注意我们插入堆中的 tuple 的含义是: (val在堆中的出现次数, val在stack中的位置, val)
        self.maxHeap.insert((self.freqMap[val], self.counter, val))
        self.counter += 1

    def pop(self) -> int:
        # * 每次弹出 heap 的频率最大的元素, 如果在 heap 中有两个元素频率相同, 那么 counter 更大的元素被弹出, counter 越大就代表 "closest to the stack's top." 而在弹出的过程中并没有对 counter 进行更新, 原因见注释
        eleFreq, eleIdx, eleVal = self.maxHeap.remove()
        self.freqMap[eleVal] -= 1
        return eleVal


""" 
/ bubble up(insert): Time: O(logn)
/ sift down(removal): Time: O(logn)
/ build heap: Time O(n) time
"""


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
            # * 调用自定义的compare函数，使得 siftUp 过程正确
            if self.compare(currentIdx, parentIdx):
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

            if (
                childTwoIdx <= endIdx
                and self.compare(childTwoIdx, childOneIdx)
            ):
                childIdxToSwap = childTwoIdx

            if self.compare(childIdxToSwap, currentIdx):
                self.swap(childIdxToSwap, currentIdx)
                currentIdx = childIdxToSwap
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def compare(self, idx1, idx2):
        #! 制定 MaxHeap 的规则:
        # * frequency 大的在前面, 如果两个 node 的 frequency 相同, 那么在栈中位置更靠后的在前面, 因为更靠后的要先被弹出来, 所以放在堆顶。
        if (self.heap[idx1][0] > self.heap[idx2][0]) or (
            self.heap[idx1][0] == self.heap[idx2][0]
            and self.heap[idx1][1] > self.heap[idx2][1]
        ):
            return True

        return False
