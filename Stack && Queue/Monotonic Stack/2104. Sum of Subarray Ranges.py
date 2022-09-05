""" 
* 结合这道题来考虑。由于我们要求的是所有子数组最大元素和最小元素的差值；有一种想法是，我们考虑每个元素成为了多少个区间的最大值，还有多少个区间的最小值。前者的数量就是该元素在累计求和中被加的次数，后者则是被减的次数。
* 这样我们只需要一种遍历一遍的方式获得每个元素是多少个区间的最大最小值即可在O(n)的时间里求出结果。
? 提问: https://leetcode.cn/problems/sum-of-subarray-ranges/solution/wei-rao-li-lun-dan-diao-zhan-on-by-wfnus-esro/1415948
? 链接：https://leetcode.cn/problems/sum-of-subarray-ranges/solution/wei-rao-li-lun-dan-diao-zhan-on-by-wfnus-esro/

? https://leetcode.cn/problems/sum-of-subarray-ranges/solution/onjie-fa-dan-diao-zhan-qiu-mei-ge-shu-zu-r8zj/
"""


class Solution:
    def subArrayRanges(self, nums) -> int:
        leftMinBound = [-1 for _ in nums]
        rightMinBound = [len(nums) for _ in nums]

        minRecord = [0 for _ in nums]

        # find next smaller element
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[i]:
                poppedIdx = stack.pop()
                rightMinBound[poppedIdx] = i
            stack.append(i)

        # find previous smaller element
        stack = []
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[j]:
                poppedIdx = stack.pop()
                leftMinBound[poppedIdx] = j
            stack.append(j)

        for i in range(len(nums)):
            minRecord[i] = (i - leftMinBound[i]) * (rightMinBound[i] - i)

        leftMaxBound = [-1 for _ in nums]
        rightMaxBound = [len(nums) for _ in nums]

        maxRecord = [0 for _ in nums]

        stack = []

        # find next greater element
        for i in range(len(nums)):
            while stack and nums[i] >= nums[stack[-1]]:
                poppedIdx = stack.pop()
                rightMaxBound[poppedIdx] = i
            stack.append(i)

        stack = []
        # find previous greater element
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] > nums[stack[-1]]:
                poppedIdx = stack.pop()
                leftMaxBound[poppedIdx] = j
            stack.append(j)

        for i in range(len(nums)):
            maxRecord[i] = (i - leftMaxBound[i]) * (rightMaxBound[i] - i)

        print(minRecord)
        print(maxRecord)

        res = 0
        for i in range(len(minRecord)):
            res += nums[i] * (maxRecord[i] - minRecord[i])

        return res
