""" 
* ➀ 第一步 穷举所有可能的密码组合
* 转一次锁, 锁上有 4 个位置, 每个位置可向「上」转, 也可向「下」转, 总共有 8 种可能;
* 例如：从 "0000" 开始, 转一次可穷举出"1000", "9000", "0100", "0900"...共 8 种密码, 再以这 8 种密码作为基础, 对每个密码再转一下, 穷举所有可能;
* 理解了这点后, 问题可抽象成一幅图, 每个节点有 8 个相邻的节点, 求最短距离。

* ➁ 第二步 解决重叠、死锁问题
* 1 会走回头路。从 "0000" 拨到 "1000", 从队列拿出 "1000" 后还会拨出一个 "0000" 进入死循环;
* 2 死亡密码不能出现,需跳过。
? 具体的图见 "开锁图示"
? https://leetcode.cn/problems/open-the-lock/solution/shou-hua-tu-jie-tu-bfs-lin-jie-guan-xi-7-ud8c/
* visited 与 deadends 可以整合的原因
* 两个集合存放的都是不可用的节点，判断方式（若当前节点在任一集合，则当前节点不可用）完全相同，因此可直接把两个集合合并为一个。

? https://leetcode.cn/problems/open-the-lock/solution/by-sunguodong-kl63/
"""


class Solution:
    def openLock(self, deadends, target):
        def num_prev(x):
            return "9" if x == "0" else str(int(x) - 1)

        def num_next(x):
            return "0" if x == "9" else str(int(x) + 1)

        start = '0000'
        deadendsSet = set(deadends)

        # * 处理特殊情况
        if start == target:
            return 0
        if start in deadendsSet:
            return -1
        deadendsSet.add(start)
        from collections import deque

        queue = deque(["0000"])
        level = 0
        while queue:
            # print("queue", queue)
            levelNodesNum = len(queue)
            for _ in range(levelNodesNum):
                curStr = queue.popleft()

                # * 如果出列的节点正好是目标节点, 则返回 level
                if curStr == target:
                    return level

                # * 将 curStr 变为 list 形式, 方便后续操作
                curStrArr = list(curStr)

                for charIdx in range(len(curStrArr)):
                    tmp = curStrArr[:]
                    # * 往上拧所得的新数, 比如1变成2
                    upChar = num_next(tmp[charIdx])
                    tmp[charIdx] = upChar
                    upStr = "".join(tmp)
                    # * 如果对应的字符串不在 deadendsSet 中, 则将其加入队列
                    if upStr not in deadendsSet:
                        queue.append(upStr)
                        deadendsSet.add(upStr)

                    tmp = curStrArr[:]
                    # * 往下拧所得的新数, 比如1变成2
                    downChar = num_prev(tmp[charIdx])
                    tmp[charIdx] = downChar
                    downStr = "".join(tmp)
                    # * 如果对应的字符串不在 deadendsSet 中, 则将其加入队列
                    if downStr not in deadendsSet:
                        queue.append(downStr)
                        deadendsSet.add(downStr)
            level += 1
        return -1


print(Solution().openLock(deadends=["0201", "0101",
                                    "0102", "1212", "2002"], target="0001"))
