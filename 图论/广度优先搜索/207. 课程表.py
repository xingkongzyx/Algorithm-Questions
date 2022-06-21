# https://leetcode.cn/problems/course-schedule/solution/ke-cheng-biao-by-leetcode-solution/
from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #* 创建入度数组，记录每个课程的初始入度
        #* 入度数组：课号 0 到 n - 1 作为索引，通过遍历先决条件表求出对应的初始入度。 
        inDegree = [0 for _ in range(numCourses)]
        for courseIdx, prerequisiteCourseIdx in prerequisites:
            inDegree[courseIdx] += 1
        # print(inDegree)
        #* 创建 hashmap. key：课号，value：依赖这门课的后续课（数组）
        courseMap = {}
        for course, prerequisiteCourse in prerequisites:
            if prerequisiteCourse not in courseMap:
                courseMap[prerequisiteCourse] = []
            courseMap[prerequisiteCourse].append(course)
                 
        # print(courseMap)
        
        #* 初始化 queue, 将入度为0的课程放入待处理的queue中
        queue = deque([])
        for course, courseDegree in enumerate(inDegree):
            if courseDegree == 0:
                queue.append(course)

        numOfTakenCourses = 0
        ## 让入度为 0 的课入列，它们是能直接选的课。然后逐个出列，出列代表着课被选，需要减小相关课的入度。 如果相关课的入度新变为 0，安排它入列、再出列……直到没有入度为 0 的课可入列。
        while len(queue) > 0:
            currentTakenCourse = queue.popleft()
            # print(f"current taken course is {currentTakenCourse}")
            numOfTakenCourses += 1
            #* 遍历课程hashmap，看courseMap中哪些课程是依赖currentTakenCourse作为前置课，减少这些课程的入度数

            #* 首先确认这门课确实有后置课，没有的话直接继续循环
            if currentTakenCourse not in courseMap:
                continue
            #* 减少以currentTakenCourse作为前置课程的这些课程的入度数
            # print(f"the prerequisiteCourse and later courses are {currentTakenCourse}, {courseMap[currentTakenCourse]}")
            for course in courseMap[currentTakenCourse]:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    queue.append(course)
            # print(f"current queue is {queue} \n\n")

        return numOfTakenCourses == numCourses


        
s = Solution()
prerequisites = [[3, 0], [3, 1], [4, 1], [4, 2], [5, 3], [5, 4]]
numCourses = 6
s.canFinish(numCourses, prerequisites)