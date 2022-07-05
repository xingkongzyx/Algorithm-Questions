
""" 
https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
题目要求获取一个数据流排序后的中位数，那么可以使用两个优先队列（堆）实现。
该题使用一个大顶堆，一个小顶堆完成。

大顶堆的每个节点的值大于等于左右孩子节点的值，堆顶为最大值。
小顶堆的每个节点的值小于等于左右孩子节点的值，堆顶为最小值。
因此我们使用 大顶堆(maxHeap) 来存储数据流中较小一半的值，用 小顶堆(minHeap) 来存储数据流中较大一半的值。即“大顶堆的堆顶”与“小顶堆的堆顶”就是排序数据流的两个中位数。


根据堆的性质，可以判断两个堆的值从下往上递增，即：
maxHeap堆底 <= maxHeap堆顶 <= minHeap堆顶 <= minHeap堆底。

链接：https://leetcode.cn/problems/find-median-from-data-stream/solution/qing-xi-tu-jie-jian-zhi-offer41-shu-ju-l-rpen/


https://leetcode.cn/problems/find-median-from-data-stream/solution/tong-ge-lai-shua-ti-la-tu-jie-da-ding-du-ghiy/

We use heapq class to implement Heaps in Python. By default Min Heap is implemented by this class. But we multiply each value by -1 so that we can use it as MaxHeap.

/ 时间复杂度：addNum 函数的复杂度为 O(logn)；findMedian 函数的复杂度为 O(1)
/ 空间复杂度：O(n)

 """
import heapq


class MedianFinder(object):

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        #/ 小顶堆存储的是「比较大」的元素，当插入数据大于「小顶堆」的堆顶之时，就将该数据插入到「小顶堆」中；否则插入到「大顶堆」中。
        if len((self.minHeap)) == 0 or num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        
        #/ 如果 minHeap 比 maxHeap 多2个元素，就平衡一下
        if len(self.minHeap) - len(self.maxHeap) > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.minHeap) - len(self.maxHeap) < -1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        


    def findMedian(self):
        #* 如果当前堆中元素总数为奇数，则一定出于两堆的堆顶元素之一，且为数字较多堆的堆顶元素。
        #* 如果当前总数为偶数，则中位数是两堆的堆顶元素平均值。
        if len(self.minHeap) == len(self.maxHeap):
            return float(self.minHeap[0] - self.maxHeap[0])/2
        return self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else -self.maxHeap[0]
