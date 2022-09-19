""" 
* 建图统计入度和出度。名人的入度为 n - 1, 出度为 0.
* https://leetcode.cn/problems/find-the-celebrity/solution/by-jmzh119yjm-lrm7/
"""


class Solution:
    def findCelebrity(self, n: int) -> int:
        inDegree = [0 for _ in range(n)]
        outDegree = [0 for _ in range(n)]
        for p1 in range(n):
            for p2 in range(n):
                if p1 != p2 and knows(p1, p2):
                    # * 如果 p1 知道 p2, 则 p2 的入度 + 1(因为有人知道他), p1 的出度 +1(因为他知道别人)
                    inDegree[p2] += 1
                    outDegree[p1] += 1

        # * 同时遍历 inDegree 和 outDegree 数组, 只有某个人的入度为 n - 1且出度为 0时这个人才会是名人
        for p in range(n):
            if inDegree[p] == n - 1 and outDegree[p] == 0:
                return p

        return -1
