""" 
? 使用优先队列的: 
? ➀ https://leetcode.cn/problems/task-scheduler/solution/ren-wu-diao-du-you-xian-dui-lie-tan-xin-n95iv/ 
? ➁ https://leetcode.com/problems/task-scheduler/discuss/130786/Python-solution-with-detailed-explanation
/ Time complexity is O(N * n) where N is the number of tasks and n is the cool-off period.
/ Space complexity is O(1) - will not be more than O(26).

=== 核心思路 ===
贪心 + 最大堆：每轮在长度为 n+1 的时间窗口内，优先执行频次最高的任务，
窗口内无任务可执行时就 idle，直到所有任务完成。

=== 三个数据结构的关系 ===
task_map → heap ⇄ tempList

1. task_map（字典）: 统计每种任务的出现频次，是一次性的中间产物
2. heap（最大堆）: 按频次降序存储任务，负责决定 "下一个该执行谁"（贪心核心）
3. tempList（临时列表）: 暂存本轮已执行但尚未完成的任务，防止同一轮内重复执行同种任务

数据流转:
  初始化: task_map → heap（一次性搬运）
  每轮内: heap 弹出 → 执行 → 未完成的暂存到 tempList
  每轮末: tempList 全部放回 → heap（下一轮可重新参与选择）

=== 为什么窗口大小是 n+1？ ===
题目要求：相同任务之间必须间隔至少 n 个时间单位。
每轮窗口 = "执行任务本身(1)" + "冷却期(n)" = n+1 个时间槽。

把每一轮想象成一个固定宽度为 n+1 的 "盒子"：
  ┌─────────────┐ ┌─────────────┐
  │  A   B  idle │ │  A   B  idle │    （n=2, 盒子宽 3）
  │  第 1 轮     │ │  第 2 轮     │
  └─────────────┘ └─────────────┘

每种任务在一个盒子里最多出现一次（tempList 隔离保证）。
盒子宽度是 n+1，所以同种任务两次出现之间天然就隔了至少 n 格。

=== 如何确保所有任务（不只是最高频的）都满足间隔要求？ ===
两个机制配合：
1. 盒子宽度 n+1 → 提供间隔的 "物理空间"
2. 频次排序的稳定性 → 保证任务在盒子内的位置不会剧烈前移

详解：堆每次弹出频次最高的任务，所以每轮内 slot 1 给频次最高的，
slot 2 给次高的……每轮所有任务频次都减 1，相对排名基本稳定。
因此同一任务在相邻两轮中的 slot 位置不会剧烈前移，间隔始终 ≥ n。

举例: tasks=["A","A","A","B","B","B"], n=2
  第 1 轮: t=1(A) t=2(B) t=3(idle)
  第 2 轮: t=4(A) t=5(B) t=6(idle)
  第 3 轮: t=7(A) t=8(B)  ← 堆空+tempList空, break
  A 的间隔: t4-t1=3≥2 ✅  B 的间隔: t5-t2=3≥2 ✅
"""

class Solution(object):
    def leastInterval(self, tasks, n):
        #* 阶段 1: 统计频次 → task_map 是数据的入口
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        
        #* 阶段 2: 将频次数据搬入最大堆（一次性操作，之后 task_map 不再使用）
        #* 堆按频次降序排列，确保每次弹出的都是当前剩余次数最多的任务（贪心策略）
        heap = MaxHeap()
        for key, val in task_map.items():
            heap.insert((key, val))
        
        #* 记录总的任务时间
        totalTime = 0
        
        #* 外层循环：只要堆中还有任务，就继续调度
        while heap.size:
            #* tempList 是冷却的 "屏障"：
            #* 本轮已执行但未完成的任务暂存在这里，防止同一轮内被重复选中。
            #* 如果直接放回堆，下一个 slot 可能又弹出同一任务，违反冷却约束！
            #* 例: n=2 时如果 A(3) 弹出后立刻放回，slot2 堆顶又是 A(2)，间隔=0 < 2 ❌
            tempList = []
            
            #* 用于记录当前轮内已经过了多少个时间槽
            count = 0
            
            #* 内层循环：一轮 = n+1 个时间槽（count 从 0 到 n）
            #* 为什么是 n+1？因为 "执行任务(1格)" + "冷却间隔(n格)" = n+1 格
            #* 这个固定宽度的窗口是保证所有任务满足冷却约束的核心机制：
            #*   - 每种任务在一个窗口内最多出现一次（tempList 隔离）
            #*   - 窗口宽 n+1，所以同种任务两次出现间隔 ≥ n
            while count <= n:
                totalTime += 1
                
                if heap.size > 0:
                    #* 贪心：每次弹出频次最高的任务执行
                    taskLetter, taskFreq = heap.remove()
                    taskFreq -= 1
                    #* 频次 > 0 说明还没做完，暂存到 tempList（不能放回堆！）
                    if taskFreq > 0:
                        tempList.append((taskLetter, taskFreq))
                #* else: 堆已空但本轮未结束 → idle（空转），totalTime 仍然 +1
                
                #* 提前退出：堆空 + tempList 空 = 所有任务已完成
                #* 避免在最后一轮末尾多算不必要的 idle 时间
                if heap.size == 0 and len(tempList) == 0:
                    break
                else:
                    count += 1
            
            #* 本轮结束，将 tempList 中暂存的任务全部放回堆
            #* 此时冷却期已过，它们可以在下一轮被重新选中执行
            #* 数据流: heap → (本轮执行) → tempList → (轮末回收) → heap
            for taskFreqPair in tempList:
                heap.insert(taskFreqPair)
                
        return totalTime
                
             
            
    
class MaxHeap:
    """自定义最大堆（Python 标准库 heapq 只支持最小堆）
    
    存储元素为 (taskLetter, taskFreq) 元组，按 taskFreq（索引 [1]）降序排列。
    核心操作:
      - insert: 插入元素 + siftUp 上浮维护堆性质
      - remove: 弹出堆顶（频次最大的任务）+ siftDown 下沉
    """
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
