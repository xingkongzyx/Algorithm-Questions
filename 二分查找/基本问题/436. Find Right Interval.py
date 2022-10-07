
""" 
* 题目翻译: 对于每一个区间 i, 寻找它的右区间就是找到另一个区间 j(j区间可以与i区间是同一个区间), j 区间的 startVal 大于等于 i 区间的 endVal
/ 时间复杂度: O(nlogn), 其中 n 为区间数组的长度。排序的时间为 O(nlogn), 每次进行二分查找花费的时间为O(logn), 一共需要进行 n 次二分查找, 因此总的时间复杂度为 O(nlogn)。
/ 空间复杂度: O(n), 其中 n 为区间数组的长度。

"""


class Solution(object):
    def findRightInterval(self, intervals):
        if len(intervals) == 1:
            return [-1]

        from collections import defaultdict
        record = defaultdict()
        # * hashmap中储存的是每个区间的 startVal 以及这个区间在 intervals 数组中的 index
        for i in range(len(intervals)):
            record[intervals[i][0]] = i

        intervals.sort(key=lambda item: item[0])
        # * 使用二分搜索找出大于当前区间的右区间
        result = [-1 for _ in intervals]

        for i in range(len(intervals)):
            currentInterval = intervals[i]
            startVal = currentInterval[0]
            endVal = currentInterval[1]

            # * 寻找对于 current interval 来说的右区间
            currentRes = self.getRightInterval(i, endVal, intervals, record)
            if currentRes == -1:
                continue
            else:
                result[record[startVal]] = currentRes

        return result

    # 找出第一个大于等于target的interval index
    def getRightInterval(self, leftBound, target, intervals, record):
        left = leftBound
        right = len(intervals) - 1

        while left < right:
            mid = left + (right - left) // 2
            # * 使用排除法, 一定不满足条件的是 mid 代表的interval的 start value < target
            if intervals[mid][0] < target:
                # * 下一轮搜索区间是[mid + 1, right]
                left = mid + 1
            else:
                # * 下一轮搜索区间是[left, mid]
                right = mid

        #! 最后有可能是搜不到对应interval的, 返回 -1
        if intervals[left][0] < target:
            return -1
        resultVal = record[intervals[left][0]]
        return resultVal


Solution().findRightInterval(intervals=[[1, 1], [3, 4]])
