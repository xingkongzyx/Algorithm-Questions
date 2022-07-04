
""" 
* 用哈希表存储每个字符的出现次数，再通过一个大顶堆（根据出现次数排序），不断取出堆顶元素，使用 result string 不断承接弹出的元素就行

* ➀ 先使用「哈希表」对词频进行统计；
* ➁ 遍历统计好词频的哈希表，将每个键值对以 {字符,词频} 的形式存储到「优先队列（堆）」中。并规定「优先队列（堆）」排序逻辑为：
*     ◎如果 词频 不同，则按照 词频 倒序；
* ➂ 从「优先队列（堆）」依次弹出，构造答案。

/ 时间复杂度：令字符集的大小为 C。使用「哈希表」统计词频的复杂度为 O(n)；最坏情况下字符集中的所有字符都有出现，最多有 C 个节点要添加到「优先队列（堆）」中，复杂度为 O(ClogC)；构造答案需要从「优先队列（堆）」中取出元素并拼接，复杂度为 O(n)。整体复杂度为 O(max(n,ClogC))
/ 空间复杂度：O(n)


链接：https://leetcode.cn/problems/sort-characters-by-frequency/solution/gong-shui-san-xie-shu-ju-jie-gou-yun-yon-gst9/


"""
class Solution(object):
    def frequencySort(self, s):
        record = {}
        
        for i in range(len(s)):
            curChar = s[i]
            record[curChar] = record.get(curChar, 0) + 1
            
        maxHeap = MaxHeap()
        for char, frequency in record.items():
            maxHeap.insert((char, frequency))
            
        print(maxHeap.heap)
        result = ""
        heapSize = maxHeap.size
        
        for i in range(heapSize):
            poppedVal = maxHeap.remove()
            result += (poppedVal[0] * poppedVal[1])
        # print(result)
        return result
        

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
            if self.heap[currentIdx][1] > self.heap[parentIdx][1]:
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
            if childTwoIdx <= endIdx and self.heap[childTwoIdx][1] > self.heap[childOneIdx][1]:
                childIdxToSwap = childTwoIdx
            
            #* 因为是 maxHeap, 如果「当前节点」比前面记录的「可能的」用于交换的「子节点」都小，则进行交换
            if self.heap[currentIdx][1] < self.heap[childIdxToSwap][1]:
                self.swap(childIdxToSwap, currentIdx)
                currentIdx = childIdxToSwap
            else:
                break
                   
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


Solution().frequencySort("cccaaa")
