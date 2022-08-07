class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


""" 
/ 1. 递归参数和返回值: 传入当前要进行clone的start node, 返回的则是最开始传入的start node的cloned node. 也就是题目中的"将「给定节点的拷贝」作为对克隆图的引用返回"。
/ 2. 递归终止条件: 当目前要访问的 currentNode 已经被记录在 graphDict 中, 直接返回它的 cloned node
/ 3. 本层递归: 首先创建 currentNode 的 cloned node, 然后将原node与cloned node加入 dict. 然后继续递归, 对 currentNode 的 neighbors 同样 create cloned copy. 并把每个 neighbor 的拷贝加入 clonedNode.neighbors 列表


* 如果不使用 hashmap 可能陷入死循环。这是由于无向图里面 A⇆B, A的邻接表会有B, B的邻接表也会有A, 如果不能把已经走过的节点记录下来就会陷入「死循环」. 所以使用一个 hashmap 存放已经走过的节点，每次进行深拷贝之前先判断是否已经拷贝过了，如果是则直接用他，如果不是再进行接下来的深拷贝操作。
? 官方讲解非常好: https://leetcode.cn/problems/clone-graph/solution/ke-long-tu-by-leetcode-solution/
? https://leetcode.cn/problems/clone-graph/solution/ke-long-tu-ha-xi-dfs-zui-qing-xi-yi-dong-3v6l/
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None

        # * 这个dictionary的key是原node, val是原node的cloned copy
        cloned_dict = {}

        def DFS(currentNode):
            # * 终止条件: 如果这个node已经被创建过了, 返回它的cloned copy
            if currentNode in cloned_dict:
                return cloned_dict[currentNode]

            # * 本层递归: 创建currentNode的clone copy并将其加入cloned_dict 中
            clonedNode = Node(currentNode.val)
            cloned_dict[currentNode] = clonedNode

            # * 对于 currentNode 的每个neighbor, 创建它的copy, 然后把 clonedNeighbor 放到 clonedNode的neighbors list中
            for neighbor in currentNode.neighbors:
                clonedNeighbor = DFS(neighbor)
                clonedNode.neighbors.append(clonedNeighbor)
            return clonedNode

        return DFS(node)


# if __name__ == '__main__':
#     S = Solution()
#     ns = [Node(i, []) for i in range(0, 5)]
#     ns[1].neighbors = [ns[2], ns[4]]
#     ns[2].neighbors = [ns[1], ns[3]]
#     ns[3].neighbors = [ns[2], ns[4]]
#     ns[4].neighbors = [ns[3], ns[1]]

#     res = S.cloneGraph(ns[1])
