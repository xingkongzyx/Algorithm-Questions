
# ? https://leetcode.cn/problems/valid-triangle-number/solution/er-fen-cha-zhao-python-dai-ma-java-dai-ma-by-liwei/
# / 时间复杂度：O(n²*logn), 其中 n 是数组 nums 的长度。我们需要 O(n*logn) 的时间对数组 nums 进行排序, 随后需要 O(n²*logn) 的时间使用二重循环枚举 a, b 的下标以及使用二分查找得到 c 的下标范围。
# / 空间复杂度：O(logn), 即为排序需要的栈空间。

class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        numsLen = len(nums)
        count = 0
        for i in range(0, numsLen - 2):
            sideOne = nums[i]
            for j in range(i + 1, numsLen - 1):
                sideTwo = nums[j]

                sum = sideOne + sideTwo
                # * 因为构成三角形的条件是两边之和大于第三边, 所以要找到严格小于第三边的元素的个数, 反过来说就是找出数组中 [j+1, numsLen-1] 中大于等于两边之和的元素个数, 然后进行减法。
                # ! 找出大于等于 "两边之和 sum" 的元素个数也就是要找出数组剩余部分中「第一个」「大于等于 sum」的下标 idx。然后 (idx-(j+1)) 就是符合要求的第三边的个数

                left = j + 1
                # * 初始化的时候 left = j + 1, right = len, right 这样初始化的原因是区间 [j + 1..numsLen - 1] 里所有的元素都可以与 nums[i]、nums[j] 构成三角形；那么通过下面的二分搜索代码找到的「第一个」大于等于 sum 的元素的下标就是 numsLen, 这样才能计算出正确的第三边的个数
                right = numsLen
                while left < right:
                    mid = left + (right - left) // 2
                    if nums[mid] < sum:
                        # 下一轮搜素区间是 [mid + 1, right]
                        left = mid + 1
                    else:
                        # 下一轮搜素区间是 [left, mid]
                        right = mid
                count = count + (left - j - 1)
        return count


print(Solution().triangleNumber([2, 3, 2, 4]))
