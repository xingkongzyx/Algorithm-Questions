
# ? https://leetcode.cn/problems/median-of-two-sorted-arrays/solution/he-bing-yi-hou-zhao-gui-bing-guo-cheng-zhong-zhao-/ 

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1Len = len(nums1)
        nums2Len = len(nums2)
        
        #* 上取整，保证总的元素数量为奇数的时候分割线的左边能比分割线右边多一个元素.nums1Len = 5，nums2Len = 6 numOfLeftElements = (5+6+1)//2 = 6
        #* 而当总的元素个数为偶数的时候，分割线左边右边元素个数相等. nums1Len = 5，nums2Len = 5 numOfLeftElements = (5+5+1)//2 = 5
        numOfLeftElements = (nums1Len + nums2Len + 1) // 2
        
        #/ 始终保证nums1为较短的数组，nums1过长可能导致j为负数而越界
        if nums1Len > nums2Len:
            nums1, nums2 = nums2, nums1
            nums1Len, nums2Len = nums2Len, nums1Len
            
        left = 0
        right = nums1Len
        #* 设 i 为 nums1 中分割线位置. i 代表分割线左边有 i 个元素, 第一个数组分割线左边元素范围是 [0, i-1], 右边的范围是 [i, num1Len - 1]
        #* 设 j 为 nums2 中分割线位置. j 代表分割线左边有 j 个元素, 第二个数组分割线左边元素范围是 [0, j-1], 右边的范围是[j, num2Len - 1]. 
        #! 两个分割线之间的关系是〖j = numOfLeftElements - i〗
        #* 希望满足的条件是「分割线左侧元素小于等于分割线右侧元素」同一个数组的分割线两侧肯定满足这个条件, 所以这里真正的指向是〚交叉满足〛, 也就是 num1[i-1] <= nums2[j] && nums2[j-1] <= nums1[i]
        #> 等价于在 [0, nums1Len] 中找到最大的i使得 nums1[i-1] <= nums2[j]，因此可以使用二分查找。
        while left < right:
            i = (left + right + 1) // 2
            j = numOfLeftElements - i
  
            if nums1[i-1] > nums2[j]:
                right = i - 1
            else:
                left = i
        nums1Line = left
        nums2Line = numOfLeftElements - left
        # print("第一组分割线的结果是", nums1[0:nums1Line], nums1[nums1Line:])
        # print("第二组分割线的结果是", nums2[0:nums2Line], nums2[nums2Line:])
        
        #* 分割线找到后，若「nums1Len + nums2Len」为奇数，分割线左侧的最大值即为中位数；若为偶数，分割线左侧的最大值与分割线右侧的最小值的平均数即为中位数。
        #* 因为左侧希望找到的是最大值, 所以如果左侧分割线出现在 i = 0 的情况, 意味着左侧没有元素, 那么给予「无穷小值」作为默认值, 这样才不会影响后续左边取最大值。
        nums1LeftMax = nums1[nums1Line - 1] if nums1Line > 0 else float('-inf')
        nums1RightMin = nums1[nums1Line] if nums1Line < nums1Len else float('inf')
        nums2LeftMax = nums2[nums2Line - 1] if nums2Line > 0 else float('-inf')
        nums2RightMin = nums2[nums2Line] if nums2Line < nums2Len else float('inf')

        
        leftMax = max(nums1LeftMax, nums2LeftMax)
        rightMin = min(nums1RightMin, nums2RightMin)
             
        if (nums1Len + nums2Len) % 2 != 0:
            #* 若「nums1Len + nums2Len」为奇数，分割线左侧的最大值即为中位数；
            return leftMax
        else:
            # *若为偶数，分割线左侧的最大值与分割线右侧的最小值的平均数即为中位数。
            return (leftMax + rightMin) / 2

       

