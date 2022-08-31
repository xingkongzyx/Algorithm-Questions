""" 
* 可以把 dislikes 中每个元组看成结点之间的边, 根据结点关系画出图, 相邻的结点之间的颜色不能相同。如果我们能够利用两种颜色把所有结点着色就说明可以把这些结点分为两类。建完图以后的步骤与 785 一模一样。

? https://leetcode.cn/problems/possible-bipartition/solution/tu-zhao-se-c-dfschu-li-er-bu-tu-de-ran-s-wx54/

"""


class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        graph = defaultdict(list)

        # # 与 785 的不同就是这里要自己建图
        for v1, v2 in dislikes:
            graph[v1].append(v2)
            graph[v2].append(v1)

        # # 与 785 代码一模一样
        colors = [0 for _ in range(n + 1)]

        def DFS(curNode, curColor):
            if colors[curNode] != 0:
                if colors[curNode] != curColor:
                    return False
                return True

            colors[curNode] = curColor

            for neighborNode in graph[curNode]:
                neighborCheck = DFS(neighborNode, -curColor)
                if neighborCheck == False:
                    return False

            return True

        for node in range(1, len(colors)):
            if colors[node] == 0:
                check = DFS(node, 1)
                if check == False:
                    return False
        return True
