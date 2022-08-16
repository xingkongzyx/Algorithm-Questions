from collections import deque


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
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
        #! 唯一与 207 不同的地方: 这道题是使用一个数组记录上过的课程以及其完成顺序
        takenCourses = []
        # # 逐个出列, 出列代表着课被选, 需要减小其对应的「后续课程」的入度. 如果「后续课程」的入度减小后变为 0, 安排它入列. 循环往复, 直到没有入度为 0 的课可入列.
        while len(queue) > 0:
            currentTakenCourse = queue.popleft()
            # print(f"current taken course is {currentTakenCourse}")
            takenCourses.append(currentTakenCourse)
            # * 遍历课程hashmap, 看courseMap中哪些课程是依赖currentTakenCourse作为前置课, 减少这些课程的入度数

            # * 首先确认这门课确实有后置课, 没有的话直接继续循环
            if currentTakenCourse not in courseMap:
                continue
            # * 减少以currentTakenCourse作为前置课程的这些课程的入度数
            for course in courseMap[currentTakenCourse]:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    queue.append(course)

        if len(takenCourses) == numCourses:
            return takenCourses
        else:
            return []
