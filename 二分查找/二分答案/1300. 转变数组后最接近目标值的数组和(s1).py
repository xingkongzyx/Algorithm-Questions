""" 
! 使用二分查找计算「第一个」使得转变后数组的和「大于等于」 target 的阈值 value
* 退出循环以后 left == right 成立, 这里的 left 表示使得转变后数组的和「大于等于」 target 的「第一个」阈值 threshold (也就是题目中说的value)。

* 对题目中说「接近」的考察, 有 3 种情况: 
* 情况 1: 「等于」是「最接近的」。
* 情况 2: 可以比 target 大一点点, 
* 情况 3: 也可以比 target 小一点点。

* 二分的思路是: 二分先找到「大于等于」 target 的时候的 value 的值. 这里对应「情况 1」和「情况 2」, 然后再将 left 为阈值的结果与 left - 1 为阈值的结果进行比较, 也就是考虑了「情况 3」, 综合下来, 就是题目要找的最小的 value 的值。
? https://leetcode.cn/problems/sum-of-mutated-array-closest-to-target/solution/er-fen-cha-zhao-by-liweiwei1419-2/
/ 时间复杂度: O(n* log k), k is the max value in arr, n is the num of elements in the array. binary search runs O(log k) times, linear sum is O(n), combined is O(n log k)
"""


class Solution(object):
    def findBestValue(self, arr, target):
        left, right = 1, max(arr)
        while left < right:
            mid = left + (right - left) // 2
            newSum = self.getNewSum(mid, arr)
            if newSum < target:
                left = mid + 1
            else:
                right = mid

        possibleResOne = abs(self.getNewSum(left - 1, arr) - target)
        possibleResTwo = abs(self.getNewSum(left, arr) - target)

        # # 因为题目中说『如果有多种使得和最接近 target 的方案, 请你返回这些整数中的最小值』, 所以等于的条件的时候返回 left - 1
        return left - 1 if possibleResOne <= possibleResTwo else left

    def getNewSum(self, value, arr):
        newSum = 0
        for num in arr:
            if num <= value:
                newSum += num
            else:
                newSum += value
        return newSum


print(Solution().findBestValue(
    arr=[60864, 25176, 27249, 21296, 20204], target=56803))
print(Solution().findBestValue(
    arr=[60864, 25176, 27249, 21296, 20204], target=56803))
