""" 「」
* 题目中给定 n 个城市, 一些彼此相连, 一些没有相连。其中有个「省份」的概念, 由一组直接或间接相连的城市组成, 组内不存在其他没有相连的城市。现在题目要求「省份」的数量
* 在这里, 我们可以将城市之间的相连关系看成是图, 矩阵 isConnected 是图的「邻接矩阵」, 城市是图的节点, 相连关系是图中相连的边, 而要求的省份即是图中的「连通分量」, 那么问题就变成求图中「连通分量」的数量。
? 连通分量概念: https://blog.csdn.net/yjw123456/article/details/90449189

* ① 先声明变量 visited 用以标记城市是否被遍历访问过；
* ② 遍历所有的城市, 若遍历的城市未被访问, 那么以此开始深度优先搜索, 同时进行标记, 直到同一个连通分量中的点都被访问, 那表示存在一个省份。
* ③ 若此时还有其他城市未被访问, 那么表示有新的连通分量, 用 count 存储。继续搜索, 直到所有的城市都被访问。最终返回 count。
? 上述思路参考: https://leetcode.cn/problems/number-of-provinces/solution/547-sheng-fen-shu-liang-dfs-bfs-bing-cha-399n/
? 代码参考: https://leetcode.cn/problems/number-of-provinces/solution/dfs-bfs-bing-cha-ji-3-chong-fang-fa-ji-s-edkl/
/ 时间复杂度: O(n^2) 其中 n 是城市的数量。需要遍历矩阵 n 中的每个元素。
/ 空间复杂度: O(n) 其中 n 是城市的数量。需要使用数组 visited 记录每个城市是否被访问过, 数组长度是 n, 递归调用栈的深度不会超过 n。

"""


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        #! 重要细节: dfs中没有显式写递归终止条件, 但是调用 dfs(i) 时, 只有当 i 不在 visited 中, 才能进行DFS, 防止死循环
        def dfs(cityIdx):
            # * 对当前的城市标记为已访问
            visited[cityIdx] = True

            # * 对于 cityIdx 代表的城市相邻的所有城市进行DFS, 在DFS之前要确定那个城市没有被访问过, 否则会陷入「死循环」
            for i in range(len(isConnected[cityIdx])):
                if visited[i] == False and isConnected[cityIdx][i] == 1:
                    dfs(i)

        # * 定义 boolean 数组标识城市是否被访问
        visited = [False for _ in isConnected]

        # * 定义 count 来累计遍历过的「连通分量」的数量, 也就是省份的数量
        count = 0

        for i in range(len(isConnected)):
            # * 若当前城市 i 未被访问，说明又是一个新的「连通分量」，则遍历新的「连通分量」且 count += 1
            if visited[i] == False:
                count += 1
                dfs(i)

        return count
