""" 
! 这并不是最优解，三指针是更好的解决办法
* ➀ 很容易想到的方法是: 从1起检验每个数是否为丑数, 直到找到n个丑数为止。但是随着n的增大, 绝大部分数字都不是丑数, 我们枚举的效率非常低。
* ➁ 因此, 换个角度思考, 如果我们只生成丑数, 且生成n个, 这道题就迎刃而解。不难发现生成丑数的规律: 如果已知丑数ugly, 那么 ugly * 2, ugly * 3 和 ugly * 5 也都是丑数。
* ➂ 既然求第 n 小的丑数, 可以采用最小堆来解决。每次弹出堆中最小的丑数, 然后检查它分别乘以2、3和 5后的数是否生成过, 如果是第一次生成, 那么就放入堆中。第n个弹出的数即为第n小的丑数。

? 讲解: https://leetcode.cn/problems/ugly-number-ii/solution/1-zui-xiao-dui-2-dong-tai-gui-hua-san-zhi-zhen-pyt/
? 动画: https://leetcode.cn/problems/ugly-number-ii/solution/chou-shu-ii-by-leetcode-solution-uoqd/ 

/ 时间复杂度: O(nlogn). 得到第 n 个丑数需要进行 n 次循环, 每次循环都要从最小堆中取出 1 个元素以及向最小堆中加入最多 3 个元素, 因此每次循环的时间复杂度是O(log3n+3log3n)=O(logn), 总时间复杂度是 O(nlogn). 
/ 空间复杂度: O(n). 空间复杂度主要取决于最小堆和哈希集合的大小, 最小堆和哈希集合的大小都不会超过 3n. 
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        
        seenSet = {1}
        heap = MinHeap()
        heap.insert(1)
        
        #* removedCount 代表已经从 heap 中提取了多少个 ugly numbers, 如果这个值已经等于 n, 说明找到了 the nth ugly number, 进行返回
        removedCount = 0
        while removedCount < n:
            heapVal = heap.remove()
            
            firstCandidateUglyNum, secondCandidateUglyNum, thirdCandidateUglyNum = heapVal * 2, heapVal * 3, heapVal * 5
            
            if firstCandidateUglyNum not in seenSet:
                seenSet.add(firstCandidateUglyNum)
                heap.insert(firstCandidateUglyNum)

            if secondCandidateUglyNum not in seenSet:
                seenSet.add(secondCandidateUglyNum)
                heap.insert(secondCandidateUglyNum)

            if thirdCandidateUglyNum not in seenSet:
                seenSet.add(thirdCandidateUglyNum)
                heap.insert(thirdCandidateUglyNum)

            removedCount += 1
            
        return heapVal

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
            if self.heap[currentIdx] < self.heap[parentIdx]:
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
        while currentIdx * 2 + 1 <= endIdx:
            childOneIdx = currentIdx * 2 + 1
            childTwoIdx = currentIdx * 2 + 2
            childIdxToSwap = childOneIdx
            
            if childTwoIdx <= endIdx and self.heap[childTwoIdx] < self.heap[childOneIdx]:
                childIdxToSwap = childTwoIdx
            
            if self.heap[childIdxToSwap] < self.heap[currentIdx]:
                self.swap(childIdxToSwap, currentIdx)
                currentIdx = childIdxToSwap
            else:
                break
                  
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
