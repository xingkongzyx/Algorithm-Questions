""" 
/ 时间复杂度 : O(nlogn) 。时间复杂度由排序决定。一旦排序完成，只需要 O(n) 的时间来判断交叠。
/ 空间复杂度 : O(1)。没有使用额外空间。
? https://leetcode.cn/problems/meeting-rooms/solution/hui-yi-shi-by-leetcode/

"""

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        # print(intervals)

        for i in range(1, len(intervals)):
            cur = intervals[i]
            pre = intervals[i - 1]
            if cur[0] < pre[1]:
                return False

        return True
