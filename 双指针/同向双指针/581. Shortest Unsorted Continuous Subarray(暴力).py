""" 
* 最终目的是让整个数组有序，那么我们可以先将数组拷贝一份进行排序，然后使用两个指针 i 和 j 分别找到左右两端第一个不同的地方，那么 [i, j] 这一区间即是答案。
/ 时间复杂度: O(nlogn)
/ 空间复杂度: O(n)
? https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/solution/gong-shui-san-xie-yi-ti-shuang-jie-shuan-e1le/

"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        copyArr = nums[:]
        
        copyArr.sort()
        
        startIdx = 0
        endIdx = 0
        
        for i in range(len(nums)):
            if nums[i] != copyArr[i]:
                startIdx = i
                break
        
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] != copyArr[j]:
                endIdx = j
                break
        
        return 0 if startIdx == endIdx else endIdx - startIdx + 1
