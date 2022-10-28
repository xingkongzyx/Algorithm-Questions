""" 
The obvious method is to BFS for each node with the complexity of O(n^2) (and will get TLE).

Here is one insight for this problem: the root of MHT is the middle point of the longest path in the tree; hence there are at most two MHT roots.

How to find them? We can BFS from the bottom (leaves) to the top until the last level with <=2 nodes. To build the current level from the previous level, we can monitor the degree of each node. If the node has degree of one, it will be added to the current level. Since it only check the edges once, the complexity is O(n).
? https://leetcode.com/problems/minimum-height-trees/discuss/1631179/C%2B%2BPython-3-Simple-Solution-w-Explanation-or-Brute-Force-%2B-2x-DFS-%2B-Remove-Leaves-w-BFS
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
            n -= leaveNodesNum
            for _ in range(leaveNodesNum):
                curLeafNode = queue.popleft()
                for nxtNode in map[curLeafNode]:
                    inDegree[nxtNode] -= 1
                    if inDegree[nxtNode] == 1:
                        queue.append(nxtNode)

        return list(queue)
