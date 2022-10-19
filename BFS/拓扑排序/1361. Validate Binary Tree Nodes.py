""" 「」
➀ 据题目描述, 一颗有效的二叉树必然是「没有环」, 且除了「唯一」的根节点的入度是 0 外, 其他的节点入度为 1。
➁ 如果存在「多个」入度为 0 的点(多个根) 或 存在入度「大于等于」 2 的点(多个父亲指向该点), 直接返回 False
➂ 如果存在环, 直接返回False。这里使用拓扑排序判断是否有环

? 带注释的代码: https://leetcode.cn/problems/validate-binary-tree-nodes/solution/zhunbu-by-made-on-earth-by-humans-er8g/
? python 版的代码: https://leetcode.cn/problems/validate-binary-tree-nodes/solution/yi-li-jie-de-you-xiang-tu-cheng-er-cha-s-t46i/
"""


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild) -> bool:
        from collections import defaultdict, deque

        graph = defaultdict(list)
        inDegree = [0 for _ in range(n)]

        # 首先统计每个节点的入度, 同时构建图
        for node in range(n):
            if leftChild[node] != -1:
                inDegree[leftChild[node]] += 1
                graph[node].append(leftChild[node])
            if rightChild[node] != -1:
                inDegree[rightChild[node]] += 1
                graph[node].append(rightChild[node])

        queue = deque([])

        for i in range(len(inDegree)):
            # 有节点有入度「大于等于 2」的情况, 说明某一个节点有多个父节点, 不满足二叉树的条件, 直接返回 False
            if inDegree[i] >= 2:
                return False
            if inDegree[i] == 0:
                queue.append(i)

        # 有多个入度为 0 的节点, 说明这棵树有「多个根节点」, 不满足二叉树的条件, 直接返回 False
        if len(queue) > 1:
            return False

        """
        * 最后使用「拓扑排序」, 判断图是否有环
        * 求出图中所有结点的出入度。
        * 将所有入度 === 0 的结点入队。
        * 当队列不空时, 弹出队首元素, 把与队首元素的左右子节点的入度减一。
        * 如果存在某个子节点的入度变为0, 则将该结点入队。
        * 循环结束时判断已经访问的结点数, 全部访问说明, 图无环; 存在没有访问到的结点, 则有环。

        """
        numOfNodes = 0
        while queue:
            curNode = queue.popleft()
            numOfNodes += 1
            for nxtNode in graph[curNode]:
                inDegree[nxtNode] -= 1
                if inDegree[nxtNode] == 0:
                    queue.append(nxtNode)

        return numOfNodes == n
