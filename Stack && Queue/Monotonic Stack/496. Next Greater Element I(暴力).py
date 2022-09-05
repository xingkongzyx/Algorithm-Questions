""" 
* 对于 nums1 的每个元素, 在 nums2 中找到它, 假设它的下标为 i, 那么从第 i+1 位开始搜索是否存在比它大的, 找到就将该值加入记录中, 否则加入 -1

/ 时间复杂度: O(mn), 其中 m 是 nums1的长度, n 是 nums2的长度。
/ 空间复杂度: O(n), 哈希表占用额外空间
"""
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        record = {}
        
        for i in range(len(nums2)):
            record[nums2[i]] = i
                
        resArr = []
        
        for num in nums1:
            numIdxInNums2 = record[num]
            res = -1
            for i in range(numIdxInNums2 + 1, len(nums2)):
                if nums2[i] > num:
                    res = nums2[i]
                    break
            resArr.append(res)
        return resArr
        
Solution().nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])
Solution().nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4])
