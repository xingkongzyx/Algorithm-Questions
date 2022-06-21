class Solution(object):
    def numberOfSubarrays(self, nums, k):
        count = 0
        
        #* 获取 nums数组 [i,j] 之间奇数数字的数量
        for i in range(len(nums)):
            oddNums = 0
            for j in range(i, len(nums)):
                if nums[j] % 2 == 1:
                    oddNums += 1
                
                if oddNums == k:
                    count += 1
                    
        return count

res = Solution().numberOfSubarrays(nums = [2,4,6], k = 1)
print(res)
