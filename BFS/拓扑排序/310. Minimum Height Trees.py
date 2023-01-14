""" 
# 与标准的「拓扑排序」代码不同的地方在于：这个问题是无向图。
#「拓扑排序」应用于有向无环图, 找到没有指向它的结点, 找的是「入度为 0」的结点; 当前这个问题, 因为是无向图, 找的是「叶子节点」, 同样用入度数组表示的话，就是找「入度为 1」的结点了
? https://leetcode.cn/problems/minimum-height-trees/solution/tan-xin-fa-gen-ju-tuo-bu-pai-xu-de-si-lu-python-da/

* The obvious method is to BFS for each node with the complexity of O(n^2) (and will get TLE).
* Here is one insight for this problem: the root of MHT is the middle point of the longest path in the tree; hence there are at most two MHT roots.
* How to find them? We can BFS from the bottom (leaves) to the top until the last level with <=2 nodes. To build the current level from the previous level, we can monitor the degree of each node. If the node has degree of one, it will be added to the current level. Since it only check the edges once, the complexity is O(n).

# 为什么在只剩下一个或者两个leaf node的时候就是答案
* 1) if you have 1 node "o" it doesn't have leaves (that single node has 0 degree), n won't change, so it's an infinite loop, but anyway it's a singular solution
* 2) if there are 2 nodes connected in a tree-like structure it must be: "o -- o" if you continue the algorithm on this it'll remove both nodes and you'll end up with an empty tree (n==0), so having 2 nodes is a solution.
* 3) for 3 or more nodes there must be leaf nodes which can be removed to eventually reach 1 or 2 nodes left.
? 讲解1: https://leetcode.com/problems/minimum-height-trees/discuss/1630778/C%2B%2B-Simple-Solution-or-Topological-Sort-or-W-Explanation
? 讲解2: https://leetcode.com/problems/minimum-height-trees/discuss/1631179/C%2B%2BPython-3-Simple-Solution-w-Explanation-or-Brute-Force-%2B-2x-DFS-%2B-Remove-Leaves-w-BFS
/ Time Complexity : O(N), iteration continues till n-2 nodes are deleted
/ Space Complexity : O(N), required for stroing G and leaves
"""


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque

        if n == 1:
            return [0]

        inDegree = [0 for _ in range(n)]
        map = defaultdict(list)

        for node1, node2 in edges:
            inDegree[node1] += 1
            inDegree[node2] += 1
            map[node1].append(node2)
            map[node2].append(node1)

        queue = deque([])

        for i in range(len(inDegree)):
            if inDegree[i] == 1:
                queue.append(i)

        # * keep doing leave nodes removal until total node count is smaller or equal to 2
        while n > 2:
            # * nodesNum 当前入度为1的节点数量
            leaveNodesNum = len(queue)
            # * 一次性将入度为一的点全部删去！！不能一个一个删！
            n -= leaveNodesNum
            for _ in range(leaveNodesNum):
                curLeafNode = queue.popleft()
                #  * 更新 curLeafNode 的邻接点对应的 inDegree：若 curLeafNode 临接点更新后的入度为1, 则将其放入 queue 中。
                for nxtNode in map[curLeafNode]:
                    inDegree[nxtNode] -= 1
                    if inDegree[nxtNode] == 1:
                        queue.append(nxtNode)

        return list(queue)
