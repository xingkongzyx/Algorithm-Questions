""" 
! 这道题就是 974 的延申，求得不再是满足要求的subarray的个数，而是是否存在某个长度大于等于 2 的 subarray, 所以 hashmap 中的 value 不再需要存储 modRes 出现的频次，而是存储 modRes 第一次出现的位置

? 为什么寻找取余的理论基础: 看 974 题

* 1. preSum 保存到当前位置 i 的前缀和, map 保存 <前缀和对k的取余 modRes, 第一次出现 modRes 的位置>
* 2. 遍历 nums 数组,每次对更新后的 preSum 取余,然后判断在位置 i 之前是否存在位置使得前缀和取余后也等于 modRes. 如存在且位置之差 >=2 (满足题目中子数组至少有两个数的要求), 则返回 True
* 3. 如果一直遍历完,说明不符合条件,返回false
"""
class Solution(object):
    def checkSubarraySum(self, nums, k):
        
        from collections import defaultdict

        map = defaultdict(int)
        map[0] = -1
        
        preSum = 0
        
        for i in range(len(nums)):
            preSum += nums[i]
            
            modRes = preSum % k
            if modRes in map:
                if i - map[modRes] >= 2:
                    return True
            else:
                map[modRes] = i

        return False

r = Solution().checkSubarraySum(nums = [23,2,6,4,7], k = 13)
print(r)
