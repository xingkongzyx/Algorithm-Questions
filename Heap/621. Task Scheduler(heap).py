""" 
? 使用优先队列的: 
? ➀ https://leetcode.cn/problems/task-scheduler/solution/ren-wu-diao-du-you-xian-dui-lie-tan-xin-n95iv/ 
? ➁ https://leetcode.com/problems/task-scheduler/discuss/130786/Python-solution-with-detailed-explanation
/ Time complexity is O(N * n) where N is the number of tasks and n is the cool-off period.
/ Space complexity is O(1) - will not be more than O(26).
"""

class Solution(object):
    def leastInterval(self, tasks, n):
         #* 用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
            
        heap = MaxHeap()
        for key, val in task_map.items():
            heap.insert((key, val))
        
        #* 记录总的任务时间
        totalTime = 0
        
        #* Begin with scheduling the most frequent task. Then cool-off for n, and in that cool-off period schedule tasks in order of frequency, or if no tasks are available, then be idle.
        #! We only stop if we're out of tasks. So we need constantly checking the heap for if it's empty
        while heap.size:
            #* 中转战, 将剩余执行次数大于 0 的 task 放到这个中转站中
            tempList = []
            
            #* 用于记录执行 task 之间的 cool-off time
            count = 0
            
            #* 这里的总的 cool-off time 使用的是 n + 1, 之所以要加 1 是因为当前 task 也需要 1 单位的时间进行执行
            while count <= n:
                totalTime += 1
                
                if heap.size > 0:
                    #* 每次都是执行 the most frequent task in the heap
                    taskLetter, taskFreq = heap.remove()
                    taskFreq -= 1
                    #* We're checking to see if it's at the end of the overall count. Remember that it was positive at the beginning
                    if taskFreq > 0:
                        tempList.append((taskLetter, taskFreq))
                
                #* Checking to see if we're out of tasks. Exit the inner loop if both are true. This will automatically exit out of the overall tasks 
                if heap.size == 0 and len(tempList) == 0:
                    break
                else:
                    count += 1
            
            #* Because we transferred all of the items from the heap to tempList, we're transferring them back to know if we should continue
            #* heap -> If we're not out of tasks -> temp
            #* temp -> Because we're not out -> heap put items in tempList back to HEAP
            for taskFreqPair in tempList:
                heap.insert(taskFreqPair)
                
        return totalTime
                
             
            
    
class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
        
    def peek(self):
        return self.heap[0]
    
    @property
    def size(self):
        return len(self.heap)
    
    def insert(self, val):
        self.heap.append(val)
        self.siftUp(self.size - 1)
        
    def siftUp(self, idx):
        while idx > 0:
            parentIdx = (idx - 1) // 2

            if self.heap[parentIdx][1] < self.heap[idx][1]:
                self.swap(parentIdx, idx)
                idx = parentIdx
            else:
                break
    
    def remove(self):
        removedItem = self.heap[0]
        self.swap(0, self.size - 1)
        self.heap.pop()
        self.siftDown(0)
        return removedItem
    
    def siftDown(self, curIdx):
        endIdx = self.size - 1
        
        while 2 * curIdx + 1 <= endIdx:
            childOneIdx = 2 * curIdx + 1
            childTwoIdx = 2 * curIdx + 2
            swapChildIdx = childOneIdx
            
            if childTwoIdx <= endIdx and self.heap[childOneIdx][1] < self.heap[childTwoIdx][1]:
                swapChildIdx = childTwoIdx
                
            if self.heap[swapChildIdx][1] > self.heap[curIdx][1]:
                self.swap(swapChildIdx, curIdx)
                curIdx = swapChildIdx
            else:
                break
    
    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]
