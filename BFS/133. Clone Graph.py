""" 
! 无论邻居节点是否已克隆过, 都要在“当前克隆节点”的邻居列表里加上它的克隆版本。
场景：小明有三个朋友：小红和小华；小红和小华也互为朋友。
你想为“仓库”里的三个人做一份“社交注册表”——每个人的好友都要记录下来。
错误做法：
你先登记小明, 告诉他“小红”和“小华”是他的朋友。
后来去找小红, 看到“已在仓库”就跳过, 不再告诉小红“小明”也要是她的朋友。
同理, 小华也没再被告知“小红”或“小明”是她的朋友。

结果：
“小明 → 小红、小华” 在表里有
但“小红 → 小明、小华” 和 “小华 → 小明、小红” 都空空如也！

正确做法：
无论这个人是不是“已登记”, 每次有人说他是你朋友, 你都要再帮他登记一次。
这样不仅小明知道小红、小华, 小红也知道小明、小华, 小华也知道小明、小红。


# 已克隆过的节点, 只是不需要再 new 一个新实例, 也不需要再入队；但它的引用要被重复用来构建所有边。
! 什么时候要像「克隆图」那样 “即使 visited 也要做额外操作”？
 - 图的克隆要保留所有边, 所以即便节点被访问过, 你也还得在克隆节点之间再加一次边。
 - 普通的网格 BFS只是路径搜索或连通性判断, 没有“保留边”这一需求, 
 - 只要保证每个格子“处理”且“入队”一次, 就不会丢信息, 也不会无限循环。

! 在 2D 矩阵(grid)上做 BFS 时为什么这种 "见过就跳过" 是对的？
 - 网格没有要“克隆”节点、也不用建立额外的“边”结构, 
 - 你需要的只是遍历／扩散, 每个格子只要被访问一次就行了。
 - 所以当 visited[nr][nc] 为 true 时, 你完全可以 continue, 跳过这个邻居。



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
#               // ——无论是否第一次见到, 都要做这一步！——
#               // 在 cloned(curNode) 的邻居里, 加入 cloned(neighbor)
                clonedCurrentNode.neighbors.append(clonedNeighbor)
        return clonedNode
