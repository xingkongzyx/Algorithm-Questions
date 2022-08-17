""" 「」
* 对于该题目的思路, 主要有两个要满足的条件: 
* ➀ 是「连通图」或者说是这个图的「连通分量」等于1。若该图有两个或更多「连通分量」, 那么也不能构成树; 
* ➁ 不存在环. 
* 
* ➀ 「连通图」要满足的条件是: 以 BFS 或者 DFS 的方式遍历一遍图. 如果存在没有遍历到的节点, 那么就是「非连通图」, 返回 False.
* ➁ 存在环的判定: DFS 或者 BFS 遍历时, 把边给数一下. 因为数的时候, 得到的结果会是生成树所需的「最少的边数」. 为什么呢? 形成环的边会因为节点「被访问过」而不计算, 如下图: BFS 遍历时, 只会遍历 1,2 和 1,3 之间的边,  2,3 之间的边则不会被遍历, 所以最终数出来的边数 < 总边数, 则形成环. 总边数的计算方法就是 len(edges). 

*     1
*     |\
*     2-3

? https://leetcode.cn/problems/graph-valid-tree/solution/shen-du-you-xian-yan-du-you-xian-bing-cha-ji-de-zo/
* 对于 ➁ 的另一种理解也可以是: 对于一个 n 结点的图, 其边数一定是 n-1。如果边数大于 n-1, 那么一定存在环; 若边数小于 n-1, 那么一定有孤立的点, 也不能构成一棵树; 如果是按这么理解, 则「不需要定义 count 变量」, 而只需要在开头进行如下判断: 
/    if len(edges) != n - 1:
/        return False
? https://leetcode.cn/problems/graph-valid-tree/solution/c-zui-jian-dan-yi-dong-de-fang-fa-by-mapleking/
"""


class Solution:
    def validTree(self, n, edges):
        from collections import defaultdict, deque

        # * 构造邻接表
        graph = defaultdict(list)

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        # * 遍历邻接表, 从而判断是否满足上面的条件 ➀ && ➁
        queue = deque([0])
        visited = set()
        visited.add(0)
        count = 0
        while queue:
            curNode = queue.popleft()
            for neighbor in graph[curNode]:
                if neighbor not in visited:
                    count += 1
                    visited.add(neighbor)
                    queue.append(neighbor)

        # * 通过计算 visited set 中的元素个数是否等于 n 来判断是否是「连通图」。如果存在没有遍历到的节点, 也就是不等于 n, 说明不是「连通图」,
        # * 或者生成树所需的「最少的边数」小于题目给的边数, 说明存在环
        # * 两种情况存在任何一个则说明不是 valid tree
        if len(visited) != n or count < len(edges):
            return False

        return True
