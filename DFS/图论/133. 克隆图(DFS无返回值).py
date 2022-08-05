"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#? https://leetcode.cn/problems/clone-graph/solution/133-ke-long-tu-by-chen-wei-f-2chn/
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        from collections import defaultdict

        if node == None:
            return None

        node_dict = defaultdict()
        #! 在这种dfs方法中,每次递归只负责创建传入node的clonedCopy,不负责返回它给它的上一层 
        def DFS(currentNode):
            #/ 拷贝节点
            clonedNode = Node(currentNode.val)
            #/ 节点值和新建节点以键值对存入visited
            node_dict[currentNode] = clonedNode
            #/ 递归遍历相邻节点, 如果邻居节点已经被created clone过,则将node_dict[neighborNode] 放在currentNode的邻接表中. 否则调用DFS(neighborNode) 创建clonedNode并将其加入node_dict中
            for neighborNode in currentNode.neighbors:
                if neighborNode not in node_dict:
                    DFS(neighborNode)
                clonedNode.neighbors.append(node_dict[neighborNode])
            return
        DFS(node)
        return node_dict[node]