""" 
* 若无向图 G=(V,E) 的顶点集 V 可以分割为两个互不相交的子集, 且图中每条边的两个顶点分别属于不同的子集, 则称图 G 为一个二分图。

# From gpt: 
* 二分图(Bipartite Graph)是什么?
* 一个无向图如果能把所有顶点分成两组, 并且每条边都是跨组连接（组内没有边）, 就叫二分图。
! 换句话说, 用两种颜色（比如「红」「蓝」）给每个节点染色, 任意一条边的两个端点颜色都不相同。
* 比喻：想象学校里把学生分成「男生组」和「女生组」, 并且只允许异性朋友关系。如果某两位同学是朋友, 他们一定一个是男生一个是女生。问：给定一张朋友关系网, 能不能这样分组？能, 就对应「二分图」。
#? 对应的染色图: https://leetcode.cn/problems/is-graph-bipartite/solution/shou-hua-tu-jie-bfs-si-lu-by-hyj8/
* 我们使用图搜索算法从各个连通域的任一顶点开始遍历整个连通域, 遍历的过程中用两种不同的颜色对顶点进行染色, 相邻顶点染成相反的颜色。这个过程中倘若发现相邻的顶点被染成了相同的颜色, 说明它不是二分图；反之, 如果所有的连通域都染色成功, 说明它是二分图。

! 注意: 题目中给定的无向图不一定保证连通, 因此我们需要进行多次遍历, 直到每一个节点都被染色, 或确定答案为 false 为止。每次遍历开始时, 我们任选一个未被染色的节点, 将所有与该节点直接或间接相连的节点进行染色。

? https://leetcode.cn/problems/is-graph-bipartite/solution/bfs-dfs-bing-cha-ji-san-chong-fang-fa-pan-duan-er-/
/ 时间复杂度: O(n+m), 其中 n 和 m 分别是无向图中的点数和边数。 
/ 空间复杂度: O(n), 存储节点颜色的数组需要 O(n) 的空间, 并且在深度优先搜索的过程中, 栈的深度最大为 n, 需要 O(n) 的空间。 
? https://leetcode.cn/problems/is-graph-bipartite/solution/pan-duan-er-fen-tu-by-leetcode-solution/ 

?  非常好的注释代码: https://leetcode.cn/problems/is-graph-bipartite/solution/ran-se-fa-dai-ma-quan-zhu-shi-by-wen-jia-yaqg/
"""


class Solution:
    def isBipartite(self, graph):
        # * 定义 colors 数组, 初始值为 0 表示「未被访问」, 赋值为 1 或者 -1 表示两种不同的颜色。
        colors = [0 for _ in range(len(graph))]

        # * curColor 代表「当前节点 curNode」将要染的颜色
        def DFS(curNode, curColor):
            # * 递归终止条件: 当前节点「已被染色」, 更直白的说法是「已被访问」, 这时要立即返回避免「死循环」. 返回什么呢? 取决于当前节点『已有的颜色』是否与本次『要染的颜色』相同, 如果『已有的颜色』与本次『要染的颜色』不同, 说明此无向图无法被正确染色, 二分图不成立, 返回 false。
            if colors[curNode] != 0:
                if colors[curNode] != curColor:
                    return False
                return True

            # # 下面是本层递归的逻辑:
            # * 对「当前节点」进行染色
            colors[curNode] = curColor

            # * 调用递归函数将「当前节点」的所有邻接点染成相反的颜色(也就是 -curColor), 并在这过程中判断是否出现 「当前节点」与「邻接节点」染色『矛盾』的情况, 出现的话立即返回 false
            for neighborNode in graph[curNode]:
                neighborCheck = DFS(neighborNode, -curColor)
                if neighborCheck == False:
                    return False
            return True

        # # 因为图中可能含有多个连通域(例如 graph = [[], [2,3], [1,3], [1,2]] ), 为了防止有「孤立节点」, 应该遍历所有节点并将为染色的节点着色, 这过程中如果出现不成立则可以直接退出循环
        for node in range(len(graph)):
            if colors[node] == 0:
                check = DFS(node, 1)
                if check == False:
                    return False
        return True
