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
            #! 注意在BFS中每次我们是为这个popped出来的 currentNode 构建它的neighbors，如果这个neighbor没有cloned(也就是没有放入cloned_dict中)，就创造这个node，放入dict，然后放到 clonedCurrentNode的 neighbors list中。但是我们 currentNode 本身不需要在这个循环中创建 cloned，因为所有cloned node的创建一是在 while loop 外面初始化时创建了，二是在构建neighbors时创建各个neighbor的clone，只不过这个clonedNeighbor node的neighbors property为空，需要在遍历过程中加入
            currentNode = queue.popleft()
            clonedCurrentNode = cloned_dict[currentNode]

            for neighbor in currentNode.neighbors:
                #* 如果neighbor已经被创建(已经放在了dict中)，则直接提取它. 否则在此进行 clonedNeighbor 的构造，并将其加入queue中。此时新创造的 clonedNeighbor 它本身的 neighbors 是 []. 我们通过加入queue然后在BFS 遍历到它时构造它的neighbors list
                if neighbor in cloned_dict:
                    clonedNeighbor = cloned_dict[neighbor]
                else:
                    clonedNeighbor = Node(neighbor.val)
                    cloned_dict[neighbor] = clonedNeighbor
                    queue.append(neighbor)
                clonedCurrentNode.neighbors.append(clonedNeighbor)
        return clonedNode