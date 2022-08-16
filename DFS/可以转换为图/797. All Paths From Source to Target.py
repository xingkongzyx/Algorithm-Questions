""" 
> 回溯的模板题
? https://leetcode.cn/problems/all-paths-from-source-to-target/solution/tong-ge-lai-shua-ti-la-yi-ti-liang-jie-d-6764/
? 代码随想录: https://leetcode.cn/problems/all-paths-from-source-to-target/solution/by-carlsun-2-66pf/
* 题目说该图是一个「有向无环」图，因此从起始顶点开始，按照某条路径遍历下去『不可能』回到某个已经遍历过的节点，不用怕进入死循环。于是我们在遍历的时候并不需要记录已经遍历过的节点, 也就是不需要使用 visited 数组。
"""


class Solution:
    def allPathsSourceTarget(self, graph):
        # * 无论什么情况 curPath 一定是要包含 0 这个起始节点的, 这个节点不需要回溯
        curPath = [0]
        total = []
        targetNode = len(graph) - 1

        def backtracking(curNode, count):
            print(f"{'  ' * count} visiting {curNode}, path is {curPath}")
            # * 递归终止条件: 当到达了目标节点的时候存储当前路径到结果中
            if curNode == targetNode:
                total.append(curPath[:])
                return

            for connectNode in (graph[curNode]):
                # * 遍历到的节点加入到路径中来
                curPath.append(connectNode)
                # * 递归
                backtracking(connectNode, count + 1)
                print(f"{'  ' * count} backtracking from {connectNode}")
                # * 回溯，撤销本节点
                curPath.pop()

        backtracking(0, 0)
        return total


Solution().allPathsSourceTarget(graph=[[1, 2], [3], [3], []])
