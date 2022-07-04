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
        """
        * 添加元素
        * 第一步，把元素加入到数组末尾
        * 第二步，把末尾元素向上调整
        """
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)
        
    
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

    
    def siftUp(self, currentIdx):
        """
        * 向上调整
        * 第一步，确定当前元素不是堆顶元素，不是的话进入 siftUp 步骤
        * 第二步，找到「父节点」在 heap 数组中的位置
        * 第三步，如果「父节点」和「当前节点」满足交换的关系（对于大顶堆是「父节点」元素比「当前节点」元素更小），则将「当前节点」向上调整
        * 如果「父节点」比「当前节点」大，说明已经满足最大堆的性质，break
        """
        while currentIdx > 0:
            parentIdx = (currentIdx - 1) // 2
            if self.heap[currentIdx] > self.heap[parentIdx]:
                self.swap(currentIdx, parentIdx)
                currentIdx = parentIdx
            else:
                break
    
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
            #* 如果「右子节点」存在且它的值比「左子节点」更大，则用它作为待交换的节点
            if childTwoIdx <= endIdx and self.heap[childTwoIdx] > self.heap[childOneIdx]:
                childIdxToSwap = childTwoIdx
            
            #* 因为是 maxHeap, 如果「当前节点」比前面记录的「可能的」用于交换的「子节点」都小，则进行交换
            if self.heap[currentIdx] < self.heap[childIdxToSwap]:
                self.swap(childIdxToSwap, currentIdx)
                currentIdx = childIdxToSwap
            else:
                break
                   
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


heap = MaxHeap()
heap.insert(2)
heap.insert(4)
heap.insert(6)
heap.insert(10)
heap.insert(-1)
print(heap.heap)
heap.remove()
print(heap.heap)
heap.remove()
print(heap.heap)
