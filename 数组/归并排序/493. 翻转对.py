class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = [0 for _ in nums]
        
        res = self.calculatePairs(0, len(nums) - 1, nums, temp)
        return res
    
    def calculatePairs(self, leftBound, rightBound, nums, tempArr):
        if leftBound == rightBound:
            return 0
        
        left = leftBound
        right = rightBound
        mid = (left + right) // 2
        
        leftPairs = self.calculatePairs(left, mid, nums, tempArr)
        rightPairs = self.calculatePairs(mid + 1, right, nums, tempArr)
        
        count = 0
        
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if nums[i] > 2 * nums[j]:
                count += (mid - i + 1)
                j += 1
            else:
                i += 1
        
        for i in range(left, right + 1):
            tempArr[i] = nums[i]
        
        i = left
        j = mid + 1
        insertPointer = left
        
        while insertPointer <= right:
            if i == mid + 1:
                nums[insertPointer] = tempArr[j]
                j += 1
            elif j == right + 1:
                nums[insertPointer] = tempArr[i]
                i += 1
            elif tempArr[i] <= tempArr[j]:
                nums[insertPointer] = tempArr[i]
                i += 1
            else:
                nums[insertPointer] = tempArr[j]
                j += 1
            insertPointer += 1
        
        return count + leftPairs + rightPairs

print(Solution().reversePairs([2,4,3,5,1]))
