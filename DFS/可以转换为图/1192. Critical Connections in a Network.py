""" 
* 递归函数
* 从0开始去遍历, 找它的相邻结点, 对应的深度就是+1
* 遍历所有结果去找最小的深度, 一旦发现在遍历过程中子节点的深度比自己小或者一样, 那么有环的（它通过另外一条路径可达了）
* 一旦发现环, 则从前面说的集合里删除即可
* 
? https://leetcode.com/problems/critical-connections-in-a-network/discuss/382638/DFS-detailed-explanation-O(orEor)-solution
? 中文翻译: https://leetcode.cn/problems/critical-connections-in-a-network/solution/dfsfan-yi-liao-xia-ying-wen-ban-zui-jia-da-an-by-k/
"""
from collections import defaultdict


class Solution(object):
    # * 构建一个已经排序的去重的 connections 的集合, 在整个遍历中, 一旦发现有回环的连接, 则从集合里删除, 最终结果就是这个集合
    def sortConnections(self, connections):
        sortedConnections = set()

        for conn in connections:
            conn.sort()
            sortedConnections.add((conn[0], conn[1]))

        return sortedConnections

    def criticalConnections(self, n, connections):
        # * 用于将 connections 转换为邻接表
        def makeGraph(connections):
            graph = defaultdict(list)
            for conn in connections:
                graph[conn[0]].append(conn[1])
                graph[conn[1]].append(conn[0])
            return graph

        graph = makeGraph(connections)
        connections = self.sortConnections(connections)
        rank = [-2] * n

        def dfs(node, depth):
            if rank[node] >= 0:
                # visiting (0<=rank<n), or visited (rank=n)
                return rank[node]
            rank[node] = depth
            min_back_depth = n
            for neighbor in graph[node]:
                if rank[neighbor] == depth - 1:
                    # don't immmediately go back to parent. that's why i didn't choose -1 as the special value, in case depth==0.
                    continue
                back_depth = dfs(neighbor, depth + 1)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            # this line is not necessary. see the "brain teaser" section below
            rank[node] = n
            return min_back_depth

        # since this is a connected graph, we don't have to loop over all nodes.
        dfs(0, 0)
        return list(connections)
