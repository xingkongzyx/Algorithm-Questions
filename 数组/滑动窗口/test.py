class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        left = 0
        right = 0
        total = 0
        maxavg = float('-inf')

        while right < len(nums):
            rightNum = nums[right]
            total += rightNum
            if right - left + 1 == k:
                # print(total)
                maxavg = max(maxavg, total / k)

            if right - left + 1 == k:
                leftNum = nums[left]
                total -= leftNum
                left += 1

            right += 1
        # print(maxavg)
        return maxavg


Solution().findMaxAverage([-1], 1)
