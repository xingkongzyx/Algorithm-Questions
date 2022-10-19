# O(v + e) time | O(v) space
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        if not self.name:
            return array
        queue = [self]
        while len(queue) > 0:
            poppedNode = queue.pop(0)
            array.append(poppedNode.name)
            for child in poppedNode.children:
                queue.append(child)
        return array
