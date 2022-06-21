class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        inDegree = [0 for _ in range(numCourses)]
        from collections import defaultdict, deque

        courseDict = defaultdict(list)
        for course, prerequisiteCourse in prerequisites:
            inDegree[course] += 1
            courseDict[prerequisiteCourse].append(course)
        # print(courseDict)
        # print(inDegree)
        queue = deque()
        for idx, val in enumerate(inDegree):
            if val == 0:
                queue.append(idx)
        while len(queue):
            takenCourse = queue.popleft()
            for laterCourse in courseDict[takenCourse]:
                inDegree[laterCourse] -= 1
                if inDegree[laterCourse] == 0:
                    queue.append(laterCourse)
        for ele in inDegree:
            if ele != 0:
                return False
        return True
s = Solution()
prerequisites = [[3, 0], [0, 3], [3, 1], [4, 1], [4, 2], [5, 3], [5, 4]]
numCourses = 6
check = s.canFinish(numCourses, prerequisites)
print(check)