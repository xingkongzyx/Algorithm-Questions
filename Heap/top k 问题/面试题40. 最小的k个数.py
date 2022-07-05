
#! 使用 maxHeap, 由于每次从堆顶弹出的数都是堆中最大的，最小的 k 个元素一定会留在堆里。这样，把数组中的元素全部入堆之后，堆中剩下的 k 个元素就是最小的 k 个数了。
#? 动画: https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/solution/tu-jie-top-k-wen-ti-de-liang-chong-jie-fa-you-lie-/
class Solution(object):
    def getLeastNumbers(self, arr, k):
        if k == 0:
            return []
        maxHeap = MaxHeap()
        for i in range(len(arr)):
            if i < k:
                maxHeap.insert(arr[i])

            else:
                if arr[i] < maxHeap.peek():
                    #* 因为 heap 中始终保存的是 arr数组中 k 个最小的元素，所以当遍历 arr 中出现比堆顶元素小的元素的时候，就要弹出堆顶元素，在堆中插入这个更小的元素，从而确保 heap 中始终保存的是 arr 数组中 k 个最小的元素
                    maxHeap.remove()
                    maxHeap.insert(arr[i])
        return maxHeap.heap


class MaxHeap:
    def __init__(self):
        self.heap = []

    @property
    def size(self):
        return len(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.size - 1)

    def siftUp(self, currentIdx):
        while currentIdx > 0:
            parentIdx = (currentIdx - 1) // 2
            if self.heap[currentIdx] > self.heap[parentIdx]:
                self.swap(currentIdx, parentIdx)
                currentIdx = parentIdx
            else:
                break

    def remove(self):
        item = self.heap[0]
        self.swap(0, self.size - 1)
        self.heap.pop()
        self.siftDown(0)
        return item

    def siftDown(self, currentIdx):
        endIdx = self.size - 1
        while 2 * currentIdx + 1 <= endIdx:
            childOneIdx = 2 * currentIdx + 1
            childTwoIdx = 2 * currentIdx + 2
            childIdxToSwap = childOneIdx

            if (
                childTwoIdx <= endIdx
                and self.heap[childOneIdx] < self.heap[childTwoIdx]
            ):
                childIdxToSwap = childTwoIdx

            if self.heap[currentIdx] < self.heap[childIdxToSwap]:
                self.swap(currentIdx, childIdxToSwap)
                currentIdx = childIdxToSwap
            else:
                break

    def peek(self):
        return self.heap[0]

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


Solution().getLeastNumbers([0, 1, 1, 2, 4, 4, 1, 3, 3, 2], 6)
