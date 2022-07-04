""" 
* ➀ 利用 hashmap 统计元素出现的频次, 建立元素与频次之间的映射
* ➁ 创建元素个数为 k 的「小顶堆 minHeap」
* ➂ 遍历 hashmap, 当 minHeap 中元素个数小于 k 时, 直接加入 minHeap 
* ➃ 如果 minHeap 中元素个数等于 k 时, 新元素的「频次」与堆顶元素「频次」比较, 如果比堆顶元素「频次」高, 调用 remove 方法移除堆顶元素, 然后再插入新的元素, 如果比堆顶元素「频次」还要低, 则不处理
* ➄ 最后使用数组保存「频次」前k的元素

* 时间复杂度
* a. 统计频率, 需要遍历一遍数组, 所需要的时间复杂度为O(n), hashmap的插入、查找的时间复杂度为O(1), 所以统计频率过程时间复杂度为O(n).
* b. 遍历hashmap的时间复杂度时间复杂度O(n), 维护元素个数为k的小顶堆时间复杂度为O(logk),  这个过程时间复杂度为O(nlogk).
* c. 把优先队列转换为数组时间复杂度为O(k).
* d. 综上所述, 整体时间复杂度为 O(nlogk).

* 空间复杂度
* a. 创建hashmap, 最坏情况, 当没有相同元素时, 复杂度为O(n)
* b. 小顶堆空间复杂度为O(k)
* c. 保存频率前k的元素数组, 复杂度O(k)
* d. 综上, 空间复杂度为O(n)

? https://leetcode.cn/problems/top-k-frequent-elements/solution/hashmaptong-ji-pin-ci-you-xian-du-lie-by-nchkdxlq/

"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        record = {}
        
        for num in nums:
            record[num] = record.get(num, 0) + 1
        print(record)
        minHeap = MinHeap()
        
        for num, frequency in record.items():
            if(minHeap.size < k):
                minHeap.insert((num, frequency))
            else:
                if frequency > minHeap.peak()[1]:
                    minHeap.remove()
                    minHeap.insert((num, frequency))
            
        # print(minHeap.heap) 
  
        result = []
        for i in range(minHeap.size):
            result.append(minHeap.heap[i][0])
        
        # print(result)
        return result
            


class MinHeap:
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
            if(self.heap[parentIdx][1] > self.heap[currentIdx][1]):
                self.swap(parentIdx, currentIdx)
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
            
            if(childTwoIdx <= endIdx and self.heap[childTwoIdx][1] < self.heap[childOneIdx][1]):
                childIdxToSwap = childTwoIdx
                
            if self.heap[currentIdx][1] > self.heap[childIdxToSwap][1]:
                self.swap(currentIdx, childIdxToSwap)
                currentIdx = childIdxToSwap
            else:
                break
    
    def peak(self):
        return self.heap[0]
                
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]            

print(Solution().topKFrequent(nums = [1], k = 1))
