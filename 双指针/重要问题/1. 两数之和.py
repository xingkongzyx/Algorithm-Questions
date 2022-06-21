class Solution(object):
    def twoSum(self, nums, target):
        record = {}
        
        for i in range(len(nums)):
            found = target - nums[i]
            
            if found in record:
                return [record[found], i]
            
            record[nums[i]] = i
            
        return [-1, -1]
    
Solution.twoSum(nums = [2,7,11,15], target = 9)
