""" 
* 1. 递归参数和返回值: 返回当前员工和他下属的总的importance, 参数为现在正在获取重要性的员工id
* 2. 递归终止条件: 当当前员工没有下属了, 便会直接返回目前的 totalImportance
* 3. 本层递归: 遍历这个员工的所有下属, 获取所有下属的 importance, 最后再加上当前员工的importance一起返回


/ 时间复杂度: O(n), 其中 n 是员工数量。需要遍历所有员工, 在哈希表中存储员工编号和员工的对应关系, 深度优先搜索对每个员工遍历一次。
/ 空间复杂度: O(n), 其中 n 是员工数量。空间复杂度主要取决于哈希表的空间和递归调用栈的空间, 哈希表的大小为 n, 栈的深度不超过 n。
? 代码: https://leetcode.cn/problems/employee-importance/solution/yuan-gong-de-zhong-yao-xing-python3shen-du-you-xia/
? 时间复杂度: https://leetcode.cn/problems/employee-importance/solution/yuan-gong-de-zhong-yao-xing-by-leetcode-h6xre/

 """


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        # * ➀ 使用hashmap建立员工id与员工的映射关系
        emplDict = {}
        for employee in employees:
            emplDict[employee.id] = employee

        # * ➁ 使用DFS或BFS实现对员工的遍历
        #! ! 这里并没有像遍历树时有明确的 if node == None 这样的终止条件, 当正在访问的 employee 没有下属时自动不会进入下一次的递归
        def DFS(currentId):
            totalImportance = emplDict[currentId].importance

            for subordinate in emplDict[currentId].subordinates:
                totalImportance += DFS(subordinate)

            return totalImportance

        return DFS(id)
