""" 
* 题目可以转换为「有向无环图」, 把一个「有向无环图」转成「线性的排序」就叫〖拓扑排序〗. 
* 有向图有「入度」和「出度」的概念: 
* 如果存在一条有向边 A --> B, 则这条边给 A 增加了 1 个出度, 给 B 增加了 1 个入度. 
* 假设 prerequisites = [[3, 0], [3, 1], [4, 1], [4, 2], [5, 3], [5, 4]], 顶点 0、1、2 的入度为 0. 顶点 3、4、5 的入度为 2. 


? https://leetcode.cn/problems/course-schedule/solution/bao-mu-shi-ti-jie-shou-ba-shou-da-tong-tuo-bu-pai-/

* 思路: 我们使用一个「队列」来进行 "BFS". 初始时, 所有入度为 0 的节点都被放入队列中, 它们就是可以作为拓扑排序最前面的节点, 并且它们之间的相对顺序是无关紧要的. 
* 在"BFS"的每一步中, 我们取出队首的节点 u: 
*    ➩ 我们将 u 放入答案中；
*    ➩ 我们移除 u 的所有出边, 也就是将所有依赖于 u 的「后续节点」的入度减少 1. 如果某个「后续节点」 v 的入度变为 0, 那么我们就将 v 放入队列中. 
# 上面的思路类似于「广度优先搜索」, 因此我们可以将「广度优先搜索」的流程与拓扑排序的求解联系起来. 
/ 时间复杂度: O(n+m), 其中 n 为课程数, m 为先修课程的要求数. 这其实就是对图进行广度优先搜索的时间复杂度. 
/ 空间复杂度: O(n+m). 题目中是以列表形式给出的先修课程关系, 为了对图进行广度优先搜索, 我们需要存储成邻接表的形式, 空间复杂度为 O(n+m). 在广度优先搜索的过程中, 我们需要最多 O(n) 的队列空间（迭代）进行广度优先搜索. 因此总空间复杂度为 O(n+m). 
? https://leetcode.cn/problems/course-schedule/solution/ke-cheng-biao-by-leetcode-solution/
"""
from collections import deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # * 创建入度数组, 记录每个课程的初始入度
        # * 入度数组: 课号 0 到 n - 1 作为索引, 通过遍历先决条件表求出对应的初始入度.
        inDegree = [0 for _ in range(numCourses)]
        # * 创建 hashmap: key是课号, value是依赖这门课的后续课（数组）
        courseMap = {}
        for courseIdx, prerequisiteCourseIdx in prerequisites:
            inDegree[courseIdx] += 1
            if prerequisiteCourseIdx not in courseMap:
                courseMap[prerequisiteCourseIdx] = []
            courseMap[prerequisiteCourseIdx].append(courseIdx)

        # * 初始化 queue, 将入度为 0 的课程放入待处理的 queue 中, 它们是能直接选的课.
        queue = deque([])
        for course, courseDegree in enumerate(inDegree):
            if courseDegree == 0:
                queue.append(course)

        numOfTakenCourses = 0
        # # 逐个出列, 出列代表着课被选, 需要减小其对应的「后续课程」的入度. 如果「后续课程」的入度减小后变为 0, 安排它入列. 循环往复, 直到没有入度为 0 的课可入列.
        while len(queue) > 0:
            currentTakenCourse = queue.popleft()
            # print(f"current taken course is {currentTakenCourse}")
            numOfTakenCourses += 1

            # * 遍历课程hashmap, 看courseMap中哪些课程是依赖currentTakenCourse作为前置课, 减少这些课程的入度数

            # * 首先确认这门课确实有后置课, 没有的话直接继续循环
            if currentTakenCourse not in courseMap:
                continue
            # * 减少以currentTakenCourse作为前置课程的这些课程的入度数
            for course in courseMap[currentTakenCourse]:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    queue.append(course)

        return numOfTakenCourses == numCourses


s = Solution()
prerequisites = [[3, 0], [3, 1], [4, 1], [4, 2], [5, 3], [5, 4]]
numCourses = 6
s.canFinish(numCourses, prerequisites)
