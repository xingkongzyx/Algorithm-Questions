""" 
* 在本题中，我们可以创建一个小根优先队列（顾名思义，就是优先队列顶端元素是最小元素的优先队列）。我们将每一个字符串插入到优先队列中，如果优先队列的大小超过了 k，那么我们就将优先队列顶端元素弹出。这样最终优先队列中剩下的 k 个元素就是前 k 个出现次数最多的单词。

? 思路来源: https://leetcode.cn/problems/top-k-frequent-words/solution/xiao-gen-dui-huo-zhe-hashbiao-pai-xu-by-9uj06/

? 调用 python 库函数: https://leetcode.cn/problems/top-k-frequent-words/solution/pythonyou-xian-dui-lie-by-luo-bi-da-quan-w8me/

/ 时间复杂度: 使用哈希表统计词频，复杂度为 O(n)；使用最多 n 个元素维护一个大小为 k 的堆，复杂度为 O(nlogk)；输出答案时颠倒数组, 复杂度为 O(k), 同时 k≤n。整体复杂度为 O(nlogk)
/ 空间复杂度: O(n)

? https://leetcode.cn/problems/top-k-frequent-words/solution/gong-shui-san-xie-xiang-jie-shi-yong-ha-8dxt2/
"""


class Solution:
    def topKFrequent(self, words, k):
        wordDic = {}

        for word in words:
            wordDic[word] = wordDic.get(word, 0) + 1

        heap = MinHeap()
        for word in wordDic:
            if heap.size < k:
                heap.insert((wordDic[word], word))
            else:
                heap.insert((wordDic[word], word))
                heap.remove()

        res = []
        # print(heap.heap)
        while heap.size:
            res.append(heap.remove()[1])

        return res[::-1]


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
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)

    def siftUp(self, currentIdx):
        while currentIdx > 0:
            parentIdx = (currentIdx - 1) // 2
            if self.compare(currentIdx, parentIdx):
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
        # * 如果「左子节点」的索引已经越界, 终止下沉
        while currentIdx * 2 + 1 <= endIdx:
            # * 记录「左子节点」在 heap 中的位置(由于 while 的判断条件, 确定它一定存在)
            childOneIdx = currentIdx * 2 + 1

            # * 记录「右子节点」在 heap 中的位置(此时不确定它是否存在)
            childTwoIdx = currentIdx * 2 + 2

            # * 记录下沉过程中「可能的」用于交换的子节点, 默认为「左子节点」。
            # 此时不能确定是否满足下沉交换条件, 这只是「可能的」用于交换的子节点
            childIdxToSwap = childOneIdx
            # * 如果「右子节点」存在且它的值比「左子节点」更小, 则用它作为待交换的节点
            if childTwoIdx <= endIdx and self.compare(childTwoIdx, childOneIdx):
                childIdxToSwap = childTwoIdx

            # * 因为是 minHeap, 如果 currentIdx 代表的数字比前面记录的「可能的」用于交换的子节点都大, 则进行交换
            if self.compare(childIdxToSwap, currentIdx):
                self.swap(childIdxToSwap, currentIdx)
                currentIdx = childIdxToSwap
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def compare(self, index1, index2):
        """ 
        * self.heap[idx][0]: 代表单词的频率
        * self.heap[idx][1]: 代表单词的本身
        * 如果 self.heap[index1] 代表的单词的出现次数小于 self.heap[index2] 代表的单词的出现次数, 返回 True. 或者, 如果两个 index 代表的单词的出现频率「相等」的时候我们需要按照「单词的字典序」从小到大排列。如果 self.heap[index1] 代表的单词的字典序「落后」于 self.heap[index2] 代表的单词的字典序, 也返回True
        # 这里使用「落后」, 但是当我们从 heap 中一个个 remove 元素得到的就是「频率由小到大，同频率单词的字典序由大到小」的结果数组，再一 reverse 数组，则能得到正确答案 -  sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
         """
        if self.heap[index1][0] < self.heap[index2][0] or (
            self.heap[index1][0] == self.heap[index2][0] and
            self.heap[index1][1] > self.heap[index2][1]
        ):
            return True

        return False
