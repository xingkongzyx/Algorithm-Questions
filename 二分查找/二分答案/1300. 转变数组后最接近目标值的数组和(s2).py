""" 
! 使用二分查找计算「最后一个」使得转变后数组的和「小于等于」target 的阈值 value. 那么目标值可能在 value 也可能在 value + 1。
? https://leetcode.cn/problems/sum-of-mutated-array-closest-to-target/solution/er-fen-cha-zhao-by-liweiwei1419-2/
/ 时间复杂度: O(n* log k), k is the max value in arr, n is the num of elements in the array. binary search runs O(log k) times, linear sum is O(n), combined is O(n log k)
"""


class Solution(object):
    def findBestValue(self, arr, target):
        arr.sort()

        left, right = 0, arr[-1]
        print(left, right)
        while left < right:
            mid = left + (right - left + 1) // 2
            newSum = self.getNewSum(mid, arr)
            # * 因为找的是「小于等于」target 的阈值, 所以大于就是一定不满足条件的情况
            if newSum > target:
                # * 下一轮搜索区间 [left, mid - 1]
                right = mid - 1
            else:
                # * 下一轮搜索区间 [mid, right]
                left = mid

        possibleResOne = abs(self.getNewSum(left, arr) - target)
        possibleResTwo = abs(self.getNewSum(left + 1, arr) - target)

        # # 因为题目中说『如果有多种使得和最接近 target 的方案, 请你返回这些整数中的最小值』, 所以等于的条件的时候返回 left - 1
        return left if possibleResOne <= possibleResTwo else (left + 1)

    def getNewSum(self, value, arr):
        newSum = 0
        for num in arr:
            if num <= value:
                newSum += num
            else:
                newSum += value
        return newSum


r = Solution().findBestValue([4, 9, 3], 10)
print(r)
