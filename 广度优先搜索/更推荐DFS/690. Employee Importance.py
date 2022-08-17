""" 
/ 时间复杂度: O(n), 其中 n 是员工数量。需要遍历所有员工, 在哈希表中存储员工编号和员工的对应关系, 广度优先搜索对每个员工遍历一次。

/ 空间复杂度: O(n), 其中 n 是员工数量。空间复杂度主要取决于哈希表的空间和队列的空间, 哈希表的大小为 n, 队列的大小不超过 n。
"""


class Solution(object):
    from collections import deque

    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        emplDict = {}
        for employee in employees:
            emplDict[employee.id] = employee

        totalImportance = 0

        queue = deque([])
        queue.append(id)

        while len(queue) > 0:
            currentEmployeeIdx = queue.popleft()
            totalImportance += emplDict[currentEmployeeIdx].importance

            for idx in emplDict[currentEmployeeIdx].subordinates:
                queue.append(idx)

        return totalImportance
