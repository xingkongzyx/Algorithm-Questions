
#? 题目来源: https://www.interviewbit.com/problems/merge-k-sorted-arrays/
""" 
/ Let n be the total elements across the k sorted arrays we are given.

/ Time: O(2(n * log(k))) = O(n * log(k) )

/ Extracting and adding to the min heap will both take log(k) time. For each of the n items, we will do an addition to the heap and removal from the heap (log(k) expense per heap operation). Hence the times 2. It is dropped. We get O( n * log(k) ).

/ Space: O(k)

/ Our heap will need to hold k elements for most of this process and cannot worsen past this.
# We are not counting the size of the output array which uses O(n) space since that isn't core to our algorithm.

"""
class Solution:
    # @param arrs : list of list of integers
    # @return a list of integers
    def solve(self, arrs):
        minHeap = MinHeap()
        k = len(arrs)
        
        #! minHeap 中记录的是一个tuple，其中包含(arrIdx, elementIdx, elementVal)
        #* 他的初始值是 arrs 中的每个 array 中的 first element(index 0)
        for i in range(k):
            minHeap.insert((i, 0, arrs[i][0]))
        result = []
        
        #! grab the smallest element in the heap, add it to the result array, and insert the next element in the heap if there is one.
        #* 只要 minHeap 不是空的, 就要从 minHeap 中移除「堆顶元素」(也是当前heap中最小的元素), 将移除的元素加入 result 数组, 再更新「堆顶元素」对应的 elementIdx, 如果更新后 elementIdx 没有越界, 则将这个新的元素加入堆, 以维持堆的大小为 k. 如果更新后的 elementIdx 越界了, 则继续 while 循环, 处理新的「堆顶元素」
        while minHeap.size > 0:
            smallestItem = minHeap.remove()
            arrIdx, elementIdx, elementVal = smallestItem
            result.append(elementVal)
            elementIdx += 1
            if elementIdx < len(arrs[arrIdx]):
                minHeap.insert((arrIdx, elementIdx, arrs[arrIdx][elementIdx]))
            else:
                continue
        return result

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

    
    def siftUp(self, currentIdx):
        while currentIdx > 0:
            parentIdx = (currentIdx - 1) // 2
            if self.heap[currentIdx][2] < self.heap[parentIdx][2]:
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
            if childTwoIdx <= endIdx and self.heap[childTwoIdx][2] < self.heap[childOneIdx][2]:
                childIdxToSwap = childTwoIdx
            
            if self.heap[childIdxToSwap][2] < self.heap[currentIdx][2]:
                self.swap(childIdxToSwap, currentIdx)
                currentIdx = childIdxToSwap
            else:
                break
                  
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    
Solution().solve(arr = [[1, 2, 3], [2, 4, 6], [0, 9, 10]])


