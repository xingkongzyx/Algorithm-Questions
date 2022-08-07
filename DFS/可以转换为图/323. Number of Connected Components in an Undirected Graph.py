""" 
* 使用 DFS 解法需要建立「邻接链表」表示 graph, 然后在其基础上进行DFS。
# 当我们建立「邻接链表」后, 题目的解法就已经与 547 一模一样了.
* 通过「搜索」图来解决「连通分量」问题是非常经典的做法。设置一个 boolean visited 数组, 大小为顶点数, 表示在此后的搜索中是否访问过。我们遍历顶点, 对当前顶点 u , 以它为起始点开始搜索, 只要能够通过 u 连通到的顶点 v, 均标记 visited[v] = true 。那么对于 u , 一次搜索过后, 一定已经找到了包含它的那个「连通分量」, 且该分量中的所有顶点都已被标记为「已访问」。遍历顶点过程中, 跳过那些已访问的点。我们总能保证考察一个「连通分量」的起始顶点, 并完成该「连通分量」的遍历。于是, 有多少个这样的「起点」, 就有多少个「连通分量」。 当采用 dfs 来执行遍历时, 即为本解法。

? https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/solution/by-yukiyama-y5l4/
/ 时间复杂度: O(|V|+|E|), 完成一遍图的遍历。
/ 空间复杂度: O(|V|+|E|), 存图空间。
"""


class Solution:
    def countComponents(self, n, edges):
        connected_graph = [[False for _ in range(n)] for _ in range(n)]
        for fromNode, toNode in edges:
            connected_graph[fromNode][toNode] = True
            connected_graph[toNode][fromNode] = True

        visited = [False for _ in range(n)]

        def DFS(nodeIdx):
            visited[nodeIdx] = True
            for i in range(len(connected_graph[nodeIdx])):
                if visited[i] == False and connected_graph[nodeIdx][i] == True:
                    DFS(i)

        count = 0
        for nodeIdx in range(len(connected_graph)):
            # * 如果没有访问过, 说明有另外一组「连通分量」
            if visited[nodeIdx] != True:
                DFS(nodeIdx)
                count += 1

        return count


Solution().countComponents(3, [[1, 0], [2, 0]])
