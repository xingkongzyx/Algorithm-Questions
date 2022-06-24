class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1Len = len(nums1)
        nums2Len = len(nums2)
        
        numOfleftEle = (nums1Len + nums2Len + 1) // 2
        
        if nums1Len > nums2Len:
            nums1, nums2 = nums2, nums1
            nums1Len, nums2Len = nums2Len, nums1Len
            
        left = 0
        right = nums1Len
        #* 第一个数组分割线所在的位置就是在 i(代表左边有 i 个元素), 分割线左边元素范围是 [0, i-1], 右边的范围是[i, num1Len - 1]
        #* 第二个数组分割线所在的位置就是在 j, 分割线左边元素范围是 [0, j-1], 右边的范围是[j, num2Len - 1]. "j = numOfleftEle - i"
        #* 希望满足的条件 num1[i-1] <= nums2[j] && nums2[j-1] <= nums1[i]
        while left < right:
            i = (left + right + 1) // 2
            j = numOfleftEle - i

            
            if nums1[i-1] > nums2[j]:
                right = i - 1
            else:
                left = i
        nums1Line = left
        nums2Line = numOfleftEle - left
        print("第一组分割线的结果是", nums1[0:nums1Line], nums1[nums1Line:])
        print("第二组分割线的结果是", nums2[0:nums2Line], nums2[nums2Line:])
        
        nums1LeftMax = nums1[nums1Line - 1] if nums1Line > 0 else float('-inf')
        nums1RightMin = nums1[nums1Line] if nums1Line < nums1Len else float('inf')
        nums2LeftMax = nums2[nums2Line - 1] if nums2Line > 0 else float('-inf')
        nums2RightMin = nums2[nums2Line] if nums2Line < nums2Len else float('inf')

        
        leftMax = max(nums1LeftMax, nums2LeftMax)
        rightMin = min(nums1RightMin, nums2RightMin)
        
        
        if (nums1Len + nums2Len) % 2 != 0:
            print("是奇数，因为奇数的时候左边比右边多一个值，所以直接返回左边最大的值", leftMax)
            return leftMax
        
        print(f"同于计算的两个数字是: {leftMax}, {rightMin}")
        
        result = (leftMax + rightMin) / 2
        print(result)
        return result
# Solution().findMedianSortedArrays([2,4,6,15], [1,7,8,10,17])
Solution().findMedianSortedArrays([1,3], [2])
