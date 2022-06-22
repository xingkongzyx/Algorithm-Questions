
#/ 时间复杂度 O(n^2)
class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        #* 获取 [i ... j] 闭区间的和, 这也就是题目中求的子数组的和, 如果等于 k, 则 count 加 1
        for i in range(0, len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count

#/ 这种做法复杂度还是O(n^2)  
    def subarraySumPresum(self, nums, k):
        count = 0
        #! preSum 比 nums 数组多一位，所以preSum[1] 代表「原数组中前1位的和」，也就是 🔵preSum[1] = nums[0]🔵；以此类推，preSum[i] 代表「原数组中前 i 位的和」，因为原数组的下标是起始于0的，也就是 🔵preSum[i] = nums[0] + nums[1] + ... + nums[i-1]🔵
        preSum = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(preSum)):
            preSum[i] = preSum[i-1] + nums[i-1]
            
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                #* 使用 preSum 获取 [i...j] 闭区间的和, 也就是 "nums[i]+nums[i+1]+...+nums[j]"。因为上面的定义, preSum[j + 1] 代表的就是 nums 数组中前 j 位的和(nums数组是以0起步的), 而想获得 [i...j] 闭区间的和, 还需要得到 nums[0]+...+nums[i-1] 前 i-1 位的和, 然后进行减法, [0...i-1] 的和转换到前缀和数组就是 preSum[i]
                if preSum[j + 1] - preSum[i] == k:
                    count += 1
        
        return count

r1 = Solution().subarraySumPresum(nums = [1,2,3], k = 3)
r2 = Solution().subarraySumPresum(nums = [1,1,1], k = 2)
print(r1, r2)
