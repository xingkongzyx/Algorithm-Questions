""" 
先构造一个连通图，每一个节点，作为key，value是节点的相邻节点列表
图建好之后，用 BFS 去遍历
过程中需要一个 visited 集合去存已经遍历过的节点，避免重复算

作者：niconiconi-12
链接：https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree/solution/chi-xiao-dou-python-bfs-hashmap-dai-ma-j-d3kl/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""



class Solution(object):
    def distanceK(self, root, target, k):
        self.graph = {}
        
        def buildGraph(currentNode):
            if currentNode.left == None and currentNode.right == None:
                if currentNode.val not in self.graph:
                    self.graph[currentNode.val] = []

            
            if currentNode.left:
                if currentNode.val not in self.graph:
                    self.graph[currentNode.val] = []
                self.graph[currentNode.val].append(currentNode.left.val)
                self.graph[currentNode.left.val] = []
                self.graph[currentNode.left.val].append(currentNode.val)
                buildGraph(currentNode.left)
            
            if currentNode.right:
                if currentNode.val not in self.graph:
                    self.graph[currentNode.val] = []
                self.graph[currentNode.val].append(currentNode.right.val)
                self.graph[currentNode.right.val] = []
                self.graph[currentNode.right.val].append(currentNode.val)
                buildGraph(currentNode.right)
        buildGraph(root)

        def findNodes(target, k):
            from collections import deque
            queue = deque([target.val])
            visited = set()
            counter = 0
            result = []

            while queue:
                queue_len = len(queue)
                
                if counter == k:
                    for idx in range(queue_len):
                        currentVal = queue.popleft()
                        if currentVal not in visited:
                            result.append(currentVal)
                    return result

                for _ in range(queue_len):
                    currentVal = queue.popleft()
                    if currentVal not in visited:
                        visited.add(currentVal)
                        if self.graph[currentVal]:
                            queue.extend(self.graph[currentVal][:])

                counter += 1

            return result

        return findNodes(target, k)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(3)
lnode1 = TreeNode(5)
lnode2 = TreeNode(6)
lnode3 = TreeNode(2)
lnode4 = TreeNode(7)
lnode5 = TreeNode(4)

rnode1 = TreeNode(1)
rnode2 = TreeNode(0)
rnode3 = TreeNode(8)

root.left = lnode1
lnode1.left = lnode2
lnode1.right= lnode3
lnode3.left = lnode4
lnode3.right = lnode5

root.right = rnode1
rnode1.left = rnode2
rnode1.right = rnode3
# root = TreeNode(1)
s =  Solution()
res = s.distanceK(root, lnode1, 2)
print(res)