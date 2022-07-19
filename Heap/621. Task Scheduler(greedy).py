""" 
! 要使完成任务所需要的时间最短，即要把任务次数的数量多的先安排
? 使用代码中方法的: 
? https://leetcode.cn/problems/task-scheduler/solution/jian-ming-yi-dong-de-javajie-da-by-lan-s-jfl9/
? https://leetcode.cn/problems/task-scheduler/solution/python-xiang-jie-by-jalan/ 
"""
class Solution(object):
    def leastInterval(self, tasks, n):
        length = len(tasks)
        if length <= 1:
            return length
        
        #* 用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        #* 按任务出现的次数从大到小排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        
        #* 出现最多次任务的次数
        max_task_count = task_sort[0][1]
        #* 至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)
        
        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1
        
        """ 
        # 当算出来的结果小于数组长度, 说明所有的冷却单位都被插满了, 但是还有任务没被插进去。这种情况说明这个数组的任务无需冷却时间, (退化成了n=0这种情况), 所以最短时间就是数组长度。
        * 为什么使用 max 呢 
        * 考虑一个任务种类足够多的情况, 例如 tasks 为 [A, A, A, A, B, C, D, E, F, G, H], n 为 2。可能的安排方案为: 
        * [[A,B,C], [A,D,E], [A,F,G], [A,H]]（评论区没办法发图片, 可以按照上面的方格图来理解一下这个安排）。这种情况如果使用公式来算的话, 由于 maxTimes为 4, maxCount 为 1, 根据公式, 结果为「(4 - 1) * (2 + 1) + 1 = 10」。但是我们的方案明明使用了全部的 11 个任务, 且11才是最短的时间, 因为我们需要执行完tasks中所有的 11 个任务嘛。公式计算是没有考虑到这种情况的, 所以需要在最后做一步判断。    
        """
        return max(res, length)
