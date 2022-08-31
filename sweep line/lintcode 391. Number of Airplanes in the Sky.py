"""
> 这题与 253 一模一样
? https://www.lintcode.com/problem/391/description
"""


class Solution:
    """
    @param airplanes: an array of meeting time airplanes
    @return: the minimum number of conference rooms required
    """

    def countOfAirplanes(self, airplanes):
        # Write your code here
        room = []
        # 加入开始时间和结束时间，1是房间+1，-1是房间-1
        for i in airplanes:
            room.append((i.start, 1))
            room.append((i.end, -1))
        tmp = 0
        ans = 0
        # 排序
        room = sorted(room)
        # 扫描一遍
        for idx, cost in room:
            tmp += cost
            ans = max(ans, tmp)
        return ans
