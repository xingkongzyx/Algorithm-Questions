
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # [1,2] [2,3] [3,4] 求得是第一个 大于等于 current interval 的 endIdx 的interval所在的下标
        from collections import defaultdict
        length = len(intervals)
        
        record = defaultdict()
        for i in range(length):
            record[intervals[i][0]] = i
        # print(record)
        intervals.sort(key = lambda item: item[0])
        # print(intervals)
        result = [-1 for _ in range(length)]
        for i in range(length):
            currentInterVal = intervals[i]
            start, end = currentInterVal[0], currentInterVal[1]
            
            left = i
            right = length - 1
            
            while left < right:
                mid = left + (right - left) // 2
                if intervals[mid][0] < end:
                    # 下一轮搜索区间 [mid + 1, right]
                    left = mid + 1
                else:
                    # 下一轮搜索区间 [left, mid]
                    right = mid
                    
            if intervals[left][0] < end:
                continue
            else:
                foundStart = intervals[left][0]
                # print(f"for current {currentInterVal}, found start {foundStart}")
                result[record[start]] = record[foundStart]
        # print(result)     

print(Solution().findRightInterval(intervals = [[1,4],[2,3],[3,4]]))
