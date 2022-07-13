
#! 使用 maxHeap, 由于每次从堆顶弹出的数都是堆中最大的(根据本题最大堆的定义, 每次弹出的都是距离最远的点)，距离最近的 k 个点一定会留在堆里。如果当前堆不满，直接添加；堆满的时候，如果新读到的数大于「堆顶元素」，肯定不是我们要找的元素，只有新遍历到的点小于「堆顶元素」的时候，才将「堆顶元素」拿出，然后放入新读到的数，进而让堆自己去调整内部结构。
class Solution(object):
    def kClosest(self, points, k):

        #* 求离的最近的，说明要把距离远的排除出去，所以使用 maxHeap
        
        maxHeap = MaxHeap()
        record = {}
        for xIdx, yIdx in points:
            dis = xIdx ** 2 + yIdx ** 2
            record[(xIdx, yIdx)] = dis
        # print("record is ", record) 
         
        for i in range(len(points)):
            xIdx, yIdx = points[i]
            dis = record[(xIdx, yIdx)]
            if i < k:
                maxHeap.insert(((xIdx, yIdx), dis))
            else:
                if maxHeap.peek()[1] > dis:
                    maxHeap.remove()
                    maxHeap.insert(((xIdx, yIdx), dis))
            # print("current heap", maxHeap.heap)
        result = []
        for i in range(maxHeap.size):
            result.append(maxHeap.heap[i][0])
        # print(result)
        return result
        
class MaxHeap:
    def __init__(self) -> None:
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
            
            if self.heap[parentIdx][1] < self.heap[currentIdx][1]:
                self.swap(parentIdx, currentIdx)
                currentIdx = parentIdx
            else:
                break
            
    def remove(self):
        removedItem = self.peek()
        self.swap(0, self.size - 1)
        self.heap.pop()
        self.siftDown(0)
        return removedItem
    
    def siftDown(self, currentIdx):
        endIdx = self.size - 1
        while 2 * currentIdx + 1 <= endIdx:
            childOneIdx = 2 * currentIdx + 1
            childTwoIdx = 2 * currentIdx + 2
            childIdxToSwap = childOneIdx
            
            if childTwoIdx <= endIdx and self.heap[childOneIdx][1] < self.heap[childTwoIdx][1]:
                childIdxToSwap = childTwoIdx
                
            if self.heap[childIdxToSwap][1] > self.heap[currentIdx][1]:
                self.swap(childIdxToSwap, currentIdx)
                currentIdx = childIdxToSwap
            else:
                break
    
    def peek(self):
        return self.heap[0]
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


