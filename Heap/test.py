

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        heap = MinHeap()
        for i in range(len(A)):
            heap.insert((i, 0, A[i][0]))
        # print(heap.heap)
        result = []
        while heap.size > 0:
            arrIdx, eleIdx, eleVal = heap.remove()
            result.append(eleVal)
            if eleIdx == len(A[arrIdx]) - 1:
                print("it is ", arrIdx, eleIdx, eleVal)
                continue
            else:
                heap.insert((arrIdx, eleIdx + 1, A[arrIdx][eleIdx + 1]))
        print(result)
        return result
        
    

class MinHeap:
    def __init__(self):
        self.heap = []
        
    def peek(self):
        return self.heap[0]
        
    @property
    def size(self):
        return len(self.heap)
        
    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]
        
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.size - 1)
        
    def siftUp(self, curIdx):
        while curIdx > 0:
            parIdx = (curIdx - 1) // 2
            
            if self.heap[curIdx][2] < self.heap[parIdx][2]:
                self.swap(curIdx, parIdx)
                curIdx = parIdx
            else:
                break
    
    def remove(self):
        removedItem = self.heap[0]
        self.swap(0, self.size - 1)
        self.heap.pop()
        self.siftDown(0)
        return removedItem
    
    def siftDown(self, idx):
        endIdx = self.size - 1
        while 2 * idx + 1 <= endIdx:
            c1Idx = 2 * idx + 1
            c2Idx = 2 * idx + 2
            swapIdx = c1Idx
            if c2Idx <= endIdx and self.heap[c1Idx][2] > self.heap[c2Idx][2]:
                swapIdx = c2Idx
                
            if self.heap[swapIdx][2] < self.heap[idx][2]:
                self.swap(swapIdx, idx)
                idx = swapIdx
            else:
                break 
            
Solution().solve(A = [[1, 2, 3, 11,13], [2, 4, 6], [0, 9, 10]])           
            
            
            
            
            
        
        
        
        
        
        
        
        