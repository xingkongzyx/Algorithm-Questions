""" 
/ bubble up(insert): Time: O(logn)
/ sift down(removal): Time: O(logn)
/ build heap: Time O(n) time
"""

class MinHeap:
    def __init__(self):
        self.heap = []
    
    @property
    def size(self):
        return len(self.heap)
    
    def peek(self):
        return self.heap[0]
    
    def insert(self, value):
        """
        * 添加元素
        * 第一步，把元素加入到数组末尾
        * 第二步，把末尾元素向上调整
        """
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)
        
    def siftUp(self, currentIdx):
        """
        * 向上调整
        * 第一步，确定当前元素不是堆顶元素，不是的话进入 siftUp 步骤
        * 第二步，找到「父节点」在 heap 数组中的位置
        * 第三步，如果「父节点」和当前节点满足交换的关系（对于小顶堆是「父节点」元素更大），则将当前节点向上调整
        * 如果「父节点」比当前节点小，说明已经满足最小堆的性质，break
        """
        while currentIdx > 0:
            parentIdx = (currentIdx - 1) // 2
            if self.heap[currentIdx] < self.heap[parentIdx]:
                self.swap(currentIdx, parentIdx)
                currentIdx = parentIdx
            else:
                break
            
    def remove(self):
        """
        * 弹出堆顶
        * 第一步，记录堆顶元素的值
        * 第二步，交换堆顶元素与末尾元素
        * 第三步，删除数组末尾元素
        * 第四步，新的堆顶元素向下调整
        * 第五步，返回答案
        """
        item = self.heap[0]
        self.swap(0, len(self.heap) - 1)
        self.heap.pop()
        self.siftDown(0)
        return item

    
    def siftDown(self, currentIdx):
        endIdx = len(self.heap) - 1
        #* 如果「左子节点」的索引已经越界，终止下沉
        while currentIdx * 2 + 1 <= endIdx:
            #* 记录「左子节点」在 heap 中的位置(由于 while 的判断条件, 确定它一定存在)
            childOneIdx = currentIdx * 2 + 1
            
            #* 记录「右子节点」在 heap 中的位置(此时不确定它是否存在)
            childTwoIdx = currentIdx * 2 + 2
            
            #* 记录下沉过程中「可能的」用于交换的子节点，默认为「左子节点」。
            ## 此时不能确定是否满足下沉交换条件，这只是「可能的」用于交换的子节点
            childIdxToSwap = childOneIdx
            #* 如果「右子节点」存在且它的值比「左子节点」更小，则用它作为待交换的节点
            if childTwoIdx <= endIdx and self.heap[childTwoIdx] < self.heap[childOneIdx]:
                childIdxToSwap = childTwoIdx
            
            #* 因为是 minHeap, 如果 currentIdx 代表的数字比前面记录的「可能的」用于交换的子节点都大，则进行交换
            if self.heap[childIdxToSwap] < self.heap[currentIdx]:
                self.swap(childIdxToSwap, currentIdx)
                currentIdx = childIdxToSwap
            else:
                break
                  
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]



heap = MinHeap()
heap.insert(4)
heap.insert(1)
heap.insert(5)
heap.insert(3)
heap.insert(2)
print(heap.heap)