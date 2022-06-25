class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        right = sum(nums)
        left = max(nums)

        while left < right:
            mid = left + (right - left) // 2
            numOfSplitArr = self.calcualteArrs(nums, mid)
            if numOfSplitArr <= m:
                right = mid
            else:
                left = mid + 1
        return left
    def calcualteArrs(self, nums, maxVal):
        count = 0
        sum = 0
        for i in range(len(nums)):
            if sum + nums[i] > maxVal:
                count += 1
                sum = nums[i]
            else:
                sum += nums[i]
        return count + 1

print(Solution().splitArray(nums = [1,4,4], m = 3))
