""" 
! 这个题跟 547 比较类似, 可以看做图的连通性问题。

* 此题思路:, 将各个邮箱组成为一个无向图, 将相同的邮箱合并在一起, 构成了多了连通分量。每个连通分量对应着一个独立的账号。
* 如何保存邮箱 email 之间的联系? 对于每一个输入条目, 第一个邮箱和其后的邮箱相连, 而其后的邮箱仅与第一个邮箱关联, 也就是从无向图变成了有向图。accounts[i][1] 对应的条目有很多, 但 accounts[i][j] (j > 1) 对应的条目仅有 accounts[i][1]。这样减少了代码的复杂度, 降低了对数组的插入次数。


? 代码: https://leetcode.cn/problems/accounts-merge/solution/python-bing-cha-ji-dfs-liang-chong-jie-f-tjzd/
? https://leetcode.cn/problems/accounts-merge/solution/dui-yu-mei-yi-ge-zhang-hu-jin-xing-dfsyi-mldd/
? https://leetcode.cn/problems/accounts-merge/solution/chao-qing-xi-si-lu-jian-tu-bian-li-bfs-o-2kde/
? https://leetcode.cn/problems/accounts-merge/solution/tu-bian-li-dfsjie-fa-by-vin-cent-ap2i/
"""
from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 构建无向图, 每个邮箱为一个节点, 同一个账户的邮箱全部相连
        # 有多少连通分量, 就有多少独立的账户
        # 该字典, 键为一个邮箱, 值为与其相连的所有邮箱
        graph = defaultdict(list)
        for account in accounts:
            master = account[1]
            for email in list(set(account[2:])):
                graph[master].append(email)
                graph[email].append(master)
        print(graph)
        res = []  # 最终的输出结果
        visited = set()  # 标记集合

        # 对每一个 account 子数组的第一个邮箱进行深度优先搜索, 子数组的姓名+得到的账户组（也要再排个序） 就是这个人对应的答案
        for account in accounts:
            emails = []  # 存储该账户的所有邮箱
            # 深度优先遍历
            self.dfs(account[1], graph, visited, emails)
            if emails:
                res.append([account[0]] + sorted(emails))
        return res

    # 深度优先遍历
    def dfs(self, email, graph, visited, emails):
        # 访问过, 不在添加直接结束
        if email in visited:
            return
        visited.add(email)  # 标记访问
        emails.append(email)  # 添加
        for neighbor in graph[email]:
            self.dfs(neighbor, graph, visited, emails)


accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com",
                                                                      "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]

Solution().accountsMerge(accounts)
