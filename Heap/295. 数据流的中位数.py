# 同剑指 offer 41
import heapq

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

We use heapq class to implement Heaps in Python. By default Min Heap is implemented by this class. But we multiply each value by -1 so that we can use it as MaxHeap.
 """
