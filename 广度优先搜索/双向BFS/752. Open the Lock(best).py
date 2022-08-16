""" 
> 双向 BFS 适用于 <起点> 和 <终点> 都知道的的情况下使用。
* 「双向 BFS」的基本实现思路如下:
* ➀ 创建「两个队列」分别用于两个方向的搜索；
* ➁ 持续使用 deadendsSet 用于解决「相同节点的重复搜索」以及记录绝对不允许到达的「一组死亡数字」
* ➂ 为了尽可能让两个搜索方向『平均』, 每次从队列中取值进行扩展时, 先判断哪个队列容量较少, 让容量较少的队列成为 beginQueue;
* ➃ 如果在搜索过程中搜索到「另一个队列搜索过的节点」, 说明找到了最短路径。
? https://leetcode.cn/problems/open-the-lock/solution/by-sunguodong-kl63/

* visited 与 deadends 可以整合的原因
* 两个集合存放的都是不可用的节点，判断方式（若当前节点在任一集合，则当前节点不可用）完全相同，因此可直接把两个集合合并为一个。

? https://leetcode.cn/problems/open-the-lock/solution/by-sunguodong-kl63/

"""


class Solution:
    def openLock(self, deadends, target):
        from collections import deque

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

        beginQueue = deque(["0000"])
        endQueue = deque([target])
        level = 0
        while beginQueue and endQueue:
            # * 选择一个容量更少的队列进行BFS搜索
            if len(beginQueue) > len(endQueue):
                beginQueue, endQueue = endQueue, beginQueue

            levelNodesNum = len(beginQueue)

            for _ in range(levelNodesNum):
                curStr = beginQueue.popleft()

                # * 将 curStr 变为 list 形式, 方便后续操作
                curStrArr = list(curStr)

                for charIdx in range(len(curStrArr)):
                    tmp = curStrArr[:]
                    # * 往上拧所得的新数, 比如1变成2
                    upChar = num_next(tmp[charIdx])
                    tmp[charIdx] = upChar
                    upStr = "".join(tmp)
                    if upStr in endQueue:
                        return level + 1
                    # * 如果对应的字符串不在 deadendsSet 中, 则将其加入队列
                    if upStr not in deadendsSet:
                        beginQueue.append(upStr)
                        deadendsSet.add(upStr)

                    tmp = curStrArr[:]
                    # * 往下拧所得的新数, 比如1变成2
                    downChar = num_prev(tmp[charIdx])
                    tmp[charIdx] = downChar
                    downStr = "".join(tmp)

                    # * 如果该字符串在另一个方向已经找到过, 说明两个方向在本字符串处汇集, 找到了最短路
                    if downStr in endQueue:
                        return level + 1
                    # * 如果字符转换后的字符串既不是dead字符串, 也没有被搜索过, 则将其加入队列
                    if downStr not in deadendsSet:
                        beginQueue.append(downStr)
                        deadendsSet.add(downStr)
            level += 1
        return -1
