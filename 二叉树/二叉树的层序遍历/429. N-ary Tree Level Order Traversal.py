"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root):
        if root == None:
            return []

        queue = collections.deque([root])
        res = []
        while queue:
            queue_len = len(queue)
            level_nodes = []
            for _ in range(queue_len):
                cur_node = queue.popleft()
                level_nodes.append(cur_node.val)

                for child in cur_node.children:
                    queue.append(child)
                    
            res.append(level_nodes)
        return res

