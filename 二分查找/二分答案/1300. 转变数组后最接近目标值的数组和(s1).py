""" 
? https://leetcode.cn/problems/sum-of-mutated-array-closest-to-target/solution/er-fen-cha-zhao-by-liweiwei1419-2/
* 退出循环以后 left == right 成立，这里的 left 表示使得转变后数组的和大于等于 target 的最小的阈值 threshold(也就是题目中说的value)。
* 
* 对题目中说「接近」的考察，有 3 种情况：
* 情况 1：等于是「最接近」。
* 情况 2：可以比 target 大一点点，
* 情况 3：也可以比 target 小一点点。
* 代码的思路是：二分先找到大于等于 target 的时候的 value 的值（情况 1 和情况 2），然后再比较 left - 1 ，也就是考虑了 情况 3 ，综合下来，就是题目要找的最小的 value 的值。
"""
class Solution(object):
    def findBestValue(self, arr, target):
        arr.sort()
        
        #! 使用二分查找计算第 1 个使得转变后数组的和大于等于 target 的阈值 value     
        left, right = 0, arr[-1]
        print(left, right)
        while left < right:
            mid = left + (right - left) // 2
            newSum = self.getNewSum(mid, arr)
            if newSum < target:
                # 下一轮搜索区间 [mid + 1, right]
                left = mid + 1
            else:
                right = mid
        
        possibleResOne = abs(self.getNewSum(left, arr) - target)
        possibleResTwo = abs(self.getNewSum(left - 1, arr) - target)
        
        return left if possibleResOne < possibleResTwo else (left - 1)
            
    def getNewSum(self, value, arr):
        newSum = 0
        for num in arr:
            if num <= value:
                newSum += num
            else:
                newSum += value
        return newSum

print(Solution().findBestValue(arr = [60864,25176,27249,21296,20204], target = 56803))
