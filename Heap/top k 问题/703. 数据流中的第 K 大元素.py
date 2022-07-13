""" 
* 我们可以使用一个大小为 k 的优先队列来存储前 k 大的元素, 其中优先队列的队头为队列中最小的元素, 也就是第 k 大的元素。
# 在单次插入的操作中, 我们「首先」将元素 val 加入到优先队列中。如果此时优先队列的大小大于 k, 我们需要将优先队列的队头元素弹出, 以保证优先队列的大小为 k。

? https://leetcode.cn/problems/kth-largest-element-in-a-stream/solution/shu-ju-liu-zhong-de-di-k-da-yuan-su-by-l-woz8/

/ 时间复杂度: O(nlog(k)) 每个元素都有插入到堆中的操作, 「插入到堆中」的时间复杂度是 O(logk), 这个操作又针对于「所有元素」, 所以复杂度是 O(n * log(k))
/ 空间复杂度: O(k), 使用了一个大小为 k + 1 的 min heap
"""
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = MinHeap()
        for num in nums:
            self.heap.insert(num)
            if self.heap.size > k:
                self.heap.remove()


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.heap.insert(val)
        if self.heap.size > self.k:
            self.heap.remove()
        return self.heap.peek()


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
        
    
    def remove(self):
        item = self.heap[0]
        self.swap(0, len(self.heap) - 1)
        self.heap.pop()
        self.siftDown(0)
        return item

    
    def siftUp(self, idx):
        while idx > 0:
            parentIdx = (idx - 1) // 2
            if self.heap[idx] < self.heap[parentIdx]:
                self.swap(idx, parentIdx)
                idx = parentIdx
            else:
                break
    
    def siftDown(self, currentIdx):
        endIdx = len(self.heap) - 1
        while currentIdx * 2 + 1 <= endIdx:
            childOneIdx = currentIdx * 2 + 1
            childTwoIdx = currentIdx * 2 + 2
            
            idxToSwap = childOneIdx
            
            if childTwoIdx <= endIdx and self.heap[childTwoIdx] < self.heap[childOneIdx]:
                idxToSwap = childTwoIdx
            
            if self.heap[idxToSwap] < self.heap[currentIdx]:
                self.swap(idxToSwap, currentIdx)
                currentIdx = idxToSwap
            else:
                break
                   
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
