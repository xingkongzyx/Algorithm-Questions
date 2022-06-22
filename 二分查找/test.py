class Solution:
    def findRightInterval(self, intervals):

        record = {}
        result = [0 for _ in intervals]
        for i in range(len(intervals)):
            startIdx = intervals[i][0]
            record[startIdx] = i
        # print(result)
        intervals.sort(key=lambda item: item[0])
        # print("intervals are", intervals)
        # print("record is ", record)

        for i in range(len(intervals)):
            current = intervals[i]
            currentStartIdx, currentEndIdx = current[0], current[1]

            res = self.findInterval(currentEndIdx, intervals)
            # print(f"first startval >= {currentEndIdx} is {res}, , 原来的interval是 {record[currentStartIdx]} \n")
            if res == '@':
                result[record[currentStartIdx]] = -1
            else:
                result[record[currentStartIdx]] = record[res]
            print(result)
        return result


    def findInterval(self, target, intervals):
        left = 0
        right = len(intervals) - 1
        
        while left < right:
            mid = (left + right) // 2
            # print(intervals[left], intervals[mid], intervals[right])
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid
        # print(f"bs result is ", intervals[left][0])        
        if intervals[left][0] < target:
            return '@'
        else:
            return intervals[left][0]


print(Solution().findRightInterval(intervals = [[-3,-1],[-2,0],[-1,1],[0,2],[1,3],[2,4]]))
