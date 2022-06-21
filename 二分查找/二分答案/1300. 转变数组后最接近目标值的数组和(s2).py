class Solution(object):
    def findBestValue(self, arr, target):
        arr.sort()
        
        #! 使用二分查找计算最后一个使得转变后数组的和 小于等于 target 的阈值 value     
        left, right = 0, arr[-1]
        print(left, right)
        while left < right:
            mid = left + (right - left + 1) // 2
            newSum = self.getNewSum(mid, arr)
            if newSum > target:
                # 下一轮搜索区间 [left, mid - 1]
                right = mid - 1
            else:
                # 下一轮搜索区间 [mid, right]
                left = mid
        
        possibleResOne = abs(self.getNewSum(left, arr) - target)
        possibleResTwo = abs(self.getNewSum(left + 1, arr) - target)
        
        ## 因为题目中说 "如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。" 所以等于的条件的时候返回 left
        return left if possibleResOne <= possibleResTwo else (left + 1)
            
    def getNewSum(self, value, arr):
        newSum = 0
        for num in arr:
            if num <= value:
                newSum += num
            else:
                newSum += value
        return newSum


r = Solution().findBestValue([4,9,3], 10)
print(r)
