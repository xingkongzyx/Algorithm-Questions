'''
#/ BFS 思路
#/ queue 队列中始终是【入度为 0 的课】在里面流动
#/ 选择一门课，就让它 出列，同时 查看哈希表，看它 对应哪些后续课
#/ 将这些后续课的 入度 - 1，如果有 减至 0 的，就将它 推入 queue
#/ 不再有新的入度 0 的课入列 时，此时 queue 为空，退出循环

链接：https://leetcode.cn/problems/course-schedule-ii/solution/bao-mu-shi-ti-jie-tuo-bu-pai-xu-si-lu-zen-yao-yi-2/


'''

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """ 
        from collections import deque

        inDegree = [0 for _ in range(numCourses)]
        courseMap = {}

        for course, prerequisiteCourse in prerequisites:
            inDegree[course] += 1
            if prerequisiteCourse not in courseMap:
                courseMap[prerequisiteCourse] = []
            courseMap[prerequisiteCourse].append(course)

        queue = deque([])
        for idx, courseDegree in enumerate(inDegree):
            if courseDegree == 0:
                queue.append(idx)
        numOfTakenCourses = 0
        courseSchedule = []
        while queue:
            currentTakenCourse = queue.popleft()
            courseSchedule.append(currentTakenCourse)
            numOfTakenCourses += 1

            if currentTakenCourse not in courseMap:
                continue
            
            for course in courseMap[currentTakenCourse]:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    queue.append(course)
        
        return courseSchedule if numOfTakenCourses == numCourses else []


s = Solution()
# prerequisites = [[3, 0], [3, 1], [4, 1], [4, 2], [5, 3], [5, 4]]
# numCourses = 6
prerequisites = [[1,0]]
numCourses = 2
courseSchedule = s.findOrder(numCourses, prerequisites)
print(courseSchedule)