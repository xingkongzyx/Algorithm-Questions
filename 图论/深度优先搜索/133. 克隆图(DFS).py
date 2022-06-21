class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

 # DFS，深拷贝，所有的节点都要新建一遍，然后重建它们之间的关系
""" 
/ 1. 递归参数和返回值: 传入当前要进行clone的start node，返回的则是最开始传入的start node的clone. 也就是题目中的 将 给定节点的拷贝 作为对克隆图的引用返回。
/ 2. 递归终止条件：当目前要访问的node已经被记录在 graphDict 中
/ 3. 本层递归: 首先创建这个node的cloned copy, 然后使用dfs函数对这个node的neighbors 同样 create cloned copy. 并把每个 neighbor 最后 clone 的引用返回并赋值给 createdNode.neighbors

https://leetcode.cn/problems/clone-graph/solution/ke-long-tu-ha-xi-dfs-zui-qing-xi-yi-dong-3v6l/
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None
            
        #* 这个dictionary的key是原node, val是原node的cloned copy
        cloned_dict = {}
        def DFS(currentNode):
            #* 终止条件: 如果这个node已经被创建过了，返回它的cloned copy
            if currentNode in cloned_dict:
                return cloned_dict[currentNode]

            #* 本层递归: 创建currentNode的clone copy并将其加入cloned_dict 中
            clonedNode = Node(currentNode.val)
            cloned_dict[currentNode] = clonedNode

            #* 对于 currentNode 的每个neighbor, 创建它的copy，然后把 clonedNeighbor 放到 clonedNode的neighbors list中
            for neightbor in currentNode.neighbors:
                clonedNeighbor = DFS(neightbor)
                clonedNode.neighbors.append(clonedNeighbor)
            return clonedNode
        
        return DFS(node)

if __name__ == '__main__':
    S = Solution()
    ns = [Node(i, []) for i in range(0, 5)]
    ns[1].neighbors = [ns[2], ns[4]]
    ns[2].neighbors = [ns[1], ns[3]]
    ns[3].neighbors = [ns[2], ns[4]]
    ns[4].neighbors = [ns[3], ns[1]]

    res = S.cloneGraph(ns[1])