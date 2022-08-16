"""
# 将 sequences 中的所有序列看成「有向图」, 数字 1 到 n 分别表示图中的 n 个结点, 每个序列中的相邻数字表示的结点之间存在一条有向边。根据给定的序列构造「超序列」等价于有向图的拓扑排序。

* 每一轮拓扑排序时, 队列中的元素个数表示可以作为「超序列」下一个数字的元素个数, 根据队列中的元素个数, 执行如下操作。
*   ⛦ 如果队列中的元素个数大于 1, 则「超序列」的下一个数字不唯一, 因此 nums 不是唯一的最短「超序列」, 返回 False。
*   ⛦ 如果队列中的元素个数等于 1, 则「超序列」的下一个数字是队列中唯一的数字。将该数字从队列中取出, 将该数字指向的每个数字的入度减 1, 并将入度变成 0 的数字添加到队列中。

! 关键是得能想到 怎么才能确定『唯一』『最短』「超序列」？
! 那就是得从队列中一个一个的出来, 但凡有两种选择, 就不是『唯一』『最短』「超序列」了
! 这个就符合拓扑排序的思想, 也就能想到这个算法了

? https://leetcode.cn/problems/sequence-reconstruction/solution/xu-lie-zhong-jian-by-leetcode-solution-x337/
? https://leetcode.cn/problems/sequence-reconstruction/solution/by-sing_for_the_moment-helm/ 
"""


class Solution:
    def sequenceReconstruction(self, nums, sequences):
        from collections import defaultdict, deque
        inDegree = [0 for _ in range(len(nums) + 1)]
        map = defaultdict(list)
        for seq in sequences:
            for i in range(len(seq) - 1):
                pre = seq[i]
                nxt = seq[i + 1]
                inDegree[nxt] += 1
                map[pre].append(nxt)

        queue = deque([])
        for j in range(1, len(inDegree)):
            if inDegree[j] == 0:
                queue.append(j)

        while queue:
            # print("current queue:", queue)
            numNodesInQueue = len(queue)

            # * 「序列唯一」等价于拓扑排序的过程中。任何时刻队列里面不能同时存在两个点。
            # # 因为如果「同层」存在并列点, 意味着他两是可以换位置的。也就意味着有多种排序。(所以像 210 的拓扑排序, 得到的结果也就是所上课程的顺序是不具有唯一性的)
            if numNodesInQueue > 1:
                return False

            currentNum = queue.popleft()
            nxtNums = map[currentNum]
            for num in nxtNums:
                inDegree[num] -= 1
                if inDegree[num] == 0:
                    queue.append(num)

        return True
