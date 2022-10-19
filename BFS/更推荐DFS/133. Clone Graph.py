""" 
? https://leetcode.cn/problems/clone-graph/solution/ke-long-tu-by-leetcode-solution/
"""


class Solution(object):
    from collections import deque

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None

        cloned_dict = {}
        clonedNode = Node(node.val)
        cloned_dict[node] = clonedNode
        queue = deque([node])

        while len(queue) > 0:
            # # 注意在 BFS 中每次循环的任务是为 queue 中的「头元素」的「cloned元素」构建 neighbors, 如果「当前neighbor」没有被「深拷贝」(也就是没有放入 cloned_dict 中), 就创造「当前neighbor」的「cloned版本」, 并放入 cloned_dict, 然后放入「头元素」的「cloned元素」的 neighbors 中。
            # # 但是「头元素」本身不需要在这个循环中创建自己的「cloned版本」, 因为所有元素的「cloned版本」的创建 1)是在 while loop 外面初始化时创建了 2)是在构建neighbors 时创建各个 neighbor 的 clone, 只不过这个 clonedNeighbor node的neighbors property为空, 需要在遍历过程中加入
            currentNode = queue.popleft()
            clonedCurrentNode = cloned_dict[currentNode]

            for neighbor in currentNode.neighbors:
                # * 如果neighbor已经被创建(已经放在了dict中), 则直接提取它. 否则在此进行 clonedNeighbor 的构造, 并将其加入queue中。此时新创造的 clonedNeighbor 它本身的 neighbors 是 []. 我们通过加入queue然后在BFS 遍历到它时构造它的neighbors list
                if neighbor in cloned_dict:
                    clonedNeighbor = cloned_dict[neighbor]
                else:
                    clonedNeighbor = Node(neighbor.val)
                    cloned_dict[neighbor] = clonedNeighbor
                    #! 每个节点只有在刚克隆好的时候才会入队且只入队一次
                    queue.append(neighbor)
                clonedCurrentNode.neighbors.append(clonedNeighbor)
        return clonedNode
